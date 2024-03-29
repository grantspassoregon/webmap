from webmap import maps as m
from webmap import refs as r
from webmap import urls as u
from arcgis.mapping import WebMap
import logging
import pprint


plss_names = [
    "state",
    "township",
    "section",
    "intersected",
]

bia_names = [
    "land_area",
    "tribal_entities",
]


def layer_names(pre, names, post):
    """
    Create list of key names for layer definition data.

    :param pre: Prefix for layer names.
    :type pre: String
    :param names: List of layer names to store in template.
    :type names: List
    :param post: Postscript to append to layer names.
    :type post: String
    :return: List of fully specified layer names for template.
    :rtype: List
    """
    layer_name = []
    for lyr in names:
        layer_name.append(pre + lyr + post)
    # layer order is reversed from menu order
    layer_name.reverse()
    return layer_name


def layer_tags(pre, urls, post):
    """
    Create list of key names for layer definition data.

    :param pre: Prefix for layer names.
    :type pre: String
    :param urls: List of layers to store in template.
    :type names: List
    :param post: Postscript to append to layer names.
    :type post: String
    :return: List of generic layer names for template.
    :rtype: List
    """
    layer_name = []
    for i in range(0, len(urls)):
        layer_name.append(pre + str(i) + post)
    # layer order is reversed from menu order
    layer_name.reverse()
    return layer_name


