from webmap import webmap as w
from webmap import maps as m
from webmap import urls as u
from webmap import template as t
from webmap.groups import fema as f
from arcgis.mapping import MapServiceLayer
import logging


def environment(base, template, basemap=False):
    """
    Environmental hazards layers for the City of Grants Pass, Oregon.

    :param base: Group layer definition or map project target for layers.
    :param template: Reference template for map layers.
    :param basemap: Indicates whether appending to group layer or project map.
    :type basemap: Boolean
    :return: Updates group layer definition with layers.
    :rtype: None
    """
    # features
    group_name = "Environment"
    map_group = w.group_layer(group_name)
    m.contours_layers(map_group, template)
    logging.info("Topographic contours added to %s.", group_name)
    w.add_single_layer(
        "wetlands",
        u.dsl_wetlands_url,
        map_group,
        template,
        title="Wetlands (DSL)",
        visibility=False,
    )
    logging.info("Wetland inventory (DSL) added to %s.", group_name)
    m.dsl_esh_layers(map_group, template)
    logging.info("Essential salmon habitat (DSL) added to %s.", group_name)
    m.deq_drinking_water_source_layers(map_group, template)
    logging.info("Drinking water source areas (DEQ) added to %s.", group_name)
    w.add_single_layer(
        "features0",
        u.features_urls[1],
        map_group,
        template,
        title="20ft Stream Buffer",
        visibility=False,
    )
    logging.info("Stream buffer added to %s.", group_name)

    # Hazards
    popup_names = t.layer_tags("hazards", u.hazards_urls, "_popup")
    label_names = t.layer_tags("hazards", u.hazards_urls, "_label")
    url_list = u.hazards_urls

    f.fema(map_group, template)
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
