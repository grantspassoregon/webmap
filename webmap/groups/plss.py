from webmap import webmap as w
from webmap import urls as u
from webmap import template as t
from arcgis.mapping import MapServiceLayer


def plss(base, template, basemap=False):
    """
    PLSS layers from BLM.

    :param group_lyr: Group layer definition target for layers.
    :param template: Reference template for map layers.
    :param basemap: Indicates whether appending to group layer or project map.
    :type basemap: Boolean
    :return: Updates group layer definition with layers.
    :rtype: None
    """
    popup_names = t.layer_names("plss", t.plss_names, "_popup")
    label_names = t.layer_names("plss", t.plss_names, "_label")
    url_list = u.plss_urls

    map_group = w.group_layer("PLSS")
    for index, url in enumerate(url_list):
        map_lyr = MapServiceLayer(url)
        fc = w.feature_class(map_lyr, 0.5)
        fc.update({"visibility": False})
        if popup_names[index] in template:
            fc.update({"popupInfo": template[popup_names[index]]})
        if label_names[index] in template:
            fc.update({"layerDefinition": template[label_names[index]]})
        map_group["layers"].append(fc)
    w.add_group(base, map_group, basemap)