def build_template(gis):
    """
    Build template dictionary from template maps.  The template stores layer
    definition information (style, labels, whether popups are enabled, etc.)
    referenced by the package when constructing a new map.

    :return: Updates the template.json file.
    """
    logging.info("Loading template layers from %s.", gis)
    address_editing = gis.content.get(r.TEMPLATE_ADDRESS_EDITING)
    address_verification = gis.content.get(r.TEMPLATE_ADDRESS_VERIFICATION)
    agreements = gis.content.get(r.TEMPLATE_AGREEMENTS)
    as_builts = gis.content.get(r.TEMPLATE_AS_BUILTS)
    aiannha = gis.content.get(r.TEMPLATE_AIANNHA)
    bia = gis.content.get(r.TEMPLATE_BIA)
    boundaries_group = gis.content.get(r.TEMPLATE_BOUNDARIES_GROUP)
    businesses = gis.content.get(r.TEMPLATE_BUSINESS)
    cell_towers = gis.content.get(r.TEMPLATE_CELL_TOWERS)
    city_boundaries = gis.content.get(r.TEMPLATE_CITY_BOUNDARIES)
    deq_dw_source = gis.content.get(r.TEMPLATE_DEQ_DW_SOURCE)
    # deq_dw_pcs = gis.content.get(r.TEMPLATE_DEQ_DW_PCS)
    deq_hydro_2022 = gis.content.get(r.TEMPLATE_DEQ_HYDRO)
    dsl_esh = gis.content.get(r.TEMPLATE_DSL_ESH)
    ecso911_ems = gis.content.get(r.REF_ECSO911_EMS)
    ecso911_fire = gis.content.get(r.REF_ECSO911_FIRE)
    ecso911_law = gis.content.get(r.REF_ECSO911_LAW)
    features = gis.content.get(r.TEMPLATE_FEATURES)
    fema_flood = gis.content.get(r.TEMPLATE_FEMA_FLOOD)
    fema_flood_wv = gis.content.get(r.TEMPLATE_FEMA_FLOOD_WV)
    fire = gis.content.get(r.TEMPLATE_FIRE)
    hazards = gis.content.get(r.TEMPLATE_HAZARDS)
    historic_cultural = gis.content.get(r.TEMPLATE_HISTORIC_CULTURAL)
    hydric_soils = gis.content.get(r.TEMPLATE_HYDRIC_SOILS)
    impervious = gis.content.get(r.TEMPLATE_IMPERVIOUS)
    land_use = gis.content.get(r.TEMPLATE_LAND_USE)
    landfill = gis.content.get(r.TEMPLATE_LANDFILL)
    marijuana_adult_use = gis.content.get(r.TEMPLATE_MARIJUANA_ADULT_USE)
    marijuana_permitting = gis.content.get(r.TEMPLATE_MARIJUANA_PERMITTING)
    missing_sidewalks = gis.content.get(r.TEMPLATE_MISSING_SIDEWALKS)
    nhd = gis.content.get(r.TEMPLATE_NHD)
    oprd = gis.content.get(r.TEMPLATE_OPRD_HISTORIC_SITES)
    parking = gis.content.get(r.TEMPLATE_PARKING)
    parks = gis.content.get(r.TEMPLATE_PARKS)
    planning = gis.content.get(r.TEMPLATE_PLANNING)
    plss = gis.content.get(r.TEMPLATE_PLSS)
    power_gas = gis.content.get(r.TEMPLATE_POWER_GAS)
    property = gis.content.get(r.TEMPLATE_PROPERTY)
    schools = gis.content.get(r.TEMPLATE_SCHOOLS)
    schools_wv = gis.content.get(r.TEMPLATE_SCHOOLS_WV)
    sketch = gis.content.get(r.TEMPLATE_SKETCH)
    sewer = gis.content.get(r.TEMPLATE_SEWER)
    soils = gis.content.get(r.TEMPLATE_SOILS)
    stormwater = gis.content.get(r.TEMPLATE_STORMWATER)
    street_imagery = gis.content.get(r.TEMPLATE_STREET_IMAGERY)
    tax_parcels = gis.content.get(r.TEMPLATE_TAX_PARCELS)
    tourism_historic = gis.content.get(r.TEMPLATE_TOURISM_HISTORIC)
    tourism_parks = gis.content.get(r.TEMPLATE_TOURISM_PARKS)
    traffic = gis.content.get(r.TEMPLATE_TRAFFIC)
    transportation = gis.content.get(r.TEMPLATE_TRANSPORTATION)
    transportation_wv = gis.content.get(r.TEMPLATE_TRANSPORTATION_WV)
    transportation_editing = gis.content.get(r.TEMPLATE_TRANSPORTATION_EDITING)
    water = gis.content.get(r.TEMPLATE_WATER)
    water_wv = gis.content.get(r.TEMPLATE_WATER_WV)
    water_editing = gis.content.get(r.TEMPLATE_WATER_EDITING)
    wells = gis.content.get(r.TEMPLATE_OWRD_WELLS)
    wetlands = gis.content.get(r.TEMPLATE_WETLANDS)
    zoning = gis.content.get(r.TEMPLATE_ZONING)

    logging.info("Building template dictionary.")
    template = {}
    template.update(build_template_dictionary("address_editing", address_editing))
    template.update(
        build_template_dictionary("address_verification", address_verification)
    )
    template.update(build_template_dictionary("agreements", agreements))
    template.update(build_template_dictionary("as_builts", as_builts))
    template.update(build_template_dictionary("aiannha", aiannha))
    template.update(build_template_dictionary("bia", bia))
    template.update(build_template_dictionary("boundaries_group", boundaries_group))
    template.update(build_template_dictionary("businesses", businesses))
    template.update(build_template_dictionary("cell_towers", cell_towers))
    template.update(build_template_dictionary("city_boundaries", city_boundaries))
    template.update(build_template_dictionary("deq_dw_source", deq_dw_source))
    # template.update(build_template_dictionary("deq_dw_pcs", deq_dw_pcs))
    template.update(build_template_dictionary("deq_hydro_2022", deq_hydro_2022))
    template.update(build_template_dictionary("dsl_esh", dsl_esh))
    template.update(build_template_dictionary("ecso911_ems", ecso911_ems))
    template.update(build_template_dictionary("ecso911_fire", ecso911_fire))
    template.update(build_template_dictionary("ecso911_law", ecso911_law))
    template.update(build_template_dictionary("features", features))
    template.update(build_template_dictionary("fema_flood", fema_flood))
    template.update(build_template_dictionary("fema_flood_wv", fema_flood_wv))
    template.update(build_template_dictionary("fire", fire))
    template.update(build_template_dictionary("hazards", hazards))
    template.update(build_template_dictionary("historic", historic_cultural))
    template.update(build_template_dictionary("hydric_soils", hydric_soils))
    template.update(build_template_dictionary("impervious", impervious))
    template.update(build_template_dictionary("land_use", land_use))
    template.update(build_template_dictionary("landfill", landfill))
    template.update(
        build_template_dictionary("marijuana_adult_use", marijuana_adult_use)
    )
    template.update(
        build_template_dictionary("marijuana_permitting", marijuana_permitting)
    )
    template.update(build_template_dictionary("missing_sidewalks", missing_sidewalks))
    template.update(build_template_dictionary("nhd", nhd))
    template.update(build_template_dictionary("oprd", oprd))
    template.update(build_template_dictionary("parking", parking))
    template.update(build_template_dictionary("parks", parks))
    template.update(build_template_dictionary("planning", planning))
    template.update(build_template_dictionary("plss", plss))
    template.update(build_template_dictionary("power_gas", power_gas))
    template.update(build_template_dictionary("property", property))
    template.update(build_template_dictionary("schools", schools))
    template.update(build_template_dictionary("schools_wv", schools_wv))
    template.update(build_template_dictionary("sketch", sketch))
    template.update(build_template_dictionary("sewer", sewer))
    template.update(build_template_dictionary("soils", soils))
    template.update(build_template_dictionary("stormwater", stormwater))
    template.update(build_template_dictionary("street_imagery", street_imagery))
    template.update(build_template_dictionary("tax_parcels", tax_parcels))
    template.update(build_template_dictionary("tourism_historic", tourism_historic))
    template.update(build_template_dictionary("tourism_parks", tourism_parks))
    template.update(build_template_dictionary("traffic", traffic))
    template.update(build_template_dictionary("transportation", transportation))
    template.update(build_template_dictionary("transportation_wv", transportation_wv))
    template.update(
        build_template_dictionary("transportation_editing", transportation_editing)
    )
    template.update(build_template_dictionary("water", water))
    template.update(build_template_dictionary("water_wv", water_wv))
    template.update(build_template_dictionary("water_editing", water_editing))
    template.update(get_definition("wells", wells))
    template.update(build_template_dictionary("wetlands", wetlands))
    template.update(build_template_dictionary("zoning", zoning))
    logging.info("Template dictionary complete.")
    return template
    # file_name = os.path.join(TEMPLATE_DIR, "template.json")
    # with open(file_name, "w") as fp:
    #     json.dump(template, fp, sort_keys=True, indent=4)


