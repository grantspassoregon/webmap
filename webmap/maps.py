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
        fc.update({"visibility": False})
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
        fc.update({"visibility": False})
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
        fc.update({"visibility": False})
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
        fc.update({"visibility": False})
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
        fc.update({"visibility": False})
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


def boundaries(group_lyr, template):
    """
    Regulatory boundaries for City of Grants Pass.

    :param group_lyr: Group layer definition target for layers.
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
    group_lyr["layers"].append(basemap)
    logging.info("Appending layers to %s definition.", map_name)


def aerial_imagery(group_lyr):
    """
    Append aerial imagery layers to group layer.

    :param group_lyr: Group layer to update with target layers.
    :type group_lyr: Group layer
    :return: Updates group layer to include the target layers.
    :rtype: None
    """
    basemap = w.group_layer("Aerial Imagery")
    basemap["layers"].append(u.esri_image_def)
    group_lyr["layers"].append(basemap)


def tax_layers(group_lyr, template):
    """
    Tax parcel layers, county and city versions.

    :param group_lyr: Group layer definition target for layers.
    :return: Updates group layer definition with layers.
    :rtype: None
    """
    popup_names = t.layer_tags("tax_parcels", u.tax_parcel_urls, "_popup")
    label_names = t.layer_tags("tax_parcels", u.tax_parcel_urls, "_label")
    url_list = u.tax_parcel_urls

    tax_group = w.group_layer("Tax Parcels")
    for index, url in enumerate(url_list):
        map_lyr = MapServiceLayer(url)
        fc = w.feature_class(map_lyr, 0.2)
        fc.update({"visibility": False})
        if fc["title"] == "Tax Parcels":
            fc.update({"title": "Taxlots (City)"})
        if fc["title"] == "Assessors Taxlots":
            fc.update({"title": "Taxlots (County)"})
        if fc["title"] == "Tax Codes":
            fc.update({"opacity": 0.2})
        if popup_names[index] in template:
            fc.update({"popupInfo": template[popup_names[index]]})
        if label_names[index] in template:
            fc.update({"layerDefinition": template[label_names[index]]})
        tax_group["layers"].append(fc)
    group_lyr["layers"].append(tax_group)


def land_use_layers(group_lyr, template):
    """
    Land use planning layers for the City of Grants Pass.

    :param group_lyr: Group layer definition target for layers.
    :return: Updates group layer definition with layers.
    :rtype: None
    """
    popup_names = t.layer_tags("land_use", u.land_use_urls, "_popup")
    label_names = t.layer_tags("land_use", u.land_use_urls, "_label")
    url_list = u.land_use_urls

    map_name = "Land Use"
    map_group = w.group_layer(map_name)
    tax_layers(map_group, template)
    for index, url in enumerate(url_list):
        map_lyr = MapServiceLayer(url)
        fc = w.feature_class(map_lyr, 0.5)
        fc.update({"visibility": False})
        if fc["title"] == "JoCo_SiteAddress":
            fc.update({"title": "Addresses (County)"})
        if popup_names[index] in template:
            fc.update({"popupInfo": template[popup_names[index]]})
        if label_names[index] in template:
            fc.update({"layerDefinition": template[label_names[index]]})
        map_group["layers"].append(fc)
        logging.debug("Appending %s to %s layer.", fc["title"], map_name)
    group_lyr["layers"].append(map_group)


def lidar_layers(group_lyr):
    """
    Lidar terrain and surface models from DOGAMI.

    :param group_lyr: Group layer to update with target layers.
    :type group_lyr: Group layer
    :return: Updates group layer to include the target layers.
    :rtype: None
    """
    basemap = w.group_layer("LiDAR Imagery")
    basemap["layers"].append(u.dogami_be_def)
    basemap["layers"].append(u.dogami_hh_def)
    group_lyr["layers"].append(basemap)


def wildfire_layers(group_lyr):
    """
    Wildfire (FS) national map services.

    :param group_lyr: Group layer to update with target layers.
    :type group_lyr: Group layer
    :return: Updates group layer to include the target layers.
    :rtype: None
    """
    basemap = w.group_layer("Wildfire")
    basemap["layers"].append(u.fs_wildfire_potential_def)
    basemap["layers"].append(u.fs_wildfire_housing_def)
    group_lyr["layers"].append(basemap)


def fema_flood_layers(group_lyr, template):
    """
    NFHL flood layers from FEMA.

    :param group_lyr: Group layer definition target for layers.
    :return: Updates group layer definition with layers.
    :rtype: None
    """
    popup_names = t.layer_tags("fema_flood", u.fema_flood_urls, "_popup")
    label_names = t.layer_tags("fema_flood", u.fema_flood_urls, "_label")
    url_list = u.fema_flood_urls

    map_name = "FEMA Flood (NFHL)"
    map_group = w.group_layer(map_name)
    for index, url in enumerate(url_list):
        map_lyr = MapServiceLayer(url)
        fc = w.feature_class(map_lyr, 0.5)
        fc.update({"visibility": False})
        if popup_names[index] in template:
            fc.update({"popupInfo": template[popup_names[index]]})
        if label_names[index] in template:
            fc.update({"layerDefinition": template[label_names[index]]})
        logging.info("Appending %s to %s layer.", fc["title"], map_name)
        map_group["layers"].append(fc)
    group_lyr["layers"].append(map_group)


def fema_nfhl_layers(group_lyr, template):
    """
    NFHL flood layers from FEMA.

    :param group_lyr: Group layer definition target for layers.
    :return: Updates group layer definition with layers.
    :rtype: None
    """
    popup_names = t.layer_tags("fema_flood", u.fema_flood_urls, "_popup")
    label_names = t.layer_tags("fema_flood", u.fema_flood_urls, "_label")
    url_list = u.fema_nfhl_wms_urls

    map_name = "FEMA Flood (NFHL)"
    map_group = w.group_layer(map_name)
    for index, url in enumerate(url_list):
        map_lyr = MapServiceLayer(url)
        fc = w.feature_class(map_lyr, 0.5)
        fc.update({"visibility": False})
        if popup_names[index] in template:
            fc.update({"popupInfo": template[popup_names[index]]})
        if label_names[index] in template:
            fc.update({"layerDefinition": template[label_names[index]]})
        logging.info("Appending %s to %s layer.", fc["title"], map_name)
        map_group["layers"].append(fc)
    group_lyr["layers"].append(map_group)


def historic_cultural_layers(group_lyr, template):
    """
    Historic district, sites and culturally significant sites in the City of Grants Pass.

    :param group_lyr: Group layer definition target for layers.
    :return: Updates group layer definition with layers.
    :rtype: None
    """
    popup_names = t.layer_tags("historic", u.historic_cultural_areas_urls, "_popup")
    label_names = t.layer_tags("historic", u.historic_cultural_areas_urls, "_label")
    url_list = u.historic_cultural_areas_urls

    map_name = "Historic/Cultural Areas"
    map_group = w.group_layer(map_name)
    for index, url in enumerate(url_list):
        map_lyr = MapServiceLayer(url)
        fc = w.feature_class(map_lyr, 0.5)
        fc.update({"visibility": False})
        if fc["title"] == "Historic_Sites":
            fc.update({"title": "Historic Sites (OPRD)"})
        if popup_names[index] in template:
            fc.update({"popupInfo": template[popup_names[index]]})
        if label_names[index] in template:
            fc.update({"layerDefinition": template[label_names[index]]})
        logging.debug("Appending %s to %s layer.", fc["title"], map_name)
        map_group["layers"].append(fc)
    group_lyr["layers"].append(map_group)


def zoning_layers(group_lyr, template):
    """
    Zoning, comprehensive plan and overlays for City of Grants Pass.

    :param group_lyr: Group layer definition target for layers.
    :return: Updates group layer definition with layers.
    :rtype: None
    """
    popup_names = t.layer_tags("zoning", u.zoning_urls, "_popup")
    label_names = t.layer_tags("zoning", u.zoning_urls, "_label")
    url_list = u.zoning_urls

    map_name = "Zoning"
    map_group = w.group_layer(map_name)
    for index, url in enumerate(url_list):
        map_lyr = MapServiceLayer(url)
        fc = w.feature_class(map_lyr, 0.5)
        fc.update({"visibility": False})
        if fc["title"] == "Comprehensive Plan 2014":
            fc.update({"title": "Comprehensive Plan"})
        if popup_names[index] in template:
            fc.update({"popupInfo": template[popup_names[index]]})
        if label_names[index] in template:
            fc.update({"layerDefinition": template[label_names[index]]})
        logging.debug("Appending %s to %s layer.", fc["title"], map_name)
        map_group["layers"].append(fc)
    group_lyr["layers"].append(map_group)


def marijuana_adult_use_layers(group_lyr, template):
    """
    Locations and buffers for marijuana and adult use planning at the City of Grants Pass.

    :param group_lyr: Group layer definition target for layers.
    :return: Updates group layer definition with layers.
    :rtype: None
    """
    popup_names = t.layer_tags("marijuana_adult_use", u.marijuana_adult_urls, "_popup")
    label_names = t.layer_tags("marijuana_adult_use", u.marijuana_adult_urls, "_label")
    url_list = u.marijuana_adult_urls

    map_name = "Marijuana and Adult Use"
    map_group = w.group_layer(map_name)
    for index, url in enumerate(url_list):
        map_lyr = MapServiceLayer(url)
        fc = w.feature_class(map_lyr, 0.5)
        fc.update({"visibility": False})
        if popup_names[index] in template:
            fc.update({"popupInfo": template[popup_names[index]]})
        if label_names[index] in template:
            fc.update({"layerDefinition": template[label_names[index]]})
        logging.debug("Appending %s to %s layer.", fc["title"], map_name)
        map_group["layers"].append(fc)
    group_lyr["layers"].append(map_group)


def agreements_layers(group_lyr, template):
    """
    Financial and planning agreements with the City of Grants Pass.

    :param group_lyr: Group layer definition target for layers.
    :return: Updates group layer definition with layers.
    :rtype: None
    """
    popup_names = t.layer_tags("agreements", u.agreements_urls, "_popup")
    label_names = t.layer_tags("agreements", u.agreements_urls, "_label")
    url_list = u.agreements_urls

    map_name = "Agreements and Financial"
    map_group = w.group_layer(map_name)
    for index, url in enumerate(url_list):
        map_lyr = MapServiceLayer(url)
        fc = w.feature_class(map_lyr, 0.5)
        fc.update({"visibility": False})
        if popup_names[index] in template:
            fc.update({"popupInfo": template[popup_names[index]]})
        if label_names[index] in template:
            fc.update({"layerDefinition": template[label_names[index]]})
        logging.debug("Appending %s to %s layer.", fc["title"], map_name)
        map_group["layers"].append(fc)
    group_lyr["layers"].append(map_group)


def planning_layers(group_lyr, template):
    """
    Zoning, historic/cultural areas and miscellaneous planning layers for City of Grants Pass.

    :param group_lyr: Group layer definition target for layers.
    :return: Updates group layer definition with layers.
    :rtype: None
    """
    popup_names = t.layer_tags("planning", u.planning_urls, "_popup")
    label_names = t.layer_tags("planning", u.planning_urls, "_label")
    url_list = u.planning_urls

    map_name = "Planning"
    map_group = w.group_layer(map_name)
    conservation = "Proposed Conservation District"
    conservation_group = w.group_layer(conservation)
    for index, url in enumerate(url_list):
        map_lyr = MapServiceLayer(url)
        fc = w.feature_class(map_lyr, 0.5)
        fc.update({"visibility": False})
        if popup_names[index] in template:
            fc.update({"popupInfo": template[popup_names[index]]})
        if label_names[index] in template:
            fc.update({"layerDefinition": template[label_names[index]]})
        logging.debug("Appending %s to %s layer.", fc["title"], map_name)
        if index in [4, 5]:
            conservation_group["layers"].append(fc)
        else:
            map_group["layers"].append(fc)
    map_group["layers"].append(conservation_group)
    zoning_layers(map_group, template)
    logging.info("Zoning layers added to %s.", map_name)
    marijuana_adult_use_layers(map_group, template)
    logging.info("Marijuana and adult use layers added to %s.", map_name)
    agreements_layers(map_group, template)
    logging.info("Agreements and financial layers added to %s.", map_name)
    historic_cultural_layers(map_group, template)
    logging.info("Historic/cultural layers added to %s.", map_name)
    group_lyr["layers"].append(map_group)


def nhd_layers(group_lyr, template):
    """
    NHD watershed, rivers, streams and water bodies.

    :param group_lyr: Group layer definition target for layers.
    :return: Updates group layer definition with layers.
    :rtype: None
    """
    popup_names = t.layer_tags("nhd", u.nhd_urls, "_popup")
    label_names = t.layer_tags("nhd", u.nhd_urls, "_label")
    url_list = u.nhd_urls

    map_name = "Hydrography (NHD)"
    map_group = w.group_layer(map_name)
    for index, url in enumerate(url_list):
        map_lyr = MapServiceLayer(url)
        fc = w.feature_class(map_lyr, 0.5)
        fc.update({"visibility": False})
        # if fc["title"] == "Comprehensive Plan 2014":
        #     fc.update({"title": "Comprehensive Plan"})
        if popup_names[index] in template:
            fc.update({"popupInfo": template[popup_names[index]]})
        if label_names[index] in template:
            fc.update({"layerDefinition": template[label_names[index]]})
        logging.debug("Appending %s to %s layer.", fc["title"], map_name)
        map_group["layers"].append(fc)
    group_lyr["layers"].append(map_group)


def deq_drinking_water_source_layers(group_lyr, template):
    """
    DEQ drinking water source areas.

    :param group_lyr: Group layer definition target for layers.
    :return: Updates group layer definition with layers.
    :rtype: None
    """
    popup_names = t.layer_tags(
        "deq_dw_source", u.deq_drinking_water_source_urls, "_popup"
    )
    label_names = t.layer_tags(
        "deq_dw_source", u.deq_drinking_water_source_urls, "_label"
    )
    url_list = u.deq_drinking_water_source_urls

    map_name = "Drinking Water Source Areas (DEQ)"
    map_group = w.group_layer(map_name)
    for index, url in enumerate(url_list):
        map_lyr = MapServiceLayer(url)
        fc = w.feature_class(map_lyr, 0.5)
        fc.update({"visibility": False})
        if popup_names[index] in template:
            fc.update({"popupInfo": template[popup_names[index]]})
        if label_names[index] in template:
            fc.update({"layerDefinition": template[label_names[index]]})
        logging.debug("Appending %s to %s layer.", fc["title"], map_name)
        map_group["layers"].append(fc)
    group_lyr["layers"].append(map_group)


def deq_hydro_layers(group_lyr, template):
    """
    Impaired surface water layer from DEQ.

    :param group_lyr: Group layer definition target for layers.
    :return: Updates group layer definition with layers.
    :rtype: None
    """
    popup_names = t.layer_tags("deq_hydro_2022", u.deq_hydro_2022_urls, "_popup")
    label_names = t.layer_tags("deq_hydro_2022", u.deq_hydro_2022_urls, "_label")
    url_list = u.deq_hydro_2022_urls

    map_name = "Impaired Surface Waters (DEQ)"
    map_group = w.group_layer(map_name)
    for index, url in enumerate(url_list):
        map_lyr = MapServiceLayer(url)
        fc = w.feature_class(map_lyr, 0.5)
        fc.update({"visibility": False})
        if popup_names[index] in template:
            fc.update({"popupInfo": template[popup_names[index]]})
        if label_names[index] in template:
            fc.update({"layerDefinition": template[label_names[index]]})
        logging.debug("Appending %s to %s layer.", fc["title"], map_name)
        map_group["layers"].append(fc)
    group_lyr["layers"].append(map_group)


def deq_drinking_water_protection_layers(group_lyr, template):
    """
    DEQ drinking water potential contaminant sources (PCS).

    :param group_lyr: Group layer definition target for layers.
    :return: Updates group layer definition with layers.
    :rtype: None
    """
    popup_names = t.layer_tags(
        "deq_dw_pcs", u.deq_drinking_water_protection_urls, "_popup"
    )
    label_names = t.layer_tags(
        "deq_dw_pcs", u.deq_drinking_water_protection_urls, "_label"
    )
    url_list = u.deq_drinking_water_protection_urls

    map_name = "Drinking Water Potential Contaminant Sources (DEQ)"
    map_group = w.group_layer(map_name)
    sub_group = w.group_layer("Surface Water Potential Contaminant Sources")
    for index, url in enumerate(url_list):
        map_lyr = MapServiceLayer(url)
        fc = w.feature_class(map_lyr, 0.5)
        fc.update({"visibility": False})
        if popup_names[index] in template:
            fc.update({"popupInfo": template[popup_names[index]]})
        if label_names[index] in template:
            fc.update({"layerDefinition": template[label_names[index]]})
        logging.debug("Appending %s to %s layer.", fc["title"], map_name)
        if index in list(range(0, 9)):
            sub_group["layers"].append(fc)
        else:
            map_group["layers"].append(fc)
    map_group["layers"].insert(0, sub_group)
    group_lyr["layers"].append(map_group)


def dsl_esh_layers(group_lyr, template):
    """
    Essential salmon habitat from DSL.

    :param group_lyr: Group layer definition target for layers.
    :return: Updates group layer definition with layers.
    :rtype: None
    """
    popup_names = t.layer_tags("dsl_esh", u.dsl_esh_urls, "_popup")
    label_names = t.layer_tags("dsl_esh", u.dsl_esh_urls, "_label")
    url_list = u.dsl_esh_urls

    map_name = "Essential Salmon Habitat (DSL)"
    map_group = w.group_layer(map_name)
    for index, url in enumerate(url_list):
        map_lyr = MapServiceLayer(url)
        fc = w.feature_class(map_lyr, 0.5)
        fc.update({"visibility": False})
        if fc["title"] == "CutThroatCoastal":
            fc.update({"title": "Cut Throat Coastal"})
        if fc["title"] == "ChinookFall":
            fc.update({"title": "Chinook - Fall"})
        if fc["title"] == "ChinookSpring":
            fc.update({"title": "Chinook - Spring"})
        if fc["title"] == "SteelheadWinter":
            fc.update({"title": "Steelhead - Winter"})
        if fc["title"] == "SteelheadSummer":
            fc.update({"title": "Steelhead - Summer"})
        if fc["title"] == "Esh2022":
            fc.update({"title": "Essential Salmon Habitat 2022"})
        if popup_names[index] in template:
            fc.update({"popupInfo": template[popup_names[index]]})
        if label_names[index] in template:
            fc.update({"layerDefinition": template[label_names[index]]})
        logging.debug("Appending %s to %s layer.", fc["title"], map_name)
        map_group["layers"].append(fc)
    group_lyr["layers"].append(map_group)


def environment_layers(group_lyr, template):
    """
    Environmental features and hazards for the City of Grants Pass.

    :param group_lyr: Group layer definition target for layers.
    :return: Updates group layer definition with layers.
    :rtype: None
    """

    map_name = "Environment"
    map_group = w.group_layer(map_name)

    features = w.group_layer("Features")
    lidar_layers(features)
    logging.info("LiDAR layers added to %s.", map_name)
    nhd_layers(features, template)
    logging.info("Hydrography (NHD) layers added to %s.", map_name)
    dsl_esh_layers(features, template)
    logging.info("Essential salmon habitat (DSL) added to %s.", map_name)
    deq_drinking_water_source_layers(features, template)
    logging.info("Drinking water source areas (DEQ) added to %s.", map_name)

    hazards = w.group_layer("Hazards")
    wildfire_layers(hazards)
    logging.info("Wildfire potential (FS) layers added to %s.", map_name)
    deq_hydro_layers(hazards, template)
    logging.info("Impaired surface waters (DEQ) added to %s.", map_name)
    fema_nfhl_layers(hazards, template)
    logging.info("FEMA flood (NFHL) added to %s.", map_name)

    map_group["layers"].append(features)
    map_group["layers"].append(hazards)
    group_lyr["layers"].append(map_group)


def city_basemap(project_map, template):
    """
    Add common reference layers to web map.

    :param project_map: Web map to update with reference layers.
    :return: Updates the web map, adding reference layers.
    :rtype: None.
    """
    map_name = "city basemap"
    logging.info("Building %s.", map_name)
    basemap = w.group_layer("City of Grants Pass Layers")
    aerial_imagery(basemap)
    logging.info("Aerial imagery added to %s.", map_name)
    environment_layers(basemap, template)
    logging.info("Environment layers added to %s.", map_name)
    planning_layers(basemap, template)
    logging.info("Planning layers added to %s.", map_name)
    land_use_layers(basemap, template)
    logging.info("Land use layers added to %s.", map_name)
    boundaries(basemap, template)
    logging.info("Regulatory boundaries added to %s.", map_name)
    map_def = project_map.get_data()
    logging.info("Appending layers to %s definition.", map_name)
    map_def["operationalLayers"].append(basemap)
    project_map.update({"text": str(map_def)})
