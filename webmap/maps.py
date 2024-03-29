from webmap import webmap as w
from webmap import urls as u
from webmap import template as t
from webmap import search as s
from webmap.groups import boundaries as b
from webmap.groups import planning as pl
from webmap.groups import property as p
from webmap.groups import transportation as tr
from webmap.groups import utilities as ut
from webmap.groups import environment as e
import webmap.groups
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


def boundary_layers(base, template, basemap=False):
    """
    Regulatory boundaries for the City of Grants Pass.

    :param group_lyr: Group layer definition or project map target for layers.
    :param template: Reference template for map layers.
    :param basemap: Indicates whether appending to group layer or project map.
    :type basemap: Boolean
    :return: Updates group layer definition with layers.
    :rtype: None
    """
    popup_names = t.layer_tags("city_boundaries", u.boundaries_urls, "_popup")
    label_names = t.layer_tags("city_boundaries", u.boundaries_urls, "_label")
    url_list = u.boundaries_urls

    map_name = "Boundaries"
    map_group = w.group_layer(map_name)
    aiannha_layers(map_group, template)
    logging.info("AIANNHA layers added to %s.", map_name)
    bia_layers(map_group, template)
    logging.info("BIA layers added to %s.", map_name)
    school_layers(map_group, template)
    logging.info("Adding school district boundaries to %s.", map_name)
    for index, url in enumerate(url_list):
        map_lyr = MapServiceLayer(url)
        fc = w.feature_class(map_lyr, 0.5)
        fc.update({"visibility": False})
        if fc["title"] == "City Limits 2023":
            fc.update({"title": "City Limits"})
            fc.update({"visibility": True})
            fc.update({"opacity": 0.9})
        if fc["title"] == "UGB 2014":
            fc.update({"title": "Urban Growth Boundary"})
            fc.update({"visibility": True})
            fc.update({"opacity": 0.75})
        if fc["title"] == "Urban Reserve 2014":
            fc.update({"title": "Urban Reserve"})
        if fc["title"] == "GP_NSWE_Town_Sections":
            fc.update({"title": "Town Section Quadrants"})
        if fc["title"] == "CMAQ Boundary (2007 UGB)":
            fc.update({"title": "CMAQ Boundary"})
        if fc["title"] == "JoCo_Boundary":
            fc.update({"title": "Josephine County Line"})
        if fc["title"] == "LibraryDistrictArea_Dissolve":
            fc.update({"title": "Library District"})
        if popup_names[index] in template:
            fc.update({"popupInfo": template[popup_names[index]]})
        if label_names[index] in template:
            fc.update({"layerDefinition": template[label_names[index]]})
        map_group["layers"].append(fc)
    map_group["layers"].insert(2, u.library_def)
    plss_layers(map_group, template)
    logging.info("PLSS layers added to %s.", map_name)
    logging.info("Appending layers to %s definition.", map_name)
    w.add_group(base, map_group, basemap)


def school_layers(base, template, basemap=False):
    """
    Grants Pass District 7 and Three Rivers School District boundaries.

    :param base: Group layer definition or map project target for layers.
    :param template: Reference template for map layers.
    :param basemap: Indicates whether appending to group layer or project map.
    :type basemap: Boolean
    :return: Updates group layer definition with layers.
    :rtype: None
    """
    popup_names = t.layer_tags("schools", u.school_districts_urls, "_popup")
    label_names = t.layer_tags("schools", u.school_districts_urls, "_label")
    url_list = u.school_districts_urls

    map_name = "School Districts"
    map_group = w.group_layer(map_name)
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
        map_group["layers"].append(fc)
    logging.info("Appending layers to %s definition.", map_name)
    w.add_group(base, map_group, basemap)


def aerial_imagery(base, basemap=False):
    """
    Append aerial imagery layers to group layer.

    :param base: Group layer definition or map project target for layers.
    :param template: Reference template for map layers.
    :param basemap: Indicates whether appending to group layer or project map.
    :type basemap: Boolean
    :return: Updates group layer definition with layers.
    :rtype: None
    """
    group_name = "Aerial Imagery"
    map_group = w.group_layer(group_name)
    map_group["layers"].append(u.aerials_1938_def)
    map_group["layers"].append(u.aerials_1952_def)
    map_group["layers"].append(u.aerials_1975_def)
    map_group["layers"].append(u.aerials_1998_def)
    map_group["layers"].append(u.aerials_2001_def)
    map_group["layers"].append(u.aerials_2004_def)
    map_group["layers"].append(u.aerials_2007_def)
    map_group["layers"].append(u.aerials_2011_def)
    map_group["layers"].append(u.aerials_2015_def)
    map_group["layers"].append(u.aerials_2017_def)
    map_group["layers"].append(u.aerials_2019_ndvi_def)
    map_group["layers"].append(u.aerials_2019_def)
    map_group["layers"].append(u.esri_image_def)
    map_group["layers"].append(u.aerials_2023_def)
    logging.info("Appending layers to %s definition.", group_name)
    w.add_group(base, map_group, basemap)


def tax_layers(base, template, basemap=False):
    """
    Tax parcel layers, county and city versions.

    :param base: Group layer definition or map project target for layers.
    :param template: Reference template for map layers.
    :param basemap: Indicates whether appending to group layer or project map.
    :type basemap: Boolean
    :return: Updates group layer definition with layers.
    :rtype: None
    """
    popup_names = t.layer_tags("tax_parcels", u.tax_parcel_urls, "_popup")
    label_names = t.layer_tags("tax_parcels", u.tax_parcel_urls, "_label")
    url_list = u.tax_parcel_urls

    group_name = "Tax Parcels"
    map_group = w.group_layer(group_name)
    for index, url in enumerate(url_list):
        map_lyr = MapServiceLayer(url)
        fc = w.feature_class(map_lyr, 0.2)
        fc.update({"visibility": False})
        if fc["title"] == "Tax Parcels":
            fc.update({"title": "Taxlots (City)"})
            fc.update({"opacity": 0.75})
        if fc["title"] == "Assessor Taxlots":
            fc.update({"title": "Taxlots (County)"})
            fc.update({"opacity": 0.75})
        if fc["title"] == "Tax Codes":
            fc.update({"opacity": 0.2})
        if popup_names[index] in template:
            fc.update({"popupInfo": template[popup_names[index]]})
        if label_names[index] in template:
            fc.update({"layerDefinition": template[label_names[index]]})
        map_group["layers"].append(fc)
    logging.info("Appending layers to %s definition.", group_name)
    w.add_group(base, map_group, basemap)


def land_use_layers(base, template, internal, basemap=False, urls=u.land_use_urls):
    """
    Land use planning layers for the City of Grants Pass.

    :param base: Group layer definition or map project target for layers.
    :param template: Reference template for map layers.
    :param internal: Portal connection for internal access layers.
    :type internal: ArcGIS GIS connection.
    :param basemap: Indicates whether appending to group layer or project map.
    :type basemap: Boolean
    :param urls: Url list for published service.
    :type urls: List(String)
    :return: Updates group layer definition with layers.
    :rtype: None
    """
    popup_names = t.layer_tags("land_use", urls, "_popup")
    label_names = t.layer_tags("land_use", urls, "_label")

    group_name = "Land Use"
    map_group = w.group_layer(group_name)
    tax_layers(map_group, template)
    edit = False
    if urls == u.land_use_editing_urls:
        edit = True
    for index, url in enumerate(urls):
        if edit:
            map_lyr = MapServiceLayer(url, internal)
        else:
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
        logging.debug("Appending %s to %s layer.", fc["title"], group_name)
    logging.info("Appending layers to %s definition.", group_name)
    w.add_group(base, map_group, basemap)


def lidar_layers(base, basemap=False):
    """
    Lidar terrain and surface models from DOGAMI.

    :param base: Group layer definition or map project target for layers.
    :param basemap: Indicates whether appending to group layer or project map.
    :type basemap: Boolean
    :return: Updates group layer definition with layers.
    :rtype: None
    """
    group_name = "LiDAR Imagery"
    map_group = w.group_layer(group_name)
    map_group["layers"].append(u.dogami_be_def)
    map_group["layers"].append(u.dogami_hh_def)
    logging.info("Appending layers to %s definition.", group_name)
    w.add_group(base, map_group, basemap)


def wildfire_layers(base, basemap=False):
    """
    Wildfire (FS) national map services.

    :param base: Group layer definition or map project target for layers.
    :param basemap: Indicates whether appending to group layer or project map.
    :type basemap: Boolean
    :return: Updates group layer definition with layers.
    :rtype: None
    """
    group_name = "Wildfire"
    map_group = w.group_layer(group_name)
    map_group["layers"].append(u.fs_wildfire_potential_def)
    map_group["layers"].append(u.fs_wildfire_housing_def)
    logging.info("Appending layers to %s definition.", group_name)
    w.add_group(base, map_group, basemap)