def build_template_dictionary(template_type, template):
    logging.debug("Building template for %s.", template_type)
    template_dict = {}
    match template_type:
        case "address_editing":
            template_dict.update(
                get_layer_info(template, "address_editing", u.address_editing_urls)
            )
        case "address_verification":
            template_dict.update(
                get_layer_info(template, "address_verification", u.address_editing_urls)
            )
        case "agreements":
            template_dict.update(
                get_layer_info(template, "agreements", u.agreements_urls)
            )
        case "as_builts":
            template_dict.update(update_layer("as_builts", u.as_builts_urls, template))
        case "aiannha":
            template_dict.update(update_layer("aiannha", u.aiannha_urls, template))
        case "bia":
            template_dict.update(update_layers("bia", bia_names, template))
        case "boundaries_group":
            template_dict.update(
                get_layer_info(template, "boundaries_group", u.boundaries_group)
            )
        case "businesses":
            template_dict.update(
                get_layer_info(template, "businesses", u.businesses_urls)
            )
        case "cell_towers":
            template_dict.update(update_layers("cell_towers", [""], template))
        case "city_boundaries":
            template_dict.update(
                get_layer_info(template, "city_boundaries", u.boundaries_urls)
            )
        case "deq_dw_source":
            template_dict.update(
                get_layer_info(
                    template, "deq_dw_source", u.deq_drinking_water_source_urls
                )
            )
        # case "deq_dw_pcs":
        #     template_dict.update(
        #         update_layer(
        #             "deq_dw_pcs", u.deq_drinking_water_protection_urls, template
        #         )
        #     )
        case "deq_hydro_2022":
            template_dict.update(
                update_layer("deq_hydro_2022", u.deq_hydro_2022_urls, template)
            )
        case "dsl_esh":
            template_dict.update(get_layer_info(template, "dsl_esh", u.dsl_esh_urls))
        case "ecso911_ems":
            template_dict.update(update_layers("ecso911_ems", [""], template))
        case "ecso911_fire":
            template_dict.update(update_layers("ecso911_fire", [""], template))
        case "ecso911_law":
            template_dict.update(update_layers("ecso911_law", [""], template))
        case "features":
            template_dict.update(update_layer("features", u.features_urls, template))
        case "fema_flood":
            template_dict.update(
                update_layer("fema_flood", u.fema_flood_urls, template)
            )
        case "fema_flood_wv":
            template_dict.update(
                get_layer_info(template, "fema_flood_wv", u.fema_flood_wv)
            )
        case "fire":
            template_dict.update(get_layer_info(template, "fire", u.fire_service_urls))
        case "hazards":
            template_dict.update(update_layer("hazards", u.hazards_urls, template))
        case "historic":
            template_dict.update(
                update_layer("historic", u.historic_cultural_areas_urls, template)
            )
        case "hydric_soils":
            template_dict.update(update_layers("hydric_soils", [""], template))
        case "impervious":
            template_dict.update(
                get_layer_info(template, "impervious", u.impervious_urls)
            )
        case "land_use":
            template_dict.update(get_layer_info(template, "land_use", u.land_use_urls))
        case "landfill":
            template_dict.update(update_layer("landfill", u.landfill_urls, template))
        case "marijuana_adult_use":
            template_dict.update(
                update_layer("marijuana_adult_use", u.marijuana_adult_urls, template)
            )
        case "marijuana_permitting":
            template_dict.update(
                get_layer_info(
                    template, "marijuana_permitting", u.marijuana_permitting_urls
                )
            )
        case "missing_sidewalks":
            template_dict.update(
                update_layer_info(m.missing_sidewalks_layer_names, template)
            )
        case "nhd":
            template_dict.update(update_layer("nhd", u.nhd_urls, template))
        case "oprd":
            template_dict.update(update_layers("oprd", [""], template))
        case "parking":
            template_dict.update(update_layer("parking", u.parking_urls, template))
        case "parks":
            template_dict.update(update_layer("parks", u.parks_urls, template))
        case "planning":
            template_dict.update(get_layer_info(template, "planning", u.planning_urls))
        case "plss":
            template_dict.update(update_layers("plss", plss_names, template))
        case "power_gas":
            template_dict.update(update_layer("power_gas", u.power_gas_urls, template))
        case "property":
            template_dict.update(get_layer_info(template, "property", u.property_urls))
        case "schools":
            template_dict.update(
                get_layer_info(template, "schools", u.school_districts_urls)
            )
        case "schools_wv":
            template_dict.update(
                get_layer_info(template, "schools_wv", u.school_districts_group)
            )
        case "sketch":
            template_dict.update(get_layer_info(template, "sketch", u.sketch_urls))
        case "sewer":
            template_dict.update(update_layer("sewer", u.sewer_urls, template))
        case "soils":
            template_dict.update(update_layers("soils", [""], template))
        case "stormwater":
            template_dict.update(
                get_layer_info(template, "stormwater", u.stormwater_urls)
            )
        case "street_imagery":
            template_dict.update(update_layers("street_imagery", [""], template))
        case "tax_parcels":
            template_dict.update(
                get_layer_info(template, "tax_parcels", u.tax_parcel_urls)
            )
        case "tourism_historic":
            template_dict.update(
                get_layer_info(
                    template, "tourism_historic", u.historic_cultural_tourism_urls
                )
            )
        case "tourism_parks":
            template_dict.update(
                get_layer_info(template, "tourism_parks", u.tourism_parks_urls)
            )
        case "traffic":
            template_dict.update(update_layer("traffic", u.traffic_urls, template))
        case "transportation":
            template_dict.update(
                update_layer("transportation", u.transportation_urls, template)
            )
        case "transportation_wv":
            template_dict.update(
                get_layer_info(template, "transportation_wv", u.transportation_group)
            )
        case "transportation_editing":
            template_dict.update(
                get_layer_info(
                    template, "transportation_editing", u.transportation_editing
                )
            )
        case "water":
            template_dict.update(update_layer("water", u.water_urls, template))
        case "water_wv":
            template_dict.update(get_layer_info(template, "water_wv", u.water_wv))
        case "water_editing":
            template_dict.update(
                get_layer_info(template, "water_editing", u.water_urls)
            )
        case "wells":
            template_dict.update(update_layer("wells", u.wells_urls, template))
        case "wetlands":
            template_dict.update(update_layers("wetlands", [""], template))
        case "zoning":
            template_dict.update(update_layer("zoning", u.zoning_urls, template))

    return template_dict


