from webmap import webmap as w
from webmap import maps as m
from webmap import urls as u
from webmap import template as t
from arcgis.mapping import MapServiceLayer
import logging


def transportation_layers(
    base, template, internal, basemap=False, urls=u.transportation_group
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
    popup_names = t.layer_tags("transportation_wv", urls, "_popup")
    label_names = t.layer_tags("transportation_wv", urls, "_label")

    group_name = "Transportation"
    map_group = w.group_layer(group_name)
    streets_group = w.group_layer("Streets Group")
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
        if index == 5:
            fc.update({"title": "Streets (County)"})
        if popup_names[index] in template:
            fc.update({"popupInfo": template[popup_names[index]]})
        if label_names[index] in template:
            fc.update({"layerDefinition": template[label_names[index]]})
        logging.debug("Appending %s to %s layer.", fc["title"], group_name)
        if index in list(range(1, 8)):
            streets_group["layers"].append(fc)
        elif index in list(range(8, 13)):
            alt_group["layers"].append(fc)
        elif index in list(range(13, 18)):
            fixtures_group["layers"].append(fc)
        else:
            map_group["layers"].append(fc)
    m.parking_layers(map_group, template)
    m.traffic_layers(map_group, template)
    logging.info("Traffic reports added to %s.", group_name)
    map_group["layers"].append(streets_group)
    logging.info("Streets added to %s.", group_name)
    map_group["layers"].append(alt_group)
    map_group["layers"].append(fixtures_group)
    logging.info("Appending layers to %s definition.", group_name)
    w.add_group(base, map_group, basemap)
