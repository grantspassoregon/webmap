from webmap import urls as u
from arcgis.mapping import WebMap

# adapted from https://www.esri.com/arcgis-blog/products/apps/field-mobility/customize-feature-search-web-maps-python/

# search list for fields in a web map
# each element in list in a list specifying:
# 1) url, 2) field of layer to search, 3) exactMatch bool, 4) field type
search_list = [
    [u.city_parcels_url, "MAPNUM", False, "esriFieldTypeString"],
    [u.city_parcels_url, "SITUS", False, "esriFieldTypeString"],
    [u.city_parcels_url, "NAME", False, "esriFieldTypeString"],
    [u.stormwater_urls[11], "FACILITYID", False, "esriFieldTypeString"],
    [u.stormwater_urls[11], "HistoricID", False, "esriFieldTypeString"],
    [u.cell_towers_url, "Street_Add", False, "esriFieldTypeString"],
    [u.cell_towers_url, "NOTES", False, "esriFieldTypeString"],
]


def get_layer_id(layers, layer_url):
    for lyr in layers:
        if lyr["layerType"] == "GroupLayer":
            layer_id = get_layer_id(lyr["layers"], layer_url)
            return layer_id
        elif "url" in lyr:
            if lyr["url"] == layer_url:
                layer_id = lyr["id"]
                return layer_id
        #     else:
        #         raise Exception("Wrong url in layer %s", lyr["id"])
        # else:
        #     raise Exception("No url in layers.")


def add_search_field(properties, id, field, match, field_type):
    d = dict()
    d.update({"id": id})
    f = dict()
    f.update({"name": field})
    f.update({"exactMatch": match})
    f.update({"type": field_type})
    d.update({"field": f})
    properties.append(d)


def search_fields(item, search_list=search_list):
    properties = list()
    wm = WebMap(item)
    lyrs = wm.layers
    for srch in search_list:
        lyr_id = get_layer_id(lyrs, srch[0])
        if lyr_id is not None:
            add_search_field(properties, lyr_id, srch[1], srch[2], srch[3])
    return properties


def add_search(project_map, search_list=search_list):
    properties = search_fields(project_map, search_list)
    map_def = project_map.get_data()
    map_def["applicationProperties"]["viewing"]["search"] = {
        "enabled": True,
        "disablePlaceFinder": False,
        "hintText": "Address or Fields",
        "layers": properties,
    }
    project_map.update({"text": str(map_def)})