def update_layer_info(names, template):
    """
    Build dictionary of layer info for layers. Includes popup info.

    :param names: Function returned layers names, appends argument to base name.
    :param template: Web map template for layer fields.
    :return: Dictionary of short keys and layer definitions for the survey layers.
    """
    popup_name = names("_popup")
    label_name = names("_label")
    ref_data = template.get_data()
    ref_list = ref_data["operationalLayers"][0]["layers"][0]["layers"]
    new_data = {}
    for i in range(0, len(popup_name)):
        logging.debug("Template layer %s.", i)
        new_data.update({popup_name[i]: ref_list[i]["popupInfo"]})
        new_data.update({label_name[i]: ref_list[i]["layerDefinition"]})

    return new_data


def update_layers(prefix, names, template):
    """
    Build dictionary of layer info for layers. Includes popup info.

    :param prefix: Prefix string for layer names.
    :param names: List of layer names for template.
    :param template: Web map template for layer fields.
    :return: Dictionary of short keys and layer definitions for the survey layers.
    """
    popup_name = layer_names(prefix, names, "_popup")
    label_name = layer_names(prefix, names, "_label")
    ref_data = template.get_data()
    ref_list = ref_data["operationalLayers"][0]["layers"][0]["layers"]
    new_data = {}
    for i in range(0, len(popup_name)):
        logging.debug("Template layer %s.", i)
        if "popupInfo" in ref_list[i]:
            new_data.update({popup_name[i]: ref_list[i]["popupInfo"]})
        if "layerDefinition" in ref_list[i]:
            new_data.update({label_name[i]: ref_list[i]["layerDefinition"]})

    return new_data


