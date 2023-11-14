from webmap import webmap as w
from webmap import maps as m
from webmap import urls as u
from webmap import template as t
from webmap.groups import historic as h
from arcgis.mapping import MapServiceLayer
import logging


def planning(base, template, public, basemap=False, urls=u.planning_group):
    """
    Zoning, historic/cultural areas and miscellaneous planning layers for City of Grants Pass.

    :param base: Group layer definition or map project target for layers.
    :param template: Reference template for map layers.
    :param basemap: Indicates whether appending to group layer or project map.
    :type basemap: Boolean
    :return: Updates group layer definition with layers.
    :rtype: None
    """
    popup_names = t.layer_tags("planning", urls, "_popup")
    label_names = t.layer_tags("planning", urls, "_label")

    group_name = "Planning"
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
    m.zoning_layers(map_group, template)
    logging.info("Zoning layers added to %s.", group_name)
    m.marijuana_adult_use_layers(map_group, template)
    logging.info("Marijuana and adult use layers added to %s.", group_name)
    if not public:
        m.marijuana_permitting_layers(map_group, template)
        logging.info("Marijuana business permitting layers added to %s.", group_name)
    m.agreements_layers(map_group, template)
    logging.info("Agreements and financial layers added to %s.", group_name)
    h.historic(map_group, template)
    logging.info("Historic/cultural layers added to %s.", group_name)
    logging.info("Appending layers to %s definition.", group_name)
    w.add_group(base, map_group, basemap)
