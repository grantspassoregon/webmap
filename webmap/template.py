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

# city_boundaries_names = [
#     "city_limits",
#     "ugb",
#     "council_wards",
#     "urban_reserve",
#     "cardinals",
#     "cmaq",
#     "gpid",
#     "county_line",
# ]

school_names = [
    "locations",
    "grounds",
    "walking",
    "hazard",
    "buffer",
    "elementary",
    "middle",
    "high",
    "district_7",
    "three_rivers",
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
    aiannha = gis.content.get(r.TEMPLATE_AIANNHA)
    bia = gis.content.get(r.TEMPLATE_BIA)
    city_boundaries = gis.content.get(r.TEMPLATE_CITY_BOUNDARIES)
    missing_sidewalks = gis.content.get(r.TEMPLATE_MISSING_SIDEWALKS)
    plss = gis.content.get(r.TEMPLATE_PLSS)
    schools = gis.content.get(r.TEMPLATE_SCHOOLS)

    template = {}
    template.update(build_template_dictionary("aiannha", aiannha))
    template.update(build_template_dictionary("bia", bia))
    template.update(build_template_dictionary("city_boundaries", city_boundaries))
    template.update(build_template_dictionary("missing_sidewalks", missing_sidewalks))
    template.update(build_template_dictionary("plss", plss))
    template.update(build_template_dictionary("schools", schools))
    return template
    # file_name = os.path.join(TEMPLATE_DIR, "template.json")
    # with open(file_name, "w") as fp:
    #     json.dump(template, fp, sort_keys=True, indent=4)


def build_template_dictionary(template_type, template):
    logging.debug("Building template for %s.", template_type)
    template_dict = {}
    match template_type:
        case "aiannha":
            template_dict.update(update_layer("aiannha", u.aiannha_urls, template))
        case "bia":
            template_dict.update(update_layers("bia", bia_names, template))
        # case "city_boundaries":
        #     template_dict.update(
        #         update_layers("city_boundaries", city_boundaries_names, template)
        #     )
        case "city_boundaries":
            template_dict.update(
                update_layer("city_boundaries", u.boundaries_urls, template)
            )
        case "missing_sidewalks":
            template_dict.update(
                update_layer_info(m.missing_sidewalks_layer_names, template)
            )
        case "plss":
            template_dict.update(update_layers("plss", plss_names, template))
        case "schools":
            template_dict.update(
                update_layer("schools", u.school_districts_urls, template)
                # update_layers("schools", school_names, template)
            )

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
        new_data.update({popup_name[i]: ref_list[i]["popupInfo"]})
        new_data.update({label_name[i]: ref_list[i]["layerDefinition"]})

    return new_data