# def fema_flood_layers(group_lyr, template):
#     """
#     NFHL flood layers from FEMA.
#
#     :param group_lyr: Group layer definition target for layers.
#     :return: Updates group layer definition with layers.
#     :rtype: None
#     """
#     popup_names = t.layer_tags("fema_flood", u.fema_flood_urls, "_popup")
#     label_names = t.layer_tags("fema_flood", u.fema_flood_urls, "_label")
#     url_list = u.fema_flood_urls
#
#     map_name = "FEMA Flood (NFHL)"
#     map_group = w.group_layer(map_name)
#     for index, url in enumerate(url_list):
#         map_lyr = MapServiceLayer(url)
#         fc = w.feature_class(map_lyr, 0.5)
#         fc.update({"visibility": False})
#         if popup_names[index] in template:
#             fc.update({"popupInfo": template[popup_names[index]]})
#         if label_names[index] in template:
#             fc.update({"layerDefinition": template[label_names[index]]})
#         logging.info("Appending %s to %s layer.", fc["title"], map_name)
#         map_group["layers"].append(fc)
#     group_lyr["layers"].append(map_group)


def fema_nfhl_layers(base, template, basemap=False):
    """
    NFHL flood layers from FEMA.

    :param base: Group layer definition or map project target for layers.
    :param template: Reference template for map layers.
    :param basemap: Indicates whether appending to group layer or project map.
    :type basemap: Boolean
    :return: Updates group layer definition with layers.
    :rtype: None
    """
    popup_names = t.layer_tags("fema_flood", u.fema_flood_urls, "_popup")
    label_names = t.layer_tags("fema_flood", u.fema_flood_urls, "_label")
    url_list = u.fema_nfhl_wms_urls

    group_name = "FEMA Flood (NFHL)"
    map_group = w.group_layer(group_name)
    for index, url in enumerate(url_list):
        map_lyr = MapServiceLayer(url)
        fc = w.feature_class(map_lyr, 0.5)
        fc.update({"visibility": False})
        if popup_names[index] in template:
            fc.update({"popupInfo": template[popup_names[index]]})
        if label_names[index] in template:
            fc.update({"layerDefinition": template[label_names[index]]})
        logging.info("Appending %s to %s layer.", fc["title"], group_name)
        map_group["layers"].append(fc)
    logging.info("Appending layers to %s definition.", group_name)
    w.add_group(base, map_group, basemap)


def historic_cultural_layers(base, template, basemap=False):
    """
    Historic district, sites and culturally significant sites in the City of Grants Pass.

    :param base: Group layer definition or map project target for layers.
    :param template: Reference template for map layers.
    :param basemap: Indicates whether appending to group layer or project map.
    :type basemap: Boolean
    :return: Updates group layer definition with layers.
    :rtype: None
    """
    popup_names = t.layer_tags("historic", u.historic_cultural_areas_urls, "_popup")
    label_names = t.layer_tags("historic", u.historic_cultural_areas_urls, "_label")
    url_list = u.historic_cultural_areas_urls

    group_name = "Historic/Cultural Areas"
    map_group = w.group_layer(group_name)
    for index, url in enumerate(url_list):
        map_lyr = MapServiceLayer(url)
        fc = w.feature_class(map_lyr, 0.5)
        fc.update({"visibility": False})
        if popup_names[index] in template:
            fc.update({"popupInfo": template[popup_names[index]]})
        if label_names[index] in template:
            fc.update({"layerDefinition": template[label_names[index]]})
        logging.debug("Appending %s to %s layer.", fc["title"], group_name)
        map_group["layers"].append(fc)
    fc = u.oprd_historic_sites_def
    if "oprd_popup" in template:
        fc.update({"popupInfo": template["oprd_popup"]})
    if "oprd_label" in template:
        fc.update({"layerDefinition": template["oprd_label"]})
    map_group["layers"].insert(2, fc)
    logging.info("Appending layers to %s definition.", group_name)
    w.add_group(base, map_group, basemap)


def historic_cultural_tourism(base, template, basemap=False):
    """
    Historic district, sites and culturally significant sites in the City of Grants Pass.

    :param base: Group layer definition or map project target for layers.
    :param template: Reference template for map layers.
    :param basemap: Indicates whether appending to group layer or project map.
    :type basemap: Boolean
    :return: Updates group layer definition with layers.
    :rtype: None
    """
    url_list = u.historic_cultural_tourism_urls
    popup_names = t.layer_tags("tourism_historic", url_list, "_popup")
    label_names = t.layer_tags("tourism_historic", url_list, "_label")

    group_name = "Historic/Cultural Tourism"
    map_group = w.group_layer(group_name)
    for index, url in enumerate(url_list):
        map_lyr = MapServiceLayer(url)
        fc = w.feature_class(map_lyr, 0.5)
        fc.update({"visibility": False})
        if popup_names[index] in template:
            fc.update({"popupInfo": template[popup_names[index]]})
        if label_names[index] in template:
            fc.update({"layerDefinition": template[label_names[index]]})
        logging.debug("Appending %s to %s layer.", fc["title"], group_name)
        map_group["layers"].append(fc)
    fc = u.oprd_historic_sites_def
    if "oprd_popup" in template:
        fc.update({"popupInfo": template["oprd_popup"]})
    if "oprd_label" in template:
        fc.update({"layerDefinition": template["oprd_label"]})
    map_group["layers"].insert(1, fc)
    logging.info("Appending layers to %s definition.", group_name)
    w.add_group(base, map_group, basemap)


def zoning_layers(base, template, basemap=False):
    """
    Zoning, comprehensive plan and overlays for City of Grants Pass.

    :param base: Group layer definition or map project target for layers.
    :param template: Reference template for map layers.
    :param basemap: Indicates whether appending to group layer or project map.
    :type basemap: Boolean
    :return: Updates group layer definition with layers.
    :rtype: None
    """
    popup_names = t.layer_tags("zoning", u.zoning_urls, "_popup")
    label_names = t.layer_tags("zoning", u.zoning_urls, "_label")
    url_list = u.zoning_urls

    group_name = "Zoning Group"
    map_group = w.group_layer(group_name)
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
        logging.debug("Appending %s to %s layer.", fc["title"], group_name)
        map_group["layers"].append(fc)
    logging.info("Appending layers to %s definition.", group_name)
    w.add_group(base, map_group, basemap)


def marijuana_adult_use_layers(base, template, basemap=False):
    """
    Locations and buffers for marijuana and adult use planning at the City of Grants Pass.

    :param base: Group layer definition or map project target for layers.
    :param template: Reference template for map layers.
    :param basemap: Indicates whether appending to group layer or project map.
    :type basemap: Boolean
    :return: Updates group layer definition with layers.
    :rtype: None
    """
    popup_names = t.layer_tags("marijuana_adult_use", u.marijuana_adult_urls, "_popup")
    label_names = t.layer_tags("marijuana_adult_use", u.marijuana_adult_urls, "_label")
    url_list = u.marijuana_adult_urls

    group_name = "Marijuana and Adult Use"
    map_group = w.group_layer(group_name)
    for index, url in enumerate(url_list):
        map_lyr = MapServiceLayer(url)
        fc = w.feature_class(map_lyr, 0.5)
        fc.update({"visibility": False})
        if popup_names[index] in template:
            fc.update({"popupInfo": template[popup_names[index]]})
        if label_names[index] in template:
            fc.update({"layerDefinition": template[label_names[index]]})
        logging.debug("Appending %s to %s layer.", fc["title"], group_name)
        map_group["layers"].append(fc)
    logging.info("Appending layers to %s definition.", group_name)
    w.add_group(base, map_group, basemap)


def marijuana_permitting_layers(base, template, basemap=False):
    """
    Locations and buffers for marijuana business permitting at the City of Grants Pass.

    :param base: Group layer definition or map project target for layers.
    :param template: Reference template for map layers.
    :param basemap: Indicates whether appending to group layer or project map.
    :type basemap: Boolean
    :return: Updates group layer definition with layers.
    :rtype: None
    """
    url_list = u.marijuana_permitting_urls
    popup_names = t.layer_tags("marijuana_permitting", url_list, "_popup")
    label_names = t.layer_tags("marijuana_permitting", url_list, "_label")

    group_name = "Marijuana Business Permitting"
    map_group = w.group_layer(group_name)
    buffers = w.group_layer("Location Buffer Restrictions")
    permissible = w.group_layer("Potentially Permissible Areas")
    for index, url in enumerate(url_list):
        map_lyr = MapServiceLayer(url)
        fc = w.feature_class(map_lyr, 0.5)
        fc.update({"visibility": False})
        if popup_names[index] in template:
            fc.update({"popupInfo": template[popup_names[index]]})
        if label_names[index] in template:
            fc.update({"layerDefinition": template[label_names[index]]})
        logging.debug("Appending %s to %s layer.", fc["title"], group_name)
        if index <= 16:
            buffers["layers"].append(fc)
        else:
            permissible["layers"].append(fc)
    map_group["layers"].append(buffers)
    map_group["layers"].append(permissible)
    logging.info("Appending layers to %s definition.", group_name)
    w.add_group(base, map_group, basemap)


