import random
import string
import json
from arcgis.mapping import MapServiceLayer
from arcgis.mapping import WebMap


def define_layer_names(urls, stub):
    names = []
    for i in range(0, len(urls)):
        names.append(stub + "_" + str(i))
    return names


def add_single_layer(key_name, url, group_lyr, template, title=None, visibility=None):
    """
    Add single feature layer to parent group layer.

    :param key_name: Base name for template definition reference.
    :type key_name: Text string
    :param url: Url address of feature service layer to add.
    :type url: Text string (must be valid url).
    :param group_lyr: Group layer definition target for layers.
    :type group_lyr: Dictionary
    :param template: Template dictionary holding layer definitions for the map.
    :type template: Dictionary
    :param title: Optional title to assign to the added layer.
    :type title: Text string
    :param visibility: Optional level of transparency to assign to new layer.
    :type visibility: Float ranging from 0-1.
    :return: Updates group layer definition with new layer.
    """
    popup_name = key_name + "_popup"
    label_name = key_name + "_label"
    lyr = MapServiceLayer(url)
    fc = feature_class(lyr, 0.5, title)
    if visibility != None:
        fc.update({"visibility": visibility})
    if popup_name in template:
        fc.update({"popupInfo": template[popup_name]})
    if label_name in template:
        fc.update({"layerDefinition": template[label_name]})
    group_lyr["layers"].append(fc)


def layer_urls(item):
    """List service layer urls.

    :param item: Service with target layers.
    :type kind: ArcGISFeatureLayer
    :return: A list of urls for layers in the service.
    :rtype: list[str]
    """
    urls = []
    for lyr in item.layers:
        urls.append(lyr.url)
    return urls


def create_layer_id(layerIndex):
    """
    Generate random ids for layers. Copied verbatim from https://community.esri.com/t5/arcgis-api-for-python-questions/python-api-add-group-layer-to-webmap/td-p/1112126.

    To build a web map from a published service, we generate feature layers pointed to each service. Each feature layer requires a unique layer id, produced by this function.

    :param layerIndex: Layer index number.
    :return: A randomized string to serve as a unique id.
    :rtype: str
    """
    return (
        "".join(random.choices(string.ascii_lowercase + string.digits, k=11))
        + "-layer-"
        + str(layerIndex)
    )


def feature_class(layer, opacity=1.0, title=None):
    """
    Generic feature class wrapper for layer data.

    :param layer: Source for feature layer.
    :type layer: MapServiceLayer
    :param opacity: Opacity of feature layer.
    :type opacity: float
    :return: Feature layer data for map service layer.
    """
    fc_dict = {}
    fc_dict.update({"id": create_layer_id(random.randint(10000, 99999))})
    fc_dict.update({"url": layer.url})
    if title != None:
        fc_dict.update({"title": title})
    else:
        fc_dict.update({"title": layer.properties.name})
    fc_dict.update({"layerType": "ArcGISFeatureLayer"})
    fc_dict.update({"opacity": opacity})
    return fc_dict


def group_layer(title):
    """
    Generates an empty group layer with a specified title.

    :param title: The title of the layer as shown in the legend.
    :return: A json dictionary for a group layer.
    """
    group_dict = {}
    group_dict.update({"id": create_layer_id(random.randint(10000, 99999))})
    group_dict.update({"layers": []})
    group_dict.update({"layerType": "GroupLayer"})
    group_dict.update({"title": title})
    return group_dict


def clear(item):
    map_item = WebMap(item)
    map_layers = map_item.layers
    for lyr in map_layers:
        map_item.remove_layer(lyr)
    map_item.update()
