from webmap import webmap as w
from webmap import urls as u
from arcgis.mapping import MapServiceLayer
import logging


def missing_sidewalks_layer_names(post):
    """
    Create list of key names for layer definition data.
    """
    layer_stub = [
        "park_street_sidewalks_export",
        "private_street_sidewalks_export",
        "state_street_sidewalks_export",
        "arterial_sidewalks_export",
        "collector_sidewalks_export",
        "local_collector_sidewalks_export",
        "local_street_sidewalks_export",
        "streets",
        "sidewalks",
        "addresses",
        "hillslope",
        "taxlots",
    ]
    layer_name = []
    for lyr in layer_stub:
        layer_name.append("missing_sidewalks_" + lyr + post)
    # layer order is reversed from menu order
    layer_name.reverse()
    return layer_name


def missing_sidewalks_layers(group_lyr, template):
    """
    Add layers for missing sidewalks map.

    :param group_lyr: Group layer definition target for layers.
    :return: Updates group layer definition with layers.
    """
    popup_names = missing_sidewalks_layer_names("_popup")
    label_names = missing_sidewalks_layer_names("_label")
    parent_group = w.group_layer("Missing Sidewalks")
    url_list = u.missing_sidewalks_urls
    for i in range(5, 12):
        map_lyr = MapServiceLayer(url_list[i])
        fc = w.feature_class(map_lyr, 0.5)
        if fc["title"] == "park_street_sidewalks_export":
            fc.update({"title": "Park"})
        if fc["title"] == "private_street_sidewalks_export":
            fc.update({"title": "Private"})
        if fc["title"] == "state_street_sidewalks_export":
            fc.update({"title": "State"})
        if fc["title"] == "arterial_sidewalks_export":
            fc.update({"title": "Arterial"})
        if fc["title"] == "collector_sidewalks_export":
            fc.update({"title": "Collector"})
        if fc["title"] == "local_collector_sidewalks_export":
            fc.update({"title": "Local Collector"})
        if fc["title"] == "local_street_sidewalks_export":
            fc.update({"title": "Local Street"})
        fc.update({"popupInfo": template[popup_names[i]]})
        fc.update({"layerDefinition": template[label_names[i]]})
        parent_group["layers"].append(fc)

    city_group = w.group_layer("City Layers")
    for i in range(0, 5):
        map_lyr = MapServiceLayer(url_list[i])
        fc = w.feature_class(map_lyr, 0.5)
        if fc["title"] == "streets":
            fc.update({"title": "Streets"})
        if fc["title"] == "sidewalks":
            fc.update({"title": "Sidewalks"})
        if fc["title"] == "addresses":
            fc.update({"title": "Addresses"})
            fc.update({"visibility": False})
        if fc["title"] == "hillslope":
            fc.update({"title": "Steep Slopes"})
        if fc["title"] == "taxlots":
            fc.update({"title": "Taxlots"})
        fc.update({"popupInfo": template[popup_names[i]]})
        fc.update({"layerDefinition": template[label_names[i]]})
        city_group["layers"].append(fc)

    group_lyr["layers"].append(city_group)
    group_lyr["layers"].append(parent_group)


def missing_sidewalks_map(project_map, template):
    """
    Adding missing sidewalks layers to project map.

    :param project_map: Web map to update with reference layers.
    :return: Updates the web map, adding reference layers.
    :rtype: None.
    """
    basemap = w.group_layer("Missing Sidewalks Map")
    missing_sidewalks_layers(basemap, template)
    logging.info("missing sidewalk layers assembled")
    map_def = project_map.get_data()
    map_def["operationalLayers"].append(basemap)
    project_map.update({"text": str(map_def)})
    logging.info("missing sidewalk layers added to basemap")