def agreements_layers(base, template, basemap=False):
    """
    Financial and planning agreements with the City of Grants Pass.

    :param base: Group layer definition or map project target for layers.
    :param template: Reference template for map layers.
    :param basemap: Indicates whether appending to group layer or project map.
    :type basemap: Boolean
    :return: Updates group layer definition with layers.
    :rtype: None
    """
    popup_names = t.layer_tags("agreements", u.agreements_urls, "_popup")
    label_names = t.layer_tags("agreements", u.agreements_urls, "_label")
    url_list = u.agreements_urls

    group_name = "Agreements and Financial"
    map_group = w.group_layer(group_name)
    for index, url in enumerate(url_list):
        map_lyr = MapServiceLayer(url)
        fc = w.feature_class(map_lyr, 0.5)
        fc.update({"visibility": False})
        if popup_names[index] in template:
            fc.update({"popupInfo": template[popup_names[index]]})
        if label_names[index] in template:
            fc.update({"layerDefinition": template[label_names[index]]})
        logging.debug("Appending %s to %s layer.", fc["title"], group_name)
        map_group["layers"].append(fc)
    logging.info("Appending layers to %s definition.", group_name)
    w.add_group(base, map_group, basemap)


def as_builts_layers(base, template, basemap=False):
    """
    As builts for the City of Grants Pass, Oregon.

    :param base: Group layer definition or map project target for layers.
    :param template: Reference template for map layers.
    :param basemap: Indicates whether appending to group layer or project map.
    :type basemap: Boolean
    :return: Updates group layer definition with layers.
    :rtype: None
    """
    popup_names = t.layer_tags("as_builts", u.as_builts_urls, "_popup")
    label_names = t.layer_tags("as_builts", u.as_builts_urls, "_label")
    url_list = u.as_builts_urls

    group_name = "As Builts"
    map_group = w.group_layer(group_name)
    for index, url in enumerate(url_list):
        map_lyr = MapServiceLayer(url)
        fc = w.feature_class(map_lyr, 0.5)
        fc.update({"visibility": False})
        if popup_names[index] in template:
            fc.update({"popupInfo": template[popup_names[index]]})
        if label_names[index] in template:
            fc.update({"layerDefinition": template[label_names[index]]})
        logging.debug("Appending %s to %s layer.", fc["title"], group_name)
        map_group["layers"].append(fc)
    logging.info("Appending layers to %s definition.", group_name)
    w.add_group(base, map_group, basemap)


def planning_layers(base, template, basemap=False):
    """
    Zoning, historic/cultural areas and miscellaneous planning layers for City of Grants Pass.

    :param base: Group layer definition or map project target for layers.
    :param template: Reference template for map layers.
    :param basemap: Indicates whether appending to group layer or project map.
    :type basemap: Boolean
    :return: Updates group layer definition with layers.
    :rtype: None
    """
    popup_names = t.layer_tags("planning", u.planning_urls, "_popup")
    label_names = t.layer_tags("planning", u.planning_urls, "_label")
    url_list = u.planning_urls

    group_name = "Planning"
    map_group = w.group_layer(group_name)
    conservation = "Lawnridge-Washington Conservation District"
    conservation_group = w.group_layer(conservation)
    as_builts_layers(map_group, template)
    logging.info("As builts added to %s.", group_name)
    for index, url in enumerate(url_list):
        map_lyr = MapServiceLayer(url)
        fc = w.feature_class(map_lyr, 0.5)
        fc.update({"visibility": False})
        if popup_names[index] in template:
            fc.update({"popupInfo": template[popup_names[index]]})
        if label_names[index] in template:
            fc.update({"layerDefinition": template[label_names[index]]})
        logging.debug("Appending %s to %s layer.", fc["title"], group_name)
        if index in [4, 5]:
            if fc["title"] == "Proposed Conservation District":
                fc.update(
                    {"title": "Lawnridge-Washington Conservation District Boundary"}
                )
            conservation_group["layers"].append(fc)
        else:
            map_group["layers"].append(fc)
    map_group["layers"].append(conservation_group)
    zoning_layers(map_group, template)
    logging.info("Zoning layers added to %s.", group_name)
    marijuana_adult_use_layers(map_group, template)
    logging.info("Marijuana and adult use layers added to %s.", group_name)
    marijuana_permitting_layers(map_group, template)
    logging.info("Marijuana business permitting layers added to %s.", group_name)
    agreements_layers(map_group, template)
    logging.info("Agreements and financial layers added to %s.", group_name)
    historic_cultural_layers(map_group, template)
    logging.info("Historic/cultural layers added to %s.", group_name)
    logging.info("Appending layers to %s definition.", group_name)
    w.add_group(base, map_group, basemap)


def nhd_layers(base, template, basemap=False, urls=u.nhd_urls):
    """
    NHD watershed, rivers, streams and water bodies.

    :param base: Group layer definition or map project target for layers.
    :param template: Reference template for map layers.
    :param basemap: Indicates whether appending to group layer or project map.
    :type basemap: Boolean
    :param urls: Url list for published service.
    :type urls: List(String)
    :return: Updates group layer definition with layers.
    :rtype: None
    """
    popup_names = t.layer_tags("nhd", urls, "_popup")
    label_names = t.layer_tags("nhd", urls, "_label")

    group_name = "Hydrography (NHD)"
    map_group = w.group_layer(group_name)
    for index, url in enumerate(urls):
        map_lyr = MapServiceLayer(url)
        fc = w.feature_class(map_lyr, 0.5)
        fc.update({"visibility": False})
        if popup_names[index] in template:
            fc.update({"popupInfo": template[popup_names[index]]})
        if label_names[index] in template:
            fc.update({"layerDefinition": template[label_names[index]]})
        logging.debug("Appending %s to %s layer.", fc["title"], group_name)
        map_group["layers"].append(fc)
    logging.info("Appending layers to %s definition.", group_name)
    w.add_group(base, map_group, basemap)


