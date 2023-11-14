from webmap import webmap as w
from webmap import urls as u
from webmap import template as t
from webmap.groups import plss as p
from arcgis.mapping import MapServiceLayer
import logging


def boundaries(base, template, basemap=False, urls=u.boundaries_group):
    """
    Regulatory boundaries for the City of Grants Pass.

    :param group_lyr: Group layer definition or project map target for layers.
    :param template: Reference template for map layers.
    :param basemap: Indicates whether appending to group layer or project map.
    :type basemap: Boolean
    :return: Updates group layer definition with layers.
    :rtype: None
    """
    popup_names = t.layer_tags("boundaries_group", urls, "_popup")
    label_names = t.layer_tags("boundaries_group", urls, "_label")

    map_name = "Boundaries"
    map_group = w.group_layer(map_name)
    for index, url in enumerate(urls):
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
        if fc["title"] == "JoCo_Boundary":
            fc.update({"title": "Josephine County Line"})
        if popup_names[index] in template:
            fc.update({"popupInfo": template[popup_names[index]]})
        if label_names[index] in template:
            fc.update({"layerDefinition": template[label_names[index]]})
        map_group["layers"].append(fc)
    p.plss(map_group, template)
    logging.info("PLSS layers added to %s.", map_name)
    logging.info("Appending layers to %s definition.", map_name)
    w.add_group(base, map_group, basemap)
