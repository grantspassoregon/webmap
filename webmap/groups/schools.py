from webmap import webmap as w
from webmap import urls as u
from webmap import template as t
from arcgis.mapping import MapServiceLayer
import logging


def schools(base, template, basemap=False, urls=u.school_districts_group):
    """
    Grants Pass District 7 and Three Rivers School District boundaries.

    :param base: Group layer definition or map project target for layers.
    :param template: Reference template for map layers.
    :param basemap: Indicates whether appending to group layer or project map.
    :type basemap: Boolean
    :return: Updates group layer definition with layers.
    :rtype: None
    """
    popup_names = t.layer_tags("schools_wv", urls, "_popup")
    label_names = t.layer_tags("schools_wv", urls, "_label")

    map_name = "School Districts"
    map_group = w.group_layer(map_name)
    for index, url in enumerate(urls):
        map_lyr = MapServiceLayer(url)
        fc = w.feature_class(map_lyr, 0.5)
        fc.update({"visibility": False})
        if fc["title"] == "Schools":
            fc.update({"title": "School Locations"})
        if fc["title"] == "GP Area School Properties":
            fc.update({"title": "School Grounds"})
        if index == 2:
            fc.update({"title": "High School Zones"})
        if index == 3:
            fc.update({"title": "Middle School Zones"})
        if index == 4:
            fc.update({"title": "Elementary School Zones"})
        if fc["title"] == "School Zone":
            fc.update({"title": "School Zones"})
        if fc["title"] == "District 7":
            fc.update({"title": "District 7 Boundary"})
        if fc["title"] == "3 Rivers School District":
            fc.update({"title": "Three Rivers District Boundary"})
        if popup_names[index] in template:
            fc.update({"popupInfo": template[popup_names[index]]})
        if label_names[index] in template:
            fc.update({"layerDefinition": template[label_names[index]]})
        map_group["layers"].append(fc)
    logging.info("Appending layers to %s definition.", map_name)
    w.add_group(base, map_group, basemap)