def deq_drinking_water_source_layers(base, template, basemap=False):
    """
    DEQ drinking water source areas.

    :param base: Group layer definition or map project target for layers.
    :param template: Reference template for map layers.
    :param basemap: Indicates whether appending to group layer or project map.
    :type basemap: Boolean
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

    group_name = "Drinking Water Source Areas (DEQ)"
    map_group = w.group_layer(group_name)
    for index, url in enumerate(url_list):
        map_lyr = MapServiceLayer(url)
        fc = w.feature_class(map_lyr, 0.5)
        fc.update({"visibility": False})
        if popup_names[index] in template:
            fc.update({"popupInfo": template[popup_names[index]]})
        if label_names[index] in template:
            fc.update({"layerDefinition": template[label_names[index]]})
        logging.debug("Appending %s to %s layer.", fc["title"], group_name)
        map_group["layers"].append(fc)
    logging.info("Appending layers to %s definition.", group_name)
    # w.add_group(map_group, u.deq_gw_2yrtot_def, False)
    w.add_group(base, map_group, basemap)


def deq_hydro_layers(base, template, basemap=False):
    """
    Impaired surface water layer from DEQ.

    :param base: Group layer definition or map project target for layers.
    :param template: Reference template for map layers.
    :param basemap: Indicates whether appending to group layer or project map.
    :type basemap: Boolean
    :return: Updates group layer definition with layers.
    :rtype: None
    """
    popup_names = t.layer_tags("deq_hydro_2022", u.deq_hydro_2022_urls, "_popup")
    label_names = t.layer_tags("deq_hydro_2022", u.deq_hydro_2022_urls, "_label")
    url_list = u.deq_hydro_2022_urls

    group_name = "Impaired Surface Waters (DEQ)"
    map_group = w.group_layer(group_name)
    for index, url in enumerate(url_list):
        map_lyr = MapServiceLayer(url)
        fc = w.feature_class(map_lyr, 0.5)
        fc.update({"visibility": False})
        if popup_names[index] in template:
            fc.update({"popupInfo": template[popup_names[index]]})
        if label_names[index] in template:
            fc.update({"layerDefinition": template[label_names[index]]})
        logging.debug("Appending %s to %s layer.", fc["title"], group_name)
        map_group["layers"].append(fc)
    logging.info("Appending layers to %s definition.", group_name)
    w.add_group(base, map_group, basemap)


def deq_pcs_layers(base, template, basemap=False):
    """
    DEQ drinking water potential contaminant sources (PCS).

    :param base: Group layer definition or map project target for layers.
    :param template: Reference template for map layers.
    :param basemap: Indicates whether appending to group layer or project map.
    :type basemap: Boolean
    :return: Updates group layer definition with layers.
    :rtype: None
    """
    deq_pcs_def = u.deq_pcs_def
    if "deq_pcs_popup" in template:
        deq_pcs_def.update({"popupInfo": template["deq_pcs_popup"]})
    if "deq_pcs_label" in template:
        deq_pcs_def.update({"layerDefinition": template["deq_pcs_label"]})
    w.add_group(base, deq_pcs_def, basemap)


def dsl_esh_layers(base, template, basemap=False):
    """
    Essential salmon habitat from DSL.

    :param base: Group layer definition or map project target for layers.
    :param template: Reference template for map layers.
    :param basemap: Indicates whether appending to group layer or project map.
    :type basemap: Boolean
    :return: Updates group layer definition with layers.
    :rtype: None
    """
    popup_names = t.layer_tags("dsl_esh", u.dsl_esh_urls, "_popup")
    label_names = t.layer_tags("dsl_esh", u.dsl_esh_urls, "_label")
    url_list = u.dsl_esh_urls

    group_name = "Essential Salmon Habitat (DSL)"
    map_group = w.group_layer(group_name)
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
        logging.debug("Appending %s to %s layer.", fc["title"], group_name)
        map_group["layers"].append(fc)
    logging.info("Appending layers to %s definition.", group_name)
    w.add_group(base, map_group, basemap)


def dsl_wetland_layers(base, template, basemap=False):
    """
    National Wetland Inventory service from Oregon DSL.

    :param base: Group layer definition or map project target for layers.
    :param template: Reference template for map layers.
    :param basemap: Indicates whether appending to group layer or project map.
    :type basemap: Boolean
    :return: Updates group layer definition with layers.
    :rtype: None
    """
    popup_names = t.layer_tags("dsl_wetland", u.dsl_wetlands_url, "_popup")
    label_names = t.layer_tags("dsl_wetland", u.dsl_wetlands_url, "_label")
    url_list = u.dsl_wetlands_url

    group_name = "Wetlands (DSL)"
    map_group = w.group_layer(group_name)
    for index, url in enumerate(url_list):
        map_lyr = MapServiceLayer(url)
        fc = w.feature_class(map_lyr, 0.5)
        fc.update({"visibility": False})
        # if fc["title"] == "Esh2022":
        #     fc.update({"title": "Essential Salmon Habitat 2022"})
        if popup_names[index] in template:
            fc.update({"popupInfo": template[popup_names[index]]})
        if label_names[index] in template:
            fc.update({"layerDefinition": template[label_names[index]]})
        logging.debug("Appending %s to %s layer.", fc["title"], group_name)
        map_group["layers"].append(fc)
    logging.info("Appending layers to %s definition.", group_name)
    w.add_group(base, map_group, basemap)


def soils_layers(base, template, basemap=False):
    """
    Soil classification layers from NRCS.

    :param base: Group layer definition or map project target for layers.
    :param template: Reference template for map layers.
    :param basemap: Indicates whether appending to group layer or project map.
    :type basemap: Boolean
    :return: Updates group layer definition with layers.
    :rtype: None
    """
    group_name = "Soils"
    map_group = w.group_layer(group_name)
    w.add_single_layer(
        "hydric_soils",
        u.dsl_hydric_soils_url,
        map_group,
        template,
        title="Hydric Soils (DSL)",
        visibility=False,
    )
    logging.info("Hydric soils added to %s.", group_name)

    nrcs_soils_def = u.nrcs_soils_def
    if "soils_popup" in template:
        nrcs_soils_def.update({"popupInfo": template["soils_popup"]})
    if "soils_label" in template:
        nrcs_soils_def.update({"layerDefinition": template["soils_label"]})
    map_group["layers"].append(nrcs_soils_def)
    logging.info("Soils added to %s.", group_name)
    logging.info("Appending layers to %s definition.", group_name)
    w.add_group(base, map_group, basemap)


# def nwi_wetland_layers(group_lyr, template):
#     """
#     National Wetland Inventory service from USFWS.
#
#     :param group_lyr: Group layer definition target for layers.
#     :return: Updates group layer definition with layers.
#     :rtype: None
#     """
#     popup_names = t.layer_tags("nwi_wetland", u.fw_nwi_wetlands, "_popup")
#     label_names = t.layer_tags("nwi_wetland", u.fw_nwi_wetlands, "_label")
#     url_list = u.fw_nwi_wetlands
#
#     map_name = "Wetlands (USFWS)"
#     map_group = w.group_layer(map_name)
#     for index, url in enumerate(url_list):
#         map_lyr = MapServiceLayer(url)
#         fc = w.feature_class(map_lyr, 0.5)
#         fc.update({"visibility": False})
#         # if fc["title"] == "Esh2022":
#         #     fc.update({"title": "Essential Salmon Habitat 2022"})
#         if popup_names[index] in template:
#             fc.update({"popupInfo": template[popup_names[index]]})
#         if label_names[index] in template:
#             fc.update({"layerDefinition": template[label_names[index]]})
#         logging.debug("Appending %s to %s layer.", fc["title"], map_name)
#         map_group["layers"].append(fc)
#     group_lyr["layers"].append(map_group)


def hazards_layers(base, template, basemap=False):
    """
    Environmental hazards layers for the City of Grants Pass, Oregon.

    :param base: Group layer definition or map project target for layers.
    :param template: Reference template for map layers.
    :param basemap: Indicates whether appending to group layer or project map.
    :type basemap: Boolean
    :return: Updates group layer definition with layers.
    :rtype: None
    """
    popup_names = t.layer_tags("hazards", u.hazards_urls, "_popup")
    label_names = t.layer_tags("hazards", u.hazards_urls, "_label")
    url_list = u.hazards_urls

    group_name = "Hazards"
    map_group = w.group_layer(group_name)
    wildfire_layers(map_group)
    logging.info("Wildfire potential (FS) layers added to %s.", group_name)
    # deq_hydro_layers(map_group, template)
    logging.info("Impaired surface waters (DEQ) added to %s.", group_name)
    deq_pcs_layers(map_group, template)
    logging.info("Potential contamination sources (DEQ) added to %s.", group_name)
    fema_nfhl_layers(map_group, template)
    logging.info("FEMA flood (NFHL) added to %s.", group_name)
    for index, url in enumerate(url_list):
        map_lyr = MapServiceLayer(url)
        fc = w.feature_class(map_lyr, 0.5)
        fc.update({"visibility": False})
        if popup_names[index] in template:
            fc.update({"popupInfo": template[popup_names[index]]})
        if label_names[index] in template:
            fc.update({"layerDefinition": template[label_names[index]]})
        logging.debug("Appending %s to %s layer.", fc["title"], group_name)
        map_group["layers"].append(fc)
    logging.info("Appending layers to %s definition.", group_name)
    w.add_group(base, map_group, basemap)


def parks_layers(base, template, basemap=False):
    """
    Parks and landscaped areas for the City of Grants Pass, Oregon.

    :param base: Group layer definition or map project target for layers.
    :param template: Reference template for map layers.
    :type template: JSON dictionary
    :param basemap: Indicates whether appending to group layer or project map.
    :type basemap: Boolean
    :return: Updates group layer definition with layers.
    :rtype: None
    """

    popup_names = t.layer_tags("parks", u.parks_urls, "_popup")
    label_names = t.layer_tags("parks", u.parks_urls, "_label")
    url_list = u.parks_urls

    group_name = "Parks"
    map_group = w.group_layer(group_name)
    for index, url in enumerate(url_list):
        map_lyr = MapServiceLayer(url)
        fc = w.feature_class(map_lyr, 0.5)
        fc.update({"visibility": False})
        if fc["title"] == "Parks":
            fc.update({"title": "Parks (City)"})
        if fc["title"] == "Landscaping Areas Maintained by Parks":
            fc.update({"title": "Landscape Maintained by City Parks"})
        if fc["title"] == "Parks_poly":
            fc.update({"title": "Parks (County)"})
        if popup_names[index] in template:
            fc.update({"popupInfo": template[popup_names[index]]})
        if label_names[index] in template:
            fc.update({"layerDefinition": template[label_names[index]]})
        logging.debug("Appending %s to %s layer.", fc["title"], group_name)
        map_group["layers"].append(fc)
    logging.info("Appending layers to %s definition.", group_name)
    w.add_group(base, map_group, basemap)


def parks_trails(base, template, basemap=False):
    """
    Parks and trails for the City of Grants Pass, Oregon.

    :param base: Group layer definition or map project target for layers.
    :param template: Reference template for map layers.
    :type template: JSON dictionary
    :param basemap: Indicates whether appending to group layer or project map.
    :type basemap: Boolean
    :return: Updates group layer definition with layers.
    :rtype: None
    """

    url_list = u.tourism_parks_urls
    popup_names = t.layer_tags("tourism_parks", url_list, "_popup")
    label_names = t.layer_tags("tourism_parks", url_list, "_label")

    group_name = "Parks & Trails"
    map_group = w.group_layer(group_name)
    for index, url in enumerate(url_list):
        map_lyr = MapServiceLayer(url)
        fc = w.feature_class(map_lyr, 0.5)
        fc.update({"visibility": False})
        if fc["title"] == "Parks":
            fc.update({"title": "Parks (City)"})
        if fc["title"] == "Parks_poly":
            fc.update({"title": "Parks (County)"})
        if popup_names[index] in template:
            fc.update({"popupInfo": template[popup_names[index]]})
        if label_names[index] in template:
            fc.update({"layerDefinition": template[label_names[index]]})
        logging.debug("Appending %s to %s layer.", fc["title"], group_name)
        map_group["layers"].append(fc)
    logging.info("Appending layers to %s definition.", group_name)
    w.add_group(base, map_group, basemap)


