from webmap import webmap as w
from webmap import urls as u
from webmap import template as t
from arcgis.mapping import MapServiceLayer
import logging


def water(base, template, internal, basemap=False, urls=u.water_wv):
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
    popup_names = t.layer_tags("water_wv", urls, "_popup")
    label_names = t.layer_tags("water_wv", urls, "_label")

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
        if popup_names[index] in template:
            fc.update({"popupInfo": template[popup_names[index]]})
        if label_names[index] in template:
            fc.update({"layerDefinition": template[label_names[index]]})
        logging.debug("Appending %s to %s layer.", fc["title"], group_name)
        map_group["layers"].append(fc)
    logging.info("Appending layers to %s definition.", group_name)
    w.add_group(base, map_group, basemap)
