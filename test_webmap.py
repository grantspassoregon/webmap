import pytest
from webmap import webmap as w
from webmap import template as t
from webmap import refs as r
from arcgis.gis import GIS
import random
from arcgis.mapping import MapServiceLayer
from arcgis.mapping import WebMap
import time

# from dotenv import load_dotenv

# load_dotenv()
# ARCGIS_USERNAME = os.getenv("ARCGIS_USERNAME")
# ARCGIS_PASSWORD = os.getenv("ARCGIS_PASSWORD")


# def test_login():
#     print("Login info: " + gis.properties.name)
#     wm = WebMap()
#     item_props = {}
#     item_props.update({"title": "test_missing_sidewalks"})
#     item_props.update(
#         {"description": "Test web map for streets missing required sidewalks."}
#     )
#     item_props.update({"snippet": "For testing purposes. Do not use."})
#     item_props.update({"tags": ["planning", "test"]})
#     item_props.update(
#         {"serviceItemId": w.create_layer_id(random.randint(10000, 99999))}
#     )
# fails, no owner
# wm.save(item_props)


def test_build_template():
    t.build_template()


def test_new():

    # build test map
    wm = WebMap()
    item_props = {}
    item_props.update({"title": "test_missing_sidewalks"})
    item_props.update(
        {"description": "Test web map for streets missing required sidewalks."}
    )
    item_props.update({"snippet": "For testing purposes. Do not use."})
    item_props.update({"tags": ["planning", "test"]})
    item_props.update(
        {"serviceItemId": w.create_layer_id(random.randint(10000, 99999))}
    )
    wm.save(item_props, folder="tests")


# def missing_sidewalks_layers():