def contours_layers(base, template, basemap=False):
    """
    Topographic contours for the City of Grants Pass, Oregon.

    :param base: Group layer definition or map project target for layers.
    :param template: Reference template for map layers.
    :type template: JSON dictionary
    :param basemap: Indicates whether appending to group layer or project map.
    :type basemap: Boolean
    :return: Updates group layer definition with layers.
    :rtype: None
    """

    popup_names = t.layer_tags("contours", u.contours_urls, "_popup")
    label_names = t.layer_tags("contours", u.contours_urls, "_label")
    url_list = u.contours_urls

    group_name = "Topographic Contours"
    map_group = w.group_layer(group_name)
    group_2004 = w.group_layer("2004 Contours")
    group_2012 = w.group_layer("2012 Contours (DEM)")
    for index, url in enumerate(url_list):
        map_lyr = MapServiceLayer(url)
        fc = w.feature_class(map_lyr, 0.5)
        fc.update({"visibility": False})
        if popup_names[index] in template:
            fc.update({"popupInfo": template[popup_names[index]]})
        if label_names[index] in template:
            fc.update({"layerDefinition": template[label_names[index]]})
        logging.debug("Appending %s to %s layer.", fc["title"], group_name)
        if index >= 5:
            group_2012["layers"].append(fc)
        else:
            group_2004["layers"].append(fc)
    map_group["layers"].append(group_2004)
    map_group["layers"].append(group_2012)
    logging.info("Appending layers to %s definition.", group_name)
    w.add_group(base, map_group, basemap)


def features_layers(base, template, basemap=False):
    """
    Environmental features layers for the City of Grants Pass, Oregon.

    :param base: Group layer definition or map project target for layers.
    :param template: Reference template for map layers.
    :type template: JSON dictionary
    :param basemap: Indicates whether appending to group layer or project map.
    :type basemap: Boolean
    :return: Updates group layer definition with layers.
    :rtype: None
    """
    group_name = "Features"
    map_group = w.group_layer(group_name)
    lidar_layers(map_group)
    logging.info("LiDAR layers added to %s.", group_name)
    soils_layers(map_group, template)
    logging.info("Soils layers added to %s.", group_name)
    contours_layers(map_group, template)
    logging.info("Topographic contours added to %s.", group_name)
    parks_layers(map_group, template)
    logging.info("Parks layers added to %s.", group_name)
    nhd_layers(map_group, template)
    logging.info("Hydrography (NHD) layers added to %s.", group_name)
    w.add_single_layer(
        "wetlands",
        u.dsl_wetlands_url,
        map_group,
        template,
        title="Wetlands (DSL)",
        visibility=False,
    )
    logging.info("Wetland inventory (DSL) added to %s.", group_name)
    dsl_esh_layers(map_group, template)
    logging.info("Essential salmon habitat (DSL) added to %s.", group_name)
    deq_drinking_water_source_layers(map_group, template)
    logging.info("Drinking water source areas (DEQ) added to %s.", group_name)
    map_group["layers"].append(u.wells_def)
    logging.info("Wells layers (OWRD) added to %s.", group_name)
    w.add_single_layer(
        "features0",
        u.features_urls[1],
        map_group,
        template,
        title="20ft Stream Buffer",
        visibility=False,
    )
    logging.info("Stream buffer added to %s.", group_name)
    logging.info("Appending layers to %s definition.", group_name)
    w.add_group(base, map_group, basemap)


def environment_layers(base, template, basemap=False):
    """
    Environmental features and hazards for the City of Grants Pass.

    :param base: Group layer definition or map project target for layers.
    :param template: Reference template for map layers.
    :type template: JSON dictionary
    :param basemap: Indicates whether appending to group layer or project map.
    :type basemap: Boolean
    :return: Updates group layer definition with layers.
    :rtype: None
    """

    group_name = "Environment"
    map_group = w.group_layer(group_name)

    features_layers(map_group, template)
    logging.info("Environmental features added to %s.", group_name)
    hazards_layers(map_group, template)
    logging.info("Hazards layers added to %s.", group_name)
    logging.info("Appending layers to %s definition.", group_name)
    w.add_group(base, map_group, basemap)


def parking_layers(base, template, basemap=False):
    """
    Parking lots and spaces for downtown City of Grants Pass, Oregon.

    :param base: Group layer definition or map project target for layers.
    :param template: Reference template for map layers.
    :type template: JSON dictionary
    :param basemap: Indicates whether appending to group layer or project map.
    :type basemap: Boolean
    :return: Updates group layer definition with layers.
    :rtype: None
    """

    popup_names = t.layer_tags("parking", u.parking_urls, "_popup")
    label_names = t.layer_tags("parking", u.parking_urls, "_label")
    url_list = u.parking_urls

    group_name = "Parking"
    map_group = w.group_layer(group_name)
    for index, url in enumerate(url_list):
        map_lyr = MapServiceLayer(url)
        fc = w.feature_class(map_lyr, 0.5)
        fc.update({"visibility": False})
        if popup_names[index] in template:
            fc.update({"popupInfo": template[popup_names[index]]})
        if label_names[index] in template:
            fc.update({"layerDefinition": template[label_names[index]]})
        logging.debug("Appending %s to %s layer.", fc["title"], group_name)
        map_group["layers"].append(fc)
    logging.info("Appending layers to %s definition.", group_name)
    w.add_group(base, map_group, basemap)


def transportation_layers(
    base, template, internal, basemap=False, urls=u.transportation_urls
):
    """
    Transportation layers for the City of Grants Pass, Oregon.

    :param base: Group layer definition or map project target for layers.
    :param template: Reference template for map layers.
    :type template: JSON dictionary
    :param internal: Portal connection for internal access layers.
    :type internal: ArcGIS GIS connection.
    :param basemap: Indicates whether appending to group layer or project map.
    :type basemap: Boolean
    :param urls: Url list for published service.
    :type urls: List(String)
    :return: Updates group layer definition with layers.
    :rtype: None
    """
    popup_names = t.layer_tags("transportation", urls, "_popup")
    label_names = t.layer_tags("transportation", urls, "_label")

    group_name = "Transportation"
    map_group = w.group_layer(group_name)
    streets_group = w.group_layer("Streets")
    fixtures_group = w.group_layer("Fixtures")
    alt_group = w.group_layer("Bike | Walk | Ride")
    edit = False
    if urls == u.transportation_editing_urls:
        edit = True
    for index, url in enumerate(urls):
        if edit:
            map_lyr = MapServiceLayer(url, internal)
        else:
            map_lyr = MapServiceLayer(url)
        fc = w.feature_class(map_lyr, 0.5)
        fc.update({"visibility": False})
        if fc["title"] == "JCT Stops":
            fc.update({"title": "Bus Stops (JCT)"})
        if fc["title"] == "JCT Routes":
            fc.update({"title": "Bus Routes (JCT)"})
        if fc["title"] == "railroadsgb":
            fc.update({"title": "Railroad"})
        if fc["title"] == "TripCheck_Construction_Data_Upload":
            fc.update({"title": "Construction (ODOT)"})
        if fc["title"] == "TripCheck_Incidents_Data_Upload":
            fc.update({"title": "Traffic Incidents (ODOT)"})
        if index == 7:
            fc.update({"title": "Streets (ODOT)"})
        if index == 8:
            fc.update({"title": "Streets (County)"})
        if index == 9:
            fc.update({"title": "Streets by Jurisdiction"})
        if index == 10:
            fc.update({"title": "Streets by Classification"})
        if popup_names[index] in template:
            fc.update({"popupInfo": template[popup_names[index]]})
        if label_names[index] in template:
            fc.update({"layerDefinition": template[label_names[index]]})
        logging.debug("Appending %s to %s layer.", fc["title"], group_name)
        if index in list(range(3, 14)):
            streets_group["layers"].append(fc)
        elif index in list(range(14, 19)):
            alt_group["layers"].append(fc)
        elif index in list(range(19, 24)):
            fixtures_group["layers"].append(fc)
        else:
            map_group["layers"].append(fc)
    parking_layers(map_group, template)
    traffic_layers(map_group, template)
    logging.info("Traffic reports added to %s.", group_name)
    map_group["layers"].append(streets_group)
    logging.info("Streets added to %s.", group_name)
    map_group["layers"].append(alt_group)
    map_group["layers"].append(fixtures_group)
    logging.info("Appending layers to %s definition.", group_name)
    w.add_group(base, map_group, basemap)