def update_layer(prefix, urls, template):
    """
    Build dictionary of layer info for layers. Includes popup info.

    :param prefix: Prefix string for layer names.
    :param urls: List of layer urls for template.
    :param template: Web map template for layer fields.
    :return: Dictionary of short keys and layer definitions for the survey layers.
    """
    popup_name = layer_tags(prefix, urls, "_popup")
    label_name = layer_tags(prefix, urls, "_label")
    ref_data = template.get_data()
    ref_list = ref_data["operationalLayers"][0]["layers"][0]["layers"]
    new_data = {}
    for i in range(0, len(popup_name)):
        if "popupInfo" in ref_list[i]:
            new_data.update({popup_name[i]: ref_list[i]["popupInfo"]})
            logging.debug("Updating popup info for %s in %s", i, prefix)
        if "layerDefinition" in ref_list[i]:
            new_data.update({label_name[i]: ref_list[i]["layerDefinition"]})
            logging.debug("Updating layer definition for %s in %s", i, prefix)
        # new_data.update({popup_name[i]: ref_list[i]["popupInfo"]})
        # new_data.update({label_name[i]: ref_list[i]["layerDefinition"]})

    return new_data


def get_definition(name, map):
    # pp = pprint.PrettyPrinter(width=4)
    # test_map = gis.content.get(map)
    map_def = map.get_data()
    # logging.debug(pp.pprint(map_def["operationalLayers"][0]["layers"]))
    template = {}
    template.update({name: map_def["operationalLayers"][0]["layers"]})
    return template


def get_layer_info(item, prefix, urls):
    """
    Read a template file, match layers to a list of urls and return a dictionary
    of popup info and layer definitions.

    :param item: Template web map to read layer info from.
    :param prefix: Short name to prefix to layers for storage in the template dictionary.
    :type prefix: String
    :param urls: List of urls stored on template web map.
    :type urls: List with String elements readable as urls.
    :return: Dictionary of layer info.
    :rtype: Dictionary with String identifiers as keys, and popup info or layer definitions as values.
    """
    popup_name = layer_tags(prefix, urls, "_popup")
    label_name = layer_tags(prefix, urls, "_label")
    wm = WebMap(item)
    lyrs = wm.layers
    layer_info = recursive_layer_info(lyrs, popup_name, label_name)
    return layer_info


def recursive_layer_info(layers, popup_name, label_name, layer_info={}, index=0):
    for lyr in layers:
        logging.debug("Reading layer %s.", lyr["title"])
        flag = False
        if "popupInfo" in lyr:
            layer_info.update({popup_name[index]: lyr["popupInfo"]})
            flag = True
        if "layerDefinition" in lyr:
            layer_info.update({label_name[index]: lyr["layerDefinition"]})
            flag = True
        if flag:
            index += 1
        if lyr["layerType"] in ["GroupLayer"]:
            recursive_layer_info(
                lyr["layers"], popup_name, label_name, layer_info, index
            )
    return layer_info
