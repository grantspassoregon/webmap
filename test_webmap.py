import os
import random
import time
import pytest
from webmap import webmap as w
from webmap import template as t
from webmap import refs as r
from webmap import maps as m
import arcgis
from arcgis.gis import GIS
from arcgis.mapping import MapServiceLayer
from arcgis.mapping import WebMap
from dotenv import load_dotenv
import logging
import json

# format log messages to include time before message
logging.basicConfig(
    format="%(asctime)s %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
    # filename="sidewalks.log",
    level=logging.DEBUG,
)


load_dotenv()
ARCGIS_USERNAME = os.getenv("ARCGIS_USERNAME")
ARCGIS_PASSWORD = os.getenv("ARCGIS_PASSWORD")
API_KEY = os.getenv("API_KEY")
CLIENT_ID = os.getenv("CLIENT_ID")
PORTAL = "https://grantspassoregon.maps.arcgis.com/"
logging.info("environmental variables loaded")

gis = GIS(
    PORTAL,
    ARCGIS_USERNAME,
    ARCGIS_PASSWORD,
    # api_key=API_KEY,
)
logging.info("Logged in to " + gis.properties.name)
# logging.info("Properties are ")
# logging.info(gis.properties)


def test_build_template():
    t.build_template(gis)


def test_missing_sidewalks():
    test_map = gis.content.get(r.TEST_MISSING_SIDEWALKS)
    template = t.build_template(gis)
    w.clear(test_map)
    m.missing_sidewalks_map(test_map, template)


def test_city_basemap():
    test_map = gis.content.get(r.TEST_CITY_BASEMAP)
    template = t.build_template(gis)
    w.clear(test_map)
    m.city_basemap(test_map, template)


def test_boundaries():
    test_map = gis.content.get(r.TEST_BOUNDARIES)
    template = t.build_template(gis)
    w.clear(test_map)
    m.boundaries(test_map, template)


# def test_new():
#
#     # build test map
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
#     wm.save(item_props, folder="tests")


# def missing_sidewalks_layers():