def transportation_editing(base, template, internal, basemap=False):
    """
    Transportation editing layers for the City of Grants Pass, Oregon.

    :param base: Group layer definition or map project target for layers.
    :param template: Reference template for map layers.
    :type template: JSON dictionary
    :param internal: Portal connection for internal access layers.
    :type internal: ArcGIS GIS connection.
    :param basemap: Indicates whether appending to group layer or project map.
    :type basemap: Boolean
    :return: Updates group layer definition with layers.
    :rtype: None
    """
    url_list = u.transportation_editing
    popup_names = t.layer_tags("transportation_editing", url_list, "_popup")
    label_names = t.layer_tags("transportation_editing", url_list, "_label")

    group_name = "Transportation Editing"
    map_group = w.group_layer(group_name)
    streets_group = w.group_layer("Streets")
    for index, url in enumerate(url_list):
        map_lyr = MapServiceLayer(url, internal)
        fc = w.feature_class(map_lyr, 0.5)
        fc.update({"visibility": False})
        if popup_names[index] in template:
            fc.update({"popupInfo": template[popup_names[index]]})
        if label_names[index] in template:
            fc.update({"layerDefinition": template[label_names[index]]})
        logging.debug("Appending %s to %s layer.", fc["title"], group_name)
        streets_group["layers"].append(fc)
    map_group["layers"].append(streets_group)
    logging.info("Streets added to %s.", group_name)
    logging.info("Appending layers to %s definition.", group_name)
    w.add_group(base, map_group, basemap)


def sewer_layers(base, template, internal, basemap=False, urls=u.sewer_urls):
    """
    Sewer utilities layers for City of Grants Pass.

    :param base: Group layer definition or map project target for layers.
    :param template: Reference template for map layers.
    :type template: JSON dictionary
    :param internal: Portal connection for internal access layers.
    :type internal: ArcGIS GIS connection.
    :param basemap: Indicates whether appending to group layer or project map.
    :type basemap: Boolean
    :param urls: Url list for published service.
    :type urls: List(String)
    :return: Updates group layer definition with layers.
    :rtype: None
    """
    url_list = urls
    popup_names = t.layer_tags("sewer", url_list, "_popup")
    label_names = t.layer_tags("sewer", url_list, "_label")

    group_name = "Wastewater"
    map_group = w.group_layer(group_name)
    for index, url in enumerate(url_list):
        if urls != u.sewer_urls:
            map_lyr = MapServiceLayer(url, internal)
        else:
            map_lyr = MapServiceLayer(url)
        fc = w.feature_class(map_lyr, 0.5)
        fc.update({"visibility": False})
        if popup_names[index] in template:
            fc.update({"popupInfo": template[popup_names[index]]})
        if label_names[index] in template:
            fc.update({"layerDefinition": template[label_names[index]]})
        logging.debug("Appending %s to %s layer.", fc["title"], group_name)
        map_group["layers"].append(fc)
    logging.info("Appending layers to %s definition.", group_name)
    w.add_group(base, map_group, basemap)


def impervious_layers(base, template, internal, basemap=False, urls=u.impervious_urls):
    """
    Impervious surfaces in the City of Grants Pass.

    :param base: Group layer definition or map project target for layers.
    :param template: Reference template for map layers.
    :type template: JSON dictionary
    :param internal: Portal connection for internal access layers.
    :type internal: ArcGIS GIS connection.
    :param basemap: Indicates whether appending to group layer or project map.
    :type basemap: Boolean
    :param urls: Url list for published service.
    :type urls: List(String)
    :return: Updates group layer definition with layers.
    :rtype: None
    """
    url_list = urls
    popup_names = t.layer_tags("impervious", url_list, "_popup")
    label_names = t.layer_tags("impervious", url_list, "_label")

    group_name = "Impervious Surface"
    map_group = w.group_layer(group_name)
    edit = False
    if urls != u.impervious_urls:
        edit = True
    for index, url in enumerate(url_list):
        if edit:
            map_lyr = MapServiceLayer(url, internal)
        else:
            map_lyr = MapServiceLayer(url)
        fc = w.feature_class(map_lyr, 0.5)
        fc.update({"visibility": False})
        if popup_names[index] in template:
            fc.update({"popupInfo": template[popup_names[index]]})
        if label_names[index] in template:
            fc.update({"layerDefinition": template[label_names[index]]})
        logging.debug("Appending %s to %s layer.", fc["title"], group_name)
        map_group["layers"].append(fc)
    logging.info("Appending layers to %s definition.", group_name)
    w.add_group(base, map_group, basemap)


def stormwater_layers(base, template, internal, basemap=False, urls=u.stormwater_urls):
    """
    Stormwater utilities layers for City of Grants Pass.

    :param base: Group layer definition or map project target for layers.
    :param template: Reference template for map layers.
    :type template: JSON dictionary
    :param internal: Portal connection for internal access layers.
    :type internal: ArcGIS GIS connection.
    :param basemap: Indicates whether appending to group layer or project map.
    :type basemap: Boolean
    :param urls: Url list for published service.
    :type urls: List(String)
    :return: Updates group layer definition with layers.
    :rtype: None
    """
    url_list = urls
    popup_names = t.layer_tags("stormwater", url_list, "_popup")
    label_names = t.layer_tags("stormwater", url_list, "_label")

    group_name = "Stormwater"
    map_group = w.group_layer(group_name)
    impervious_layers(map_group, template, internal)
    for index, url in enumerate(url_list):
        if urls != u.stormwater_urls:
            map_lyr = MapServiceLayer(url, internal)
        else:
            map_lyr = MapServiceLayer(url)
        fc = w.feature_class(map_lyr, 0.5)
        fc.update({"visibility": False})
        if popup_names[index] in template:
            fc.update({"popupInfo": template[popup_names[index]]})
        if label_names[index] in template:
            fc.update({"layerDefinition": template[label_names[index]]})
        logging.debug("Appending %s to %s layer.", fc["title"], group_name)
        if index in [0, 1]:
            map_group["layers"].insert(index, fc)
        else:
            map_group["layers"].append(fc)
    logging.info("Appending layers to %s definition.", group_name)
    w.add_group(base, map_group, basemap)


def water_layers(base, template, internal, basemap=False, urls=u.water_urls):
    """
    Water utilities layers for City of Grants Pass.

    :param base: Group layer definition or map project target for layers.
    :param template: Reference template for map layers.
    :type template: JSON dictionary
    :param internal: Portal connection for internal access layers.
    :type internal: ArcGIS GIS connection.
    :param basemap: Indicates whether appending to group layer or project map.
    :type basemap: Boolean
    :param urls: Url list for published service.
    :type urls: List(String)
    :return: Updates group layer definition with layers.
    :rtype: None
    """
    popup_names = t.layer_tags("water", urls, "_popup")
    label_names = t.layer_tags("water", urls, "_label")

    group_name = "Water Utilities"
    map_group = w.group_layer(group_name)
    edit = False
    if urls == u.water_editing_urls:
        edit = True
    for index, url in enumerate(urls):
        if edit:
            map_lyr = MapServiceLayer(url, internal)
        else:
            map_lyr = MapServiceLayer(url)
        fc = w.feature_class(map_lyr, 0.5)
        fc.update({"visibility": False})
        if index == 2:
            fc.update({"title": "Water Pressure Zones (Billing)"})
        if index == 6:
            fc.update({"title": "Water Mains (by Owner)"})
        if index == 7:
            fc.update({"title": "Water Mains (by Size)"})
        if popup_names[index] in template:
            fc.update({"popupInfo": template[popup_names[index]]})
        if label_names[index] in template:
            fc.update({"layerDefinition": template[label_names[index]]})
        logging.debug("Appending %s to %s layer.", fc["title"], group_name)
        map_group["layers"].append(fc)
    logging.info("Appending layers to %s definition.", group_name)
    w.add_group(base, map_group, basemap)


def power_gas_layers(base, template, internal, basemap=False):
    """
    Pacific Power and Avista Gas utilities for the City of Grants Pass, Oregon.

    :param base: Group layer definition or map project target for layers.
    :param template: Reference template for map layers.
    :type template: JSON dictionary
    :param internal: Portal connection for internal access layers.
    :type internal: ArcGIS GIS connection.
    :param basemap: Indicates whether appending to group layer or project map.
    :type basemap: Boolean
    :return: Updates group layer definition with layers.
    :rtype: None
    """
    popup_names = t.layer_tags("power_gas", u.power_gas_urls, "_popup")
    label_names = t.layer_tags("power_gas", u.power_gas_urls, "_label")
    url_list = u.power_gas_urls

    group_name = "Power & Gas (Internal Use Only)"
    map_group = w.group_layer(group_name)
    for index, url in enumerate(url_list):
        map_lyr = MapServiceLayer(url, internal)
        fc = w.feature_class(map_lyr, 0.5)
        fc.update({"visibility": False})
        if popup_names[index] in template:
            fc.update({"popupInfo": template[popup_names[index]]})
        if label_names[index] in template:
            fc.update({"layerDefinition": template[label_names[index]]})
        logging.debug("Appending %s to %s layer.", fc["title"], group_name)
        map_group["layers"].append(fc)
    logging.info("Appending layers to %s definition.", group_name)
    w.add_group(base, map_group, basemap)


