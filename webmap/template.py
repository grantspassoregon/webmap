from webmap import maps as m
from webmap import refs as r
from webmap import urls as u
import logging


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
    agreements = gis.content.get(r.TEMPLATE_AGREEMENTS)
    as_builts = gis.content.get(r.TEMPLATE_AS_BUILTS)
    aiannha = gis.content.get(r.TEMPLATE_AIANNHA)
    bia = gis.content.get(r.TEMPLATE_BIA)
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
    hazards = gis.content.get(r.TEMPLATE_HAZARDS)
    historic_cultural = gis.content.get(r.TEMPLATE_HISTORIC_CULTURAL)
    hydric_soils = gis.content.get(r.TEMPLATE_HYDRIC_SOILS)
    land_use = gis.content.get(r.TEMPLATE_LAND_USE)
    landfill = gis.content.get(r.TEMPLATE_LANDFILL)
    marijuana_adult_use = gis.content.get(r.TEMPLATE_MARIJUANA_ADULT_USE)
    missing_sidewalks = gis.content.get(r.TEMPLATE_MISSING_SIDEWALKS)
    nhd = gis.content.get(r.TEMPLATE_NHD)
    plss = gis.content.get(r.TEMPLATE_PLSS)
    power_gas = gis.content.get(r.TEMPLATE_POWER_GAS)
    schools = gis.content.get(r.TEMPLATE_SCHOOLS)
    sewer = gis.content.get(r.TEMPLATE_SEWER)
    soils = gis.content.get(r.TEMPLATE_SOILS)
    stormwater = gis.content.get(r.TEMPLATE_STORMWATER)
    street_imagery = gis.content.get(r.TEMPLATE_STREET_IMAGERY)
    tax_parcels = gis.content.get(r.TEMPLATE_TAX_PARCELS)
    transportation = gis.content.get(r.TEMPLATE_TRANSPORTATION)
    water = gis.content.get(r.TEMPLATE_WATER)
    wetlands = gis.content.get(r.TEMPLATE_WETLANDS)
    zoning = gis.content.get(r.TEMPLATE_ZONING)

    template = {}
    template.update(build_template_dictionary("agreements", agreements))
    template.update(build_template_dictionary("as_builts", as_builts))
    template.update(build_template_dictionary("aiannha", aiannha))
    template.update(build_template_dictionary("bia", bia))
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
    template.update(build_template_dictionary("hazards", hazards))
    template.update(build_template_dictionary("historic", historic_cultural))
    template.update(build_template_dictionary("hydric_soils", hydric_soils))
    template.update(build_template_dictionary("land_use", land_use))
    template.update(build_template_dictionary("landfill", landfill))
    template.update(
        build_template_dictionary("marijuana_adult_use", marijuana_adult_use)
    )
    template.update(build_template_dictionary("missing_sidewalks", missing_sidewalks))
    template.update(build_template_dictionary("nhd", nhd))
    template.update(build_template_dictionary("plss", plss))
    template.update(build_template_dictionary("power_gas", power_gas))
    template.update(build_template_dictionary("schools", schools))
    template.update(build_template_dictionary("sewer", sewer))
    template.update(build_template_dictionary("soils", soils))
    template.update(build_template_dictionary("stormwater", stormwater))
    template.update(build_template_dictionary("street_imagery", street_imagery))
    template.update(build_template_dictionary("tax_parcels", tax_parcels))
    template.update(build_template_dictionary("transportation", transportation))
    template.update(build_template_dictionary("water", water))
    template.update(build_template_dictionary("wetlands", wetlands))
    template.update(build_template_dictionary("zoning", zoning))
    return template
    # file_name = os.path.join(TEMPLATE_DIR, "template.json")
    # with open(file_name, "w") as fp:
    #     json.dump(template, fp, sort_keys=True, indent=4)


def build_template_dictionary(template_type, template):
    logging.debug("Building template for %s.", template_type)
    template_dict = {}
    match template_type:
        case "agreements":
            template_dict.update(
                update_layer("agreements", u.agreements_urls, template)
            )
        case "as_builts":
            template_dict.update(update_layer("as_builts", u.as_builts_urls, template))
        case "aiannha":
            template_dict.update(update_layer("aiannha", u.aiannha_urls, template))
        case "bia":
            template_dict.update(update_layers("bia", bia_names, template))
        case "cell_towers":
            template_dict.update(update_layers("cell_towers", [""], template))
        case "city_boundaries":
            template_dict.update(
                update_layer("city_boundaries", u.boundaries_urls, template)
            )
        case "deq_dw_source":
            template_dict.update(
                update_layer(
                    "deq_dw_source", u.deq_drinking_water_source_urls, template
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
            template_dict.update(update_layer("dsl_esh", u.dsl_esh_urls, template))
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
        case "hazards":
            template_dict.update(update_layer("hazards", u.hazards_urls, template))
        case "historic":
            template_dict.update(
                update_layer("historic", u.historic_cultural_areas_urls, template)
            )
        case "hydric_soils":
            template_dict.update(update_layers("hydric_soils", [""], template))
        case "land_use":
            template_dict.update(update_layer("land_use", u.land_use_urls, template))
        case "landfill":
            template_dict.update(update_layer("landfill", u.landfill_urls, template))
        case "marijuana_adult_use":
            template_dict.update(
                update_layer("marijuana_adult_use", u.marijuana_adult_urls, template)
            )
        case "missing_sidewalks":
            template_dict.update(
                update_layer_info(m.missing_sidewalks_layer_names, template)
            )
        case "nhd":
            template_dict.update(update_layer("nhd", u.nhd_urls, template))
        case "plss":
            template_dict.update(update_layers("plss", plss_names, template))
        case "power_gas":
            template_dict.update(update_layer("power_gas", u.power_gas_urls, template))
        case "schools":
            template_dict.update(
                update_layer("schools", u.school_districts_urls, template)
            )
        case "sewer":
            template_dict.update(update_layer("sewer", u.sewer_urls, template))
        case "soils":
            template_dict.update(update_layers("soils", [""], template))
        case "stormwater":
            template_dict.update(
                update_layer("stormwater", u.stormwater_urls, template)
            )
        case "street_imagery":
            template_dict.update(update_layers("street_imagery", [""], template))
        case "tax_parcels":
            template_dict.update(
                update_layer("tax_parcels", u.tax_parcel_urls, template)
            )
        case "transportation":
            template_dict.update(
                update_layer("transportation", u.transportation_urls, template)
            )
        case "water":
            template_dict.update(update_layer("water", u.water_urls, template))
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
