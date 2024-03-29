import os
import random
import time
import pytest
from webmap import webmap as w
from webmap import template as t
from webmap import refs as r
from webmap import maps as m
from webmap import search as s
import arcgis
from arcgis.gis import GIS
from arcgis.mapping import MapServiceLayer
from arcgis.mapping import WebMap
from dotenv import load_dotenv
import logging
import pprint

# format log messages to include time before message
logging.basicConfig(
    format="%(asctime)s %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
    # filename="sidewalks.log",
    level=logging.INFO,
)


load_dotenv()
ARCGIS_USERNAME = os.getenv("ARCGIS_USERNAME")
ARCGIS_PASSWORD = os.getenv("ARCGIS_PASSWORD")
API_KEY = os.getenv("API_KEY")
CLIENT_ID = os.getenv("CLIENT_ID")
PORTAL = "https://grantspassoregon.maps.arcgis.com/"
INTERNAL = os.getenv("INTERNAL")
INTERNAL_ID = os.getenv("INTERNAL_ID")
logging.info("environmental variables loaded")

gis = GIS(
    PORTAL,
    ARCGIS_USERNAME,
    ARCGIS_PASSWORD,
    # api_key=API_KEY,
)
internal = GIS(
    PORTAL,
    ARCGIS_USERNAME,
    ARCGIS_PASSWORD,
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


def test_city_basemap(public=False):
    test_map = gis.content.get(r.TEST_CITY_BASEMAP)
    template = t.build_template(gis)
    w.clear(test_map)
    m.city_basemap(test_map, template, internal, public)


def test_build(map, portal, gis, public=False):
    test_map = portal.content.get(map)
    template = t.build_template(gis)
    w.clear(test_map)
    m.city_basemap(test_map, template, portal, public)


def test_business_map():
    test_map = gis.content.get(r.STABLE_BUSINESSES)
    template = t.build_template(gis)
    w.clear(test_map)
    m.business_layers(test_map, template, True)


def test_editing_map(public=False):
    test_map = gis.content.get(r.TEST_CITY_BASEMAP)
    template = t.build_template(gis)
    w.clear(test_map)
    m.editing_map(test_map, template, internal, public)


def test_editing_subset(public=False):
    test_map = gis.content.get(r.TEST_CITY_BASEMAP)
    template = t.build_template(gis)
    w.clear(test_map)
    m.address_editing_layers(test_map, template, internal, True)
    m.sketch_layers(test_map, template, internal, public, True)


def test_search(map):
    s.add_search(map)


def test_map_def(map):
    pp = pprint.PrettyPrinter(width=4)
    test_map = gis.content.get(map)
    map_def = test_map.get_data()
    logging.info(pp.pprint(map_def["operationalLayers"]))


def test_web_viewer(public=False):
    test_map = gis.content.get(r.TEST_CITY_BASEMAP)
    template = t.build_template(gis)
    w.clear(test_map)
    m.web_viewer(test_map, template, internal, public)


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