def utility_layers(base, template, internal, public=False, basemap=False):
    """
    Utilities for the City of Grants Pass, Oregon.

    :param base: Group layer definition or map project target for layers.
    :param template: Reference template for map layers.
    :type template: JSON dictionary
    :param internal: Portal connection for internal access layers.
    :type internal: ArcGIS GIS connection.
    :param public: Indicates whether to build internal access layers.
    :type public: Boolean
    :param basemap: Indicates whether appending to group layer or project map.
    :type basemap: Boolean
    :return: Updates group layer definition with layers.
    :rtype: None
    """

    group_name = "Utilities"
    map_group = w.group_layer(group_name)

    w.add_single_layer(
        "cell_towers", u.cell_towers_url, map_group, template, visibility=False
    )
    logging.info("Cell towers added to %s.", group_name)
    sewer_layers(map_group, template, internal)
    logging.info("Sewer layers added to %s.", group_name)
    stormwater_layers(map_group, template, internal)
    logging.info("Stormwater layers added to %s.", group_name)
    water_layers(map_group, template, internal)
    logging.info("Water utilities layers added to %s.", group_name)
    if not public:
        power_gas_layers(map_group, template, internal)
        logging.info("Power and gas utilities layers added to %s.", group_name)

    logging.info("Appending layers to %s definition.", group_name)
    w.add_group(base, map_group, basemap)


def safety_layers(base, template, internal, public=False, basemap=False):
    """
    Public safety layers from Josephine County ECSO 911 service.

    :param base: Group layer definition or map project target for layers.
    :param template: Reference template for map layers.
    :type template: JSON dictionary
    :param basemap: Indicates whether appending to group layer or project map.
    :type basemap: Boolean
    :return: Updates group layer definition with layers.
    :rtype: None
    """

    group_name = "Public Safety"
    map_group = w.group_layer(group_name)

    w.add_single_layer(
        "ecso911_law",
        u.ecso911_law_url,
        map_group,
        template,
        title="Law Enforcement Zones (ECSO 911)",
        visibility=False,
    )
    w.add_single_layer(
        "ecso911_fire",
        u.ecso911_fire_url,
        map_group,
        template,
        title="Fire Response Zones (ECSO 911)",
        visibility=False,
    )
    w.add_single_layer(
        "ecso911_ems",
        u.ecso911_ems_url,
        map_group,
        template,
        title="EMS Response Zones (ECSO 911)",
        visibility=False,
    )

    if not public:
        fire_layers(map_group, template, internal, False)

    logging.info("Appending layers to %s definition.", group_name)
    w.add_group(base, map_group, basemap)


def street_imagery_layers(base, template, basemap=False):
    """
    Street level imagery for the City of Grants Pass, Oregon.

    :param base: Group layer definition or map project target for layers.
    :param template: Reference template for map layers.
    :type template: JSON dictionary
    :param basemap: Indicates whether appending to group layer or project map.
    :type basemap: Boolean
    :return: Updates group layer definition with layers.
    :rtype: None
    """

    w.add_single_layer(
        "street_imagery",
        u.street_imagery_url,
        base,
        template,
        title="Street Imagery (2018)",
        visibility=False,
        basemap=basemap,
    )


def landfill_layers(base, template, basemap=False):
    """
    Merlin landfill layers for the City of Grants Pass, Oregon.

    :param base: Group layer definition or map project target for layers.
    :param template: Reference template for map layers.
    :type template: JSON dictionary
    :param basemap: Indicates whether appending to group layer or project map.
    :type basemap: Boolean
    :return: Updates group layer definition with layers.
    :rtype: None
    """

    popup_names = t.layer_tags("landfill", u.landfill_urls, "_popup")
    label_names = t.layer_tags("landfill", u.landfill_urls, "_label")
    url_list = u.landfill_urls

    group_name = "Merlin Landfill"
    map_group = w.group_layer(group_name)
    for index, url in enumerate(url_list):
        map_lyr = MapServiceLayer(url)
        fc = w.feature_class(map_lyr, 0.5)
        fc.update({"visibility": False})
        if popup_names[index] in template:
            fc.update({"popupInfo": template[popup_names[index]]})
        if label_names[index] in template:
            fc.update({"layerDefinition": template[label_names[index]]})
        logging.debug("Appending %s to %s layer.", fc["title"], group_name)
        map_group["layers"].append(fc)
    logging.info("Appending layers to %s definition.", group_name)
    w.add_group(base, map_group, basemap)


def wells_layers(group_lyr, template):
    """
    Wells layers from the OWRD service.

    :param group_lyr: Group layer definition target for layers.
    :return: Updates group layer definition with layers.
    :rtype: None
    """

    popup_names = t.layer_tags("wells", u.wells_urls, "_popup")
    label_names = t.layer_tags("wells", u.wells_urls, "_label")
    url_list = u.wells_urls

    map_name = "Wells (OWRD)"
    map_group = w.group_layer(map_name)
    char_group = w.group_layer("Well Characteristics")
    geo_group = w.group_layer("Type of Work for Geotechnical Holes")
    water_group = w.group_layer("Type of Work for Water/Monitor Wells")
    log_group = w.group_layer("Type of Log")
    prim_group = w.group_layer("Primary Use")
    for index, url in enumerate(url_list):
        map_lyr = MapServiceLayer(url)
        fc = w.feature_class(map_lyr, 0.5)
        fc.update({"visibility": False})
        if popup_names[index] in template:
            fc.update({"popupInfo": template[popup_names[index]]})
        if label_names[index] in template:
            fc.update({"layerDefinition": template[label_names[index]]})
        logging.debug("Appending %s to %s layer.", fc["title"], map_name)
        if index in [0, 1]:
            char_group["layers"].append(fc)
        if index >= 2 and index <= 10:
            prim_group["layers"].append(fc)
        if index >= 11 and index <= 16:
            geo_group["layers"].append(fc)
        if index >= 17 and index <= 22:
            water_group["layers"].append(fc)
        if index >= 23 and index <= 25:
            log_group["layers"].append(fc)
    char_group["layers"].append(prim_group)
    map_group["layers"].append(char_group)
    map_group["layers"].append(geo_group)
    map_group["layers"].append(water_group)
    map_group["layers"].append(log_group)
    group_lyr["layers"].append(map_group)


def traffic_layers(base, template, basemap=False):
    """
    Traffic reports for the City of Grants Pass, Oregon.

    :param base: Group layer definition or map project target for layers.
    :param template: Reference template for map layers.
    :type template: JSON dictionary
    :param basemap: Indicates whether appending to group layer or project map.
    :type basemap: Boolean
    :return: Updates group layer definition with layers.
    :rtype: None
    """

    popup_names = t.layer_tags("traffic", u.traffic_urls, "_popup")
    label_names = t.layer_tags("traffic", u.traffic_urls, "_label")
    url_list = u.traffic_urls

    group_name = "Traffic"
    map_group = w.group_layer(group_name)
    for index, url in enumerate(url_list):
        map_lyr = MapServiceLayer(url)
        fc = w.feature_class(map_lyr, 0.5)
        fc.update({"visibility": False})
        if popup_names[index] in template:
            fc.update({"popupInfo": template[popup_names[index]]})
        if label_names[index] in template:
            fc.update({"layerDefinition": template[label_names[index]]})
        logging.debug("Appending %s to %s layer.", fc["title"], group_name)
        map_group["layers"].append(fc)
    logging.info("Appending layers to %s definition.", group_name)
    w.add_group(base, map_group, basemap)


def tourism_layers(base, template, basemap=False):
    """
    Tourism features for the City of Grants Pass.

    :param base: Group layer definition or map project target for layers.
    :param template: Reference template for map layers.
    :type template: JSON dictionary
    :param basemap: Indicates whether appending to group layer or project map.
    :type basemap: Boolean
    :return: Updates group layer definition with layers.
    :rtype: None
    """

    group_name = "Tourism"
    map_group = w.group_layer(group_name)

    parking_layers(map_group, template)
    logging.info("Parking added to %s.", group_name)
    parks_trails(map_group, template)
    logging.info("Parks and trails added to %s.", group_name)
    historic_cultural_tourism(map_group, template)
    logging.info("Historic/Cultural areas added to %s.", group_name)
    logging.info("Appending layers to %s definition.", group_name)
    w.add_group(base, map_group, basemap)


def business_layers(base, template, basemap=False, urls=u.businesses_urls):
    """
    Business layers for the City of Grants Pass, Oregon.

    :param base: Group layer definition or map project target for layers.
    :param template: Reference template for map layers.
    :type template: JSON dictionary
    :param basemap: Indicates whether appending to group layer or project map.
    :type basemap: Boolean
    :param urls: Url list for published service.
    :type urls: List(String)
    :return: Updates group layer definition with layers.
    :rtype: None
    """
    popup_names = t.layer_tags("businesses", urls, "_popup")
    label_names = t.layer_tags("businesses", urls, "_label")

    group_name = "Economic Development"
    map_group = w.group_layer(group_name)
    # edit = False
    # if urls != u.businesses_url:
    #     edit = True
    for index, url in enumerate(urls):
        # if edit:
        #     map_lyr = MapServiceLayer(url, internal)
        # else:
        #     map_lyr = MapServiceLayer(url)
        map_lyr = MapServiceLayer(url)
        fc = w.feature_class(map_lyr, 0.5)
        fc.update({"visibility": False})
        if popup_names[index] in template:
            fc.update({"popupInfo": template[popup_names[index]]})
        if label_names[index] in template:
            fc.update({"layerDefinition": template[label_names[index]]})
        logging.debug("Appending %s to %s layer.", fc["title"], group_name)
        map_group["layers"].append(fc)
    logging.info("Appending layers to %s definition.", group_name)
    w.add_group(base, map_group, basemap)


