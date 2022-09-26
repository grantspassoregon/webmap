from webmap import maps as m
from webmap import refs as r


def build_template(gis):
    """
    Build template dictionary from template maps.  The template stores layer
    definition information (style, labels, whether popups are enabled, etc.)
    referenced by the package when constructing a new map.

    :return: Updates the template.json file.
    """
    missing_sidewalks = gis.content.get(r.TEMPLATE_MISSING_SIDEWALKS)

    template = {}
    template.update(build_template_dictionary("missing_sidewalks", missing_sidewalks))
    return template
    # file_name = os.path.join(TEMPLATE_DIR, "template.json")
    # with open(file_name, "w") as fp:
    #     json.dump(template, fp, sort_keys=True, indent=4)


def build_template_dictionary(template_type, template):
    template_dict = {}
    match template_type:
        case "missing_sidewalks":
            template_dict.update(
                update_layer_info(m.missing_sidewalks_layer_names, template)
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
        new_data.update({popup_name[i]: ref_list[i]["popupInfo"]})
        new_data.update({label_name[i]: ref_list[i]["layerDefinition"]})

    return new_data
