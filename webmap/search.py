from webmap import urls as u
from arcgis.mapping import WebMap
import logging

# adapted from https://www.esri.com/arcgis-blog/products/apps/field-mobility/customize-feature-search-web-maps-python/


def search_item(url, field, matchExists=False, field_type="esriFieldTypeString"):
    """
    List of fields to specify search in a web map.

    :param url: Url for the target search layer.
    :type url: String
    :param field: Field in attribute table of layer to search.
    :type field: String
    :param matchExists: Indicates whether to search for exact matches only.
    :type matchExists: Boolean
    :param field_type: Esri data type of field parameter.
    :type field_type: String
    """
    item_list = [url, field, matchExists, field_type]
    return item_list


# search list for fields in a web map
# each element in list in a list specifying:
# 1) url, 2) field of layer to search, 3) exactMatch bool, 4) field type
search_list = [
    search_item(u.land_use_urls[3], "FULLADDR"),
    search_item(u.land_use_urls[2], "FULLADDR"),
    search_item(u.land_use_urls[2], "TAXLOT"),
    search_item(u.land_use_urls[1], "NAME"),
    search_item(u.land_use_urls[0], "FACILITYID"),
    search_item(u.land_use_urls[0], "MAPNUMX"),
    search_item(u.city_parcels_url, "MAPNUM"),
    search_item(u.city_parcels_url, "SITUS"),
    search_item(u.city_parcels_url, "NAME"),
    search_item(u.county_parcels_url, "MAPNUM"),
    search_item(u.county_parcels_url, "SITUS"),
    search_item(u.county_parcels_url, "NAME"),
    search_item(u.assessment_maps_url, "MAPNUMBE_1"),
    search_item(u.tax_code_url, "TaxCode"),
    search_item(u.bia_urls[1], "LARName"),
    search_item(u.bia_urls[0], "Land_Area_"),
    search_item(u.aiannha_urls[6], "NAME"),
    search_item(u.aiannha_urls[6], "AIANNH"),
    search_item(u.aiannha_urls[5], "NAME"),
    search_item(u.aiannha_urls[5], "AIANNH"),
    search_item(u.aiannha_urls[4], "NAME"),
    search_item(u.aiannha_urls[4], "AIANNH"),
    search_item(u.aiannha_urls[3], "NAME"),
    search_item(u.aiannha_urls[3], "AIANNH"),
    search_item(u.aiannha_urls[2], "NAME"),
    search_item(u.aiannha_urls[2], "AIANNH"),
    search_item(u.aiannha_urls[1], "NAME"),
    search_item(u.aiannha_urls[1], "AIANNH"),
    search_item(u.aiannha_urls[0], "NAME"),
    search_item(u.aiannha_urls[0], "AIANNH"),
    search_item(u.boundaries_urls[6], "NAME"),
    search_item(u.boundaries_urls[2], "AcctNum"),
    search_item(u.boundaries_urls[2], "MAPNUM"),
    search_item(u.school_locations, "Institution_Name_Line1"),
    search_item(u.school_locations, "Site_Address_Line1"),
    search_item(u.school_districts_urls[8], "ADDRESS"),
    search_item(u.school_districts_urls[8], "SCHOOL_DIS"),
    search_item(u.school_districts_urls[8], "SCHOOL_NAM"),
    search_item(u.school_districts_urls[7], "Name"),
    search_item(u.school_districts_urls[6], "Name"),
    search_item(u.school_districts_urls[5], "ADDRESS"),
    search_item(u.school_districts_urls[5], "SCHOOL_DIS"),
    search_item(u.school_districts_urls[5], "SCHOOL_NAM"),
    search_item(u.school_districts_urls[4], "EDUCATIONAL_SERVICE_DISTRICT_NAME"),
    search_item(u.school_districts_urls[4], "GRADE_K_NAME"),
    search_item(u.school_districts_urls[4], "SCHOOL_DISTRICT_NAME"),
    search_item(u.school_districts_urls[3], "GRADE_8_NAME"),
    search_item(u.school_districts_urls[2], "GRADE_12_NAME"),
    search_item(u.school_districts_urls[1], "DISTRICTNAME"),
    search_item(u.school_districts_urls[1], "NAME"),
    search_item(u.school_districts_urls[0], "NAME"),
    search_item(u.historic_cultural_areas_urls[3], "Artist"),
    search_item(u.historic_cultural_areas_urls[3], "FACILITYID"),
    search_item(u.historic_cultural_areas_urls[3], "Title_of_Piece"),
    search_item(u.historic_cultural_areas_urls[2], "OHSR_HX_NAME"),
    search_item(u.agreements_urls[4], "DOC_NO"),
    search_item(u.agreements_urls[4], "UNREC_NUM"),
    search_item(u.agreements_urls[3], "INSTRUMENT"),
    search_item(u.agreements_urls[2], "InstrumentNumber"),
    search_item(u.agreements_urls[1], "INSTRUMENT"),
    search_item(u.agreements_urls[0], "INST_NUM"),
    search_item(u.agreements_urls[0], "DISTRICT_1"),
    search_item(u.agreements_urls[0], "FINAL_ORDI"),
    search_item(u.agreements_urls[0], "FIRST_RESO"),
    search_item(u.marijuana_adult_urls[13], "BusinessAddress"),
    search_item(u.marijuana_adult_urls[13], "BusinessName"),
    search_item(u.marijuana_adult_urls[13], "BusinessOwner"),
    search_item(u.marijuana_adult_urls[12], "BusinessName"),
    search_item(u.marijuana_adult_urls[11], "FacilityAddress"),
    search_item(u.marijuana_adult_urls[11], "FacilityName"),
    search_item(u.marijuana_adult_urls[10], "FacilityName"),
    search_item(u.marijuana_adult_urls[9], "NAME"),
    search_item(u.marijuana_adult_urls[8], "NAME"),
    search_item(u.marijuana_adult_urls[7], "NAME"),
    search_item(u.marijuana_adult_urls[7], "CLASS"),
    search_item(u.marijuana_adult_urls[6], "NAME"),
    search_item(u.marijuana_adult_urls[5], "ADDRESS"),
    search_item(u.marijuana_adult_urls[5], "SCHOOL_NAM"),
    search_item(u.marijuana_adult_urls[4], "SCHOOL_NAM"),
    search_item(u.marijuana_adult_urls[1], "NAME"),
    search_item(u.marijuana_adult_urls[0], "NAME"),
    search_item(u.zoning_urls[4], "LAYER"),
    search_item(u.zoning_urls[2], "FOOD_ZONE"),
    search_item(u.zoning_urls[1], "ZONECLASS"),
    search_item(u.zoning_urls[1], "ZONEDESC"),
    search_item(u.zoning_urls[0], "COMPCLASS"),
    search_item(u.zoning_urls[0], "COMPDESC"),
    search_item(u.planning_urls[5], "NAME"),
    search_item(u.planning_urls[5], "ADDRESS"),
    search_item(u.planning_urls[5], "MAPNUM"),
    search_item(u.planning_urls[4], "NAME"),
    search_item(u.planning_urls[3], "RSIA_NAME"),
    search_item(u.transportation_urls[23], "TSSU_ID"),
    search_item(u.transportation_urls[22], "FACILITYID"),
    search_item(u.transportation_urls[19], "FACILITYID"),
    search_item(u.transportation_urls[19], "HistoricID"),
    search_item(u.transportation_urls[18], "LAYER"),
    search_item(u.transportation_urls[18], "ROUTE_NUMBER"),
    search_item(u.stormwater_urls[11], "FACILITYID"),
    search_item(u.stormwater_urls[11], "HistoricID"),
    search_item(u.cell_towers_url, "Street_Add"),
    search_item(u.cell_towers_url, "NOTES"),
]


def get_layer_id(layers, layer_url):
    layer_id = None
    for lyr in layers:
        logging.debug("Searching layer %s for url.", lyr["title"])
        if lyr["layerType"] == "GroupLayer" and layer_id is None:
            layer_id = get_layer_id(lyr["layers"], layer_url)
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
        else:
            logging.debug("Layer %s not found.", srch[0])
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