def fire_layers(base, template, internal, basemap=False, urls=u.fire_service_urls):
    """
    Fire service layers for the City of Grants Pass, Oregon.

    :param base: Group layer definition or map project target for layers.
    :param template: Reference template for map layers.
    :type template: JSON dictionary
    :param internal: Portal connection for internal access layers.
    :type internal: ArcGIS GIS connection.
    :param basemap: Indicates whether appending to group layer or project map.
    :type basemap: Boolean
    :param urls: Url list for published service.
    :type urls: List(String)
    :return: Updates group layer definition with layers.
    :rtype: None
    """
    popup_names = t.layer_tags("fire", urls, "_popup")
    label_names = t.layer_tags("fire", urls, "_label")

    group_name = "Fire"
    map_group = w.group_layer(group_name)
    for index, url in enumerate(urls):
        map_lyr = MapServiceLayer(url, internal)
        fc = w.feature_class(map_lyr, 0.5)
        fc.update({"visibility": False})
        if popup_names[index] in template:
            fc.update({"popupInfo": template[popup_names[index]]})
        if label_names[index] in template:
            fc.update({"layerDefinition": template[label_names[index]]})
        logging.debug("Appending %s to %s layer.", fc["title"], group_name)
        map_group["layers"].append(fc)
    logging.info("Appending layers to %s definition.", group_name)
    w.add_group(base, map_group, basemap)


def sketch_layers(base, template, internal, public=False, basemap=False):
    """
    Staff markup layers for the City of Grants Pass, Oregon.

    :param base: Group layer definition or map project target for layers.
    :param template: Reference template for map layers.
    :type template: JSON dictionary
    :param internal: Portal connection for internal access layers.
    :type internal: ArcGIS GIS connection.
    :param public: Indicates whether to build internal access layers.
    :type public: Boolean
    :param basemap: Indicates whether appending to group layer or project map.
    :type basemap: Boolean
    :return: Updates group layer definition with layers.
    :rtype: None
    """

    if not public:
        popup_names = t.layer_tags("sketch", u.sketch_urls, "_popup")
        label_names = t.layer_tags("sketch", u.sketch_urls, "_label")
        url_list = u.sketch_urls

        group_name = "Sketch Editing"
        map_group = w.group_layer(group_name)
        for index, url in enumerate(url_list):
            map_lyr = MapServiceLayer(url, internal)
            fc = w.feature_class(map_lyr, 0.5)
            fc.update({"visibility": False})
            if popup_names[index] in template:
                fc.update({"popupInfo": template[popup_names[index]]})
            if label_names[index] in template:
                fc.update({"layerDefinition": template[label_names[index]]})
            logging.debug("Appending %s to %s layer.", fc["title"], group_name)
            map_group["layers"].append(fc)
        logging.info("Appending layers to %s definition.", group_name)
        w.add_group(base, map_group, basemap)
        logging.info("Sketch editing added to map.")


def address_editing_layers(base, template, internal, basemap=False):
    """
    Address editing layers for the City of Grants Pass, Oregon.

    :param base: Group layer definition or map project target for layers.
    :param template: Reference template for map layers.
    :type template: JSON dictionary
    :param internal: Portal connection for internal access layers.
    :type internal: ArcGIS GIS connection.
    :param basemap: Indicates whether appending to group layer or project map.
    :type basemap: Boolean
    :return: Updates group layer definition with layers.
    :rtype: None
    """

    popup_names = t.layer_tags("address_verification", u.address_editing_urls, "_popup")
    label_names = t.layer_tags("address_verification", u.address_editing_urls, "_label")
    url_list = u.address_editing_urls

    group_name = "Address Editing"
    map_group = w.group_layer(group_name)
    for index, url in enumerate(url_list):
        map_lyr = MapServiceLayer(url, internal)
        fc = w.feature_class(map_lyr, 0.5)
        fc.update({"visibility": False})
        if popup_names[index] in template:
            fc.update({"popupInfo": template[popup_names[index]]})
        if label_names[index] in template:
            fc.update({"layerDefinition": template[label_names[index]]})
        logging.debug("Appending %s to %s layer.", fc["title"], group_name)
        map_group["layers"].append(fc)
    logging.info("Appending layers to %s definition.", group_name)
    w.add_group(base, map_group, basemap)
    logging.info("Address editing added to map.")


def editing_map(project_map, template, internal, public=False):
    """
    Add common reference layers to web map.

    :param project_map: Web map to update with reference layers.
    :return: Updates the web map, adding reference layers.
    :rtype: None.
    """
    map_name = "City Web Editor"
    logging.info("Building %s.", map_name)

    # city_basemap(project_map, template, internal, public)
    aerial_imagery(project_map, True)
    sketch_layers(project_map, template, internal, public, True)
    sewer_layers(project_map, template, internal, True, u.sewer_editing)
    stormwater_layers(project_map, template, internal, True, u.stormwater_editing)
    water_layers(project_map, template, internal, True, u.water_editing_urls)
    transportation_layers(
        project_map, template, internal, True, u.transportation_editing_urls
    )
    land_use_layers(project_map, template, internal, True, u.land_use_editing_urls)
    address_editing_layers(project_map, template, internal, True)

    logging.info("Adding editing search.")
    s.add_search(project_map, s.search_edit_list)


def city_basemap(project_map, template, internal, public=False):
    """
    Add common reference layers to web map.

    :param project_map: Web map to update with reference layers.
    :return: Updates the web map, adding reference layers.
    :rtype: None.
    """
    map_name = "City Web Viewer"
    logging.info("Building %s.", map_name)

    # aerial_imagery(project_map, True)
    # logging.info("Aerial imagery added to %s.", map_name)
    # street_imagery_layers(project_map, template, True)
    # logging.info("Street imagery added to %s.", map_name)
    # sketch_layers(project_map, template, internal, public, True)
    # landfill_layers(project_map, template, True)
    # logging.info("Merlin landfill added to %s.", map_name)
    # safety_layers(project_map, template, internal, public, True)
    # logging.info("Public safety layers added to %s.", map_name)
    # environment_layers(project_map, template, True)
    # logging.info("Environment layers added to %s.", map_name)
    # utility_layers(project_map, template, internal, public, True)
    # logging.info("Utility layers added to %s.", map_name)
    transportation_layers(project_map, template, internal, True)
    logging.info("Transportation layers added to %s.", map_name)
    # if not public:
    #     business_layers(project_map, template, True)
    #     logging.info("Economic Development layers added to %s.", map_name)

    # agreements_layers(project_map, template, True)
    # planning_layers(project_map, template, True)
    # logging.info("Planning layers added to %s.", map_name)
    # land_use_layers(project_map, template, internal, True)
    # logging.info("Land use layers added to %s.", map_name)
    # boundary_layers(project_map, template, True)
    # logging.info("Regulatory boundaries added to %s.", map_name)
    # tourism_layers(project_map, template, True)
    # logging.info("Tourism group added to %s.", map_name)

    logging.info("Adding search.")
    s.add_search(project_map)


def web_viewer(project_map, template, internal, public=False):
    """
    Add common reference layers to web map.

    :param project_map: Web map to update with reference layers.
    :return: Updates the web map, adding reference layers.
    :rtype: None.
    """
    map_name = "City of Grants Pass Web Viewer"
    logging.info("Building %s.", map_name)

    aerial_imagery(project_map, True)
    logging.info("Aerial imagery added to %s.", map_name)
    street_imagery_layers(project_map, template, True)
    logging.info("Street imagery added to %s.", map_name)
    sketch_layers(project_map, template, internal, public, True)
    landfill_layers(project_map, template, True)
    logging.info("Merlin landfill added to %s.", map_name)
    safety_layers(project_map, template, internal, public, True)
    logging.info("Public safety layers added to %s.", map_name)
    e.environment(project_map, template, True)
    logging.info("Environment layers added to %s.", map_name)
    parks_layers(project_map, template, True)
    logging.info("Parks layers added to %s.", map_name)
    ut.utilities(project_map, template, internal, public, True)
    logging.info("Utility layers added to %s.", map_name)
    tr.transportation_layers(project_map, template, internal, True)
    logging.info("Transportation layers added to %s.", map_name)
    if not public:
        business_layers(project_map, template, True)
        logging.info("Economic Development layers added to %s.", map_name)

    pl.planning(project_map, template, False, True)
    logging.info("Planning layers added to %s.", map_name)
    p.property(project_map, template, internal, True)
    logging.info("Property layers added to %s.", map_name)
    b.boundaries(project_map, template, True)
    logging.info("Boundaries added to %s.", map_name)

    logging.info("Adding search.")
    s.add_search(project_map)
