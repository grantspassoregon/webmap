from webmap import webmap as w
from webmap import urls as u
from webmap import template as t
from arcgis.mapping import MapServiceLayer
import logging


def missing_sidewalks_layer_names(post):
    """
    Create list of key names for layer definition data.
    """
    layer_stub = [
        "local_street_sidewalks_export",
        "local_collector_sidewalks_export",
        "collector_sidewalks_export",
        "arterial_sidewalks_export",
        "state_street_sidewalks_export",
        "private_street_sidewalks_export",
        "park_street_sidewalks_export",
        "local_street_sidewalks_undeveloped",
        "local_collector_sidewalks_undeveloped",
        "collector_sidewalks_undeveloped",
        "arterial_sidewalks_undeveloped",
        "state_street_sidewalks_undeveloped",
        "private_street_sidewalks_undeveloped",
        "park_street_sidewalks_undeveloped",
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
    url_list = u.missing_sidewalks_urls
    # parent_group = w.group_layer("Sidewalks")
    # for i in range(0, len(url_list)):
    #     map_lyr = MapServiceLayer(url_list[i])
    #     fc = w.feature_class(map_lyr, 0.5)
    #     parent_group["layers"].append(fc)

    # group_lyr["layers"].append(parent_group)

    missing_group = w.group_layer("Missing Sidewalks")
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
        missing_group["layers"].append(fc)

    undeveloped_group = w.group_layer("Undeveloped")
    for i in range(12, 19):
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
        undeveloped_group["layers"].append(fc)

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
    group_lyr["layers"].append(undeveloped_group)
    group_lyr["layers"].append(missing_group)


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


def plss_layers(group_lyr, template):
    """
    PLSS layers from BLM.

    :param group_lyr: Group layer definition target for layers.
    :return: Updates group layer definition with layers.
    :rtype: None
    """
    popup_names = t.layer_names("plss", t.plss_names, "_popup")
    label_names = t.layer_names("plss", t.plss_names, "_label")
    url_list = u.plss_urls

    plss_group = w.group_layer("PLSS")
    for index, url in enumerate(url_list):
        map_lyr = MapServiceLayer(url)
        fc = w.feature_class(map_lyr, 0.5)
        if popup_names[index] in template:
            fc.update({"popupInfo": template[popup_names[index]]})
        if label_names[index] in template:
            fc.update({"layerDefinition": template[label_names[index]]})
        plss_group["layers"].append(fc)
    group_lyr["layers"].append(plss_group)


def bia_layers(group_lyr, template):
    """
    Bureau of Indian Affairs tribal land boundaries.


    :param group_lyr: Group layer definition target for layers.
    :return: Updates group layer definition with layers.
    :rtype: None
    """
    popup_names = t.layer_names("bia", t.bia_names, "_popup")
    label_names = t.layer_names("bia", t.bia_names, "_label")
    url_list = u.bia_urls

    bia_group = w.group_layer("BIA Tribal Lands")
    for index, url in enumerate(url_list):
        map_lyr = MapServiceLayer(url)
        fc = w.feature_class(map_lyr, 0.5)
        if popup_names[index] in template:
            fc.update({"popupInfo": template[popup_names[index]]})
        if label_names[index] in template:
            fc.update({"layerDefinition": template[label_names[index]]})
        bia_group["layers"].append(fc)
    group_lyr["layers"].append(bia_group)


def aiannha_layers(group_lyr, template):
    """
    American Indian, Alaska Native, and Native Hawaiian Areas from Tigerweb.

    :param group_lyr: Group layer definition target for layers.
    :return: Updates group layer definition with layers.
    :rtype: None
    """
    popup_names = t.layer_tags("aiannha", u.aiannha_urls, "_popup")
    label_names = t.layer_tags("aiannha", u.aiannha_urls, "_label")
    url_list = u.aiannha_urls

    aiannha_group = w.group_layer("AIANNHA Areas")
    for index, url in enumerate(url_list):
        map_lyr = MapServiceLayer(url)
        fc = w.feature_class(map_lyr, 0.5)
        if popup_names[index] in template:
            fc.update({"popupInfo": template[popup_names[index]]})
        if label_names[index] in template:
            fc.update({"layerDefinition": template[label_names[index]]})
        aiannha_group["layers"].append(fc)
    group_lyr["layers"].append(aiannha_group)


def city_boundaries(group_lyr, template):
    """
    Regulatory boundaries for the City of Grants Pass.

    :param group_lyr: Group layer definition target for layers.
    :return: Updates group layer definition with layers.
    :rtype: None
    """
    # popup_names = t.layer_names("boundaries", t.city_boundaries_names, "_popup")
    # label_names = t.layer_names("boundaries", t.city_boundaries_names, "_label")
    popup_names = t.layer_tags("city_boundaries", u.boundaries_urls, "_popup")
    label_names = t.layer_tags("city_boundaries", u.boundaries_urls, "_label")
    url_list = u.boundaries_urls

    boundaries_group = w.group_layer("City Boundaries")
    for index, url in enumerate(url_list):
        map_lyr = MapServiceLayer(url)
        fc = w.feature_class(map_lyr, 0.5)
        if fc["title"] == "City Limits 2016":
            fc.update({"title": "City Limits"})
        if fc["title"] == "UGB 2014":
            fc.update({"title": "Urban Growth Boundary"})
        if fc["title"] == "Urban Reserve 2014":
            fc.update({"title": "Urban Reserve"})
        if fc["title"] == "GP_NSWE_Town_Sections":
            fc.update({"title": "Town Section Cardinals"})
        if fc["title"] == "CMAQ Boundary (2007 UGB)":
            fc.update({"title": "CMAQ Boundary"})
        if fc["title"] == "JoCo_Boundary":
            fc.update({"title": "Josephine County Line"})
        if popup_names[index] in template:
            fc.update({"popupInfo": template[popup_names[index]]})
        if label_names[index] in template:
            fc.update({"layerDefinition": template[label_names[index]]})
        # fc.update({"popupInfo": template[popup_names[index]]})
        # fc.update({"layerDefinition": template[label_names[index]]})
        boundaries_group["layers"].append(fc)
    group_lyr["layers"].append(boundaries_group)


def school_layers(group_lyr, template):
    """
    Grants Pass District 7 and Three Rivers School District boundaries.

    :param group_lyr: Group layer definition target for layers.
    :return: Updates group layer definition with layers.
    :rtype: None
    """
    popup_names = t.layer_tags("schools", u.school_districts_urls, "_popup")
    label_names = t.layer_tags("schools", u.school_districts_urls, "_label")
    # popup_names = t.layer_names("boundaries", t.school_names, "_popup")
    # label_names = t.layer_names("boundaries", t.school_names, "_label")
    url_list = u.school_districts_urls

    schools_group = w.group_layer("School Districts")
    for index, url in enumerate(url_list):
        map_lyr = MapServiceLayer(url)
        fc = w.feature_class(map_lyr, 0.5)
        if fc["title"] == "Schools":
            fc.update({"title": "School Locations"})
        if fc["title"] == "GP Area School Properties":
            fc.update({"title": "School Grounds"})
        if fc["title"] == "GP Area Schools 1000' Buffer":
            fc.update({"title": "Schools 1000' Buffer"})
        if index == 2:
            fc.update({"title": "High School Zones"})
        if index == 3:
            fc.update({"title": "Middle School Zones"})
        if index == 4:
            fc.update({"title": "Elementary School Zones"})
        if fc["title"] == "School Zone":
            fc.update({"title": "School Zones"})
        if fc["title"] == "District 7":
            fc.update({"title": "District 7 Boundary"})
        if fc["title"] == "3 Rivers School District":
            fc.update({"title": "Three Rivers District Boundary"})
        if popup_names[index] in template:
            fc.update({"popupInfo": template[popup_names[index]]})
        if label_names[index] in template:
            fc.update({"layerDefinition": template[label_names[index]]})
        # fc.update({"popupInfo": template[popup_names[index]]})
        # fc.update({"layerDefinition": template[label_names[index]]})
        schools_group["layers"].append(fc)
    group_lyr["layers"].append(schools_group)


def city_basemap(project_map, template):
    """
    Add common reference layers to web map.

    :param project_map: Web map to update with reference layers.
    :return: Updates the web map, adding reference layers.
    :rtype: None.
    """
    logging.info("Building city basemap.")
    basemap = w.group_layer("City of Grants Pass Layers")
    plss_layers(basemap, template)
    logging.info("Regulatory boundaries added to city basemap.")
    map_def = project_map.get_data()
    logging.info("Appending layers to city basemap definition.")
    map_def["operationalLayers"].append(basemap)
    project_map.update({"text": str(map_def)})


def boundaries(project_map, template):
    """
    Regulatory boundaries for City of Grants Pass.

    :param project_map: Web map to update with reference layers.
    :return: Updates the web map, adding reference layers.
    :rtype: None.
    """
    map_name = "boundaries map"
    logging.info("Building %s.", map_name)
    basemap = w.group_layer("Boundaries")
    school_layers(basemap, template)
    logging.info("Adding school district boundaries to %s.", map_name)
    city_boundaries(basemap, template)
    logging.info("City boundaries layers added to boundaries map.")
    aiannha_layers(basemap, template)
    logging.info("AIANNHA layers added to boundaries map.")
    bia_layers(basemap, template)
    logging.info("BIA layers added to boundaries map.")
    plss_layers(basemap, template)
    logging.info("PLSS layers added to boundaries map.")
    map_def = project_map.get_data()
    logging.info("Appending layers to definition.")
    map_def["operationalLayers"].append(basemap)
    project_map.update({"text": str(map_def)})
