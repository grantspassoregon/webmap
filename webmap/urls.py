def expand_urls(stub, rng):
    """
    Generate list of urls over range index given a service stub.

    :param stub: Url base string for map service.
    :param rng: List of numbers generated by range() call.
    :return: List of urls beginning in stub and ending in rng values.
    """
    urls = []
    for i in rng:
        urls.append(stub + str(i))
    return urls


missing_sidewalks_base = "https://services2.arcgis.com/pc4beVTMEhYHqerq/arcgis/rest/services/missing_sidewalks_service/FeatureServer/"
# read this in reverse so it matches the order of operational layers in the .get_data() method
# and the operational layers when building the template
url_range = [11, 10, 9, 8, 7, 14, 15, 16, 17, 18, 19, 20, 0, 1, 2, 3, 4, 5, 6]

missing_sidewalks_urls = expand_urls(missing_sidewalks_base, url_range)

# regulatory boundaries

plss_base = "https://gis.blm.gov/arcgis/rest/services/Cadastral/BLM_Natl_PLSS_CadNSDI/MapServer/"
url_range = list(range(3, -1, -1))
plss_urls = expand_urls(plss_base, url_range)

# bia tribal lands

bia_base = "https://arcgis.water.nv.gov/arcgis/rest/services/BaseLayers/BIA_Boundaries/MapServer/"
url_range = [1, 0]
bia_urls = expand_urls(bia_base, url_range)

# aiannha tigerweb indian lands

aiannha_base = (
    "https://tigerweb.geo.census.gov/arcgis/rest/services/Census2020/AIANNHA/MapServer/"
)
url_range = [10, 9, 8, 4, 3, 2, 1]
aiannha_urls = expand_urls(aiannha_base, url_range)

# library district
library_url = "https://gis.co.josephine.or.us/arcgis/rest/services/Assessor/Library_District/MapServer/2"
library_def = {
    "id": "Library_District_4708",
    "layerType": "ArcGISMapServiceLayer",
    "opacity": 0.5,
    "title": "Library District",
    "url": "https://gis.co.josephine.or.us/arcgis/rest/services/Assessor/Library_District/MapServer",
    "visibility": False,
}

# city boundaries

boundaries_base = "https://services2.arcgis.com/pc4beVTMEhYHqerq/arcgis/rest/services/regulatory_boundaries/FeatureServer/"
# boundaries_base = "https://gisserver.grantspassoregon.gov/server/rest/services/city_boundaries/MapServer/"
# urban_reserve_url = "https://services2.arcgis.com/pc4beVTMEhYHqerq/arcgis/rest/services/urban_reserve/FeatureServer/0"
url_range = list(range(7, -1, -1))
boundaries_urls = expand_urls(boundaries_base, url_range)
# boundaries_urls[4] = urban_reserve_url
# boundaries_urls.insert(1, library_url)

# school districts

# josephine county
school_locations = "https://gis.co.josephine.or.us/arcgis/rest/services/Planning/SchoolLocatons/MapServer/0"
# elementary schools
# school_zones = "https://gis.co.josephine.or.us/arcgis/rest/services/Planning/School_Zones/MapServer/0"
school_zones = "https://gis.co.josephine.or.us/arcgis/rest/services/Boundary/School_Zones/MapServer/0"

# city schools data
school_districts_base = "https://services2.arcgis.com/pc4beVTMEhYHqerq/arcgis/rest/services/school_district/FeatureServer/"
url_range = list(range(5, -1, -1))
school_districts_urls = expand_urls(school_districts_base, url_range)
# elementary, middle and high school zones
school_districts_urls.insert(2, school_zones)
school_districts_urls.insert(2, school_zones)
school_districts_urls.insert(2, school_zones)
school_districts_urls.append(school_locations)


# addresses
county_addresses_url = "https://services6.arcgis.com/Hf6u9DI4oZH2QTg9/arcgis/rest/services/Josephine_County_Site_Address/FeatureServer/0"
ecso911_addresses_url = "https://gis.ecso911.com/server/rest/services/Hosted/JoCo_SiteAddress/FeatureServer/0"

# address editing
address_editing_url = "https://gisserver.grantspassoregon.gov/server/rest/services/land_use/FeatureServer/0"
address_verification_url = "https://gisserver.grantspassoregon.gov/server/rest/services/Editing/address_verification/FeatureServer/0"
address_editing_urls = [address_editing_url, address_verification_url]

# land use
land_use_base = "https://services2.arcgis.com/pc4beVTMEhYHqerq/arcgis/rest/services/land_use/FeatureServer/"
# land_use_base = (
#     "https://gisserver.grantspassoregon.gov/server/rest/services/land_use/MapServer/"
# )
url_range = [2, 1, 0]
land_use_urls = expand_urls(land_use_base, url_range)
land_use_urls.insert(2, ecso911_addresses_url)


# tax parcels
county_parcels_url = "https://gis.co.josephine.or.us/arcgis/rest/services/Assessor/Assessor_Taxlots/MapServer/0"
# city_parcels_url = "https://services2.arcgis.com/pc4beVTMEhYHqerq/arcgis/rest/services/taxlots/FeatureServer/0"
city_parcels_url = (
    "https://gisserver.grantspassoregon.gov/server/rest/services/taxlots/MapServer/0"
)
assessment_maps_url = "https://services2.arcgis.com/pc4beVTMEhYHqerq/arcgis/rest/services/land_use/FeatureServer/3"
# assessment_maps_url = (
#     "https://gisserver.grantspassoregon.gov/server/rest/services/land_use/MapServer/3"
# )
tax_code_url = (
    "https://gis.co.josephine.or.us/arcgis/rest/services/Assessor/Codes_Map/MapServer/7"
)
tax_parcel_urls = [
    tax_code_url,
    assessment_maps_url,
    county_parcels_url,
    city_parcels_url,
]


# hazards

# fema
fema_flood_base = (
    "https://hazards.fema.gov/gis/nfhl/rest/services/public/NFHL/MapServer/"
)
url_range = [
    31,
    30,
    26,
    13,
    12,
    11,
    10,
    9,
    8,
    6,
    4,
    25,
    28,
    27,
    19,
    5,
    32,
    7,
    24,
    18,
    15,
    29,
    23,
    16,
    14,
    20,
    17,
    22,
    34,
    1,
    3,
    0,
]
fema_flood_urls = expand_urls(fema_flood_base, url_range)

fema_nfhlwms_stub = (
    "https://hazards.fema.gov/gis/nfhl/rest/services/public/NFHLWMS/MapServer/"
)
# fema_nfhlwms_rng = range(1, 33)
fema_nfhl_wms_urls = expand_urls(fema_nfhlwms_stub, url_range)

# forest service
# wildfire housing list
fs_wildfire_housing_url = "https://apps.fs.usda.gov/fsgisx01/rest/services/RDW_Wildfire/RMRS_WRC_HousingUnitRisk/ImageServer"
# wildfire potential hazard
fs_wildfire_potential_url = "https://apps.fs.usda.gov/fsgisx01/rest/services/RDW_Wildfire/RMRS_WRC_WildfireHazardPotential/ImageServer"


# environmental features

features_base = "https://gisserver.grantspassoregon.gov/server/rest/services/environmental_features/MapServer/"
url_range = [1, 0]
features_urls = expand_urls(features_base, url_range)

# dsl
# dsl wetlands
dsl_wetlands_url = "https://maps.dsl.state.or.us/arcgis/rest/services/NWI/MapServer/0"

# Soils
dsl_hydric_soils_url = (
    # "https://maps.dsl.state.or.us/arcgis/rest/services/SwiHydric/MapServer/0"
    "https://maps.dsl.state.or.us/arcgis/rest/services/SWISoil23/MapServer/0"
)

# esri usa soils map units
nrcs_soils_url = "https://landscape11.arcgis.com/arcgis/rest/services/USA_Soils_Map_Units/featureserver/0"

soils_urls = [dsl_hydric_soils_url, nrcs_soils_url]

nrcs_soils_def = {
    "id": "184814d8dc6-layer-2",
    "itemId": "06e5fd61bdb6453fb16534c676e1c9b9",
    "layerType": "ArcGISFeatureLayer",
    "opacity": 0.5,
    "title": "Soils Map Units (NRCS)",
    "url": "https://landscape11.arcgis.com/arcgis/rest/services/USA_Soils_Map_Units/featureserver/0",
    "visibility": False,
}

# Fish & Wildlife NWI Wetlands
# fw_nwi_wetlands = (
#     "https://www.fws.gov/wetlandsmapservice/rest/services/Wetlands/MapServer/0"
# )

# NRCS Hydric Soils
# nrcs_hydric_soils = "https://gisdata.dsl.state.or.us/arcgis/rest/services/Maps/SWI_HydricSoil_2020_B/MapServer/0"
# nrcs_hydric_soils = (
#     "https://maps.dsl.state.or.us/arcgis/rest/services/HydricSoil/MapServer/0"
# )

# dogami lidar
dogami_be_def = {
    "id": "DIGITAL_TERRAIN_MODEL_MOSAIC_HS_9457",
    "layerType": "ArcGISImageServiceLayer",
    "opacity": 1,
    "title": "Hillshade Bare Earth (DOGAMI)",
    "url": "https://gis.dogami.oregon.gov/arcgis/rest/services/lidar/DIGITAL_TERRAIN_MODEL_MOSAIC_HS/ImageServer",
    "visibility": False,
}

dogami_hh_def = {
    "id": "DIGITAL_SURFACE_MODEL_MOSAIC_HS_4921",
    "layerType": "ArcGISImageServiceLayer",
    "opacity": 1,
    "title": "Hillshade Highest Hits (DOGAMI)",
    "url": "https://gis.dogami.oregon.gov/arcgis/rest/services/lidar/DIGITAL_SURFACE_MODEL_MOSAIC_HS/ImageServer",
    "visibility": False,
}

# national hyrdo (NHDPlus)
nhd_base = "https://hydro.nationalmap.gov/arcgis/rest/services/NHDPlus_HR/MapServer/"
url_range = list(range(12, -1, -1))
nhd_urls = expand_urls(nhd_base, url_range)

# owrd wells
wells_base = "https://arcgis.wrd.state.or.us/arcgis/rest/services/dynamic/wl_well_logs_themes_WGS84/MapServer/"
# well characteristics
url_range = list(range(31, 20, -1))
# type of work for geotechnical holes
url_range.extend(list(range(18, 12, -1)))
# type of work for Water/Monitor wells
url_range.extend(list(range(11, 5, -1)))
# type of log
url_range.extend(list(range(4, 1, -1)))
wells_urls = expand_urls(wells_base, url_range)

wells_def = {
    "id": "wl_well_logs_themes_WGS84_980",
    "layerType": "ArcGISMapServiceLayer",
    "opacity": 0.5,
    "title": "Wells (ORWD)",
    "url": "https://arcgis.wrd.state.or.us/arcgis/rest/services/dynamic/wl_well_logs_themes_WGS84/MapServer",
    "visibility": False,
}

# deq
# drinking water sources
deq_drinking_water_source_base = "https://arcgis.deq.state.or.us/arcgis/rest/services/DEQ_Services/DrinkingWaterTestService/MapServer/"
url_range = [7, 6, 4, 3, 2]
deq_drinking_water_source_urls = expand_urls(deq_drinking_water_source_base, url_range)


deq_gw_2yrtot_def = {
    "id": "DrinkingWaterTestService_2020",
    "layerType": "ArcGISMapServiceLayer",
    "layers": [
        {
            "defaultVisibility": True,
            "disablePopup": False,
            "id": 0,
            "layerDefinition": {
                "drawingInfo": {"showLabels": True, "transparency": 0},
                "source": {"mapLayerId": 0, "type": "mapLayer"},
            },
            "maxScale": 0,
            "minScale": 0,
            "name": "Groundwater " "Drinking " "Water " "Source " "Area " "outlines",
            "parentLayerId": -1,
            "showLegend": True,
            "subLayerIds": [1],
        },
        {
            "defaultVisibility": True,
            "disablePopup": False,
            "id": 1,
            "layerDefinition": {
                "drawingInfo": {
                    "renderer": {
                        "description": "",
                        "label": "",
                        "symbol": {
                            "color": [0, 0, 0, 0],
                            "outline": {
                                "color": [255, 255, 0, 255],
                                "style": "esriSLSSolid",
                                "type": "esriSLS",
                                "width": 1.5,
                            },
                            "style": "esriSFSSolid",
                            "type": "esriSFS",
                        },
                        "type": "simple",
                    },
                    "showLabels": True,
                    "transparency": 0,
                },
                "source": {"mapLayerId": 1, "type": "mapLayer"},
            },
            "maxScale": 0,
            "minScale": 0,
            "name": "2yrTOT",
            "parentLayerId": 0,
            "showLegend": True,
        },
    ],
    "opacity": 1,
    "title": "DrinkingWaterTestService",
    "url": "https://arcgis.deq.state.or.us/arcgis/rest/services/DEQ_Services/DrinkingWaterTestService/MapServer",
    "visibility": True,
    "visibleLayers": [0, 1],
}

# drinking water protection
# deq_drinking_water_protection_base = "https://arcgis.deq.state.or.us/arcgis/rest/services/WQ/DrinkingWaterProtectionPCS/MapServer/"
# url_range = list(range(31, 22, -1))
# url_range.extend(list(range(21, -1, -1)))
# deq_drinking_water_protection_urls = expand_urls(
#     deq_drinking_water_protection_base, url_range
# )

deq_pcs_def = {
    "id": "DrinkingWaterProtectionPCS_946",
    "layerType": "ArcGISMapServiceLayer",
    "opacity": 0.5,
    "title": "Drinking Water Protection (DEQ PCS)",
    "url": "https://arcgis.deq.state.or.us/arcgis/rest/services/WQ/DrinkingWaterProtectionPCS/MapServer",
    "visibility": False,
}

# surface water impaired
deq_hydro_2022_base = (
    "https://arcgis.deq.state.or.us/arcgis/rest/services/WQ/WQL_Hydro_2022/MapServer/"
)
url_range = [2, 1, 0]
deq_hydro_2022_urls = expand_urls(deq_hydro_2022_base, url_range)


# dsl essential salmon habitat
dsl_esh_base = (
    "https://maps.dsl.state.or.us/arcgis/rest/services/EshAndSpecies/MapServer/"
)
url_range = list(range(9, 0, -1))
dsl_esh_urls = expand_urls(dsl_esh_base, url_range)


# environmental hazards
hazards_base = "https://gisserver.grantspassoregon.gov/server/rest/services/environmental_hazards/MapServer/0"
url_range = list(range(3, -1, -1))
hazards_urls = expand_urls(hazards_base, url_range)


# transportation
odot_roads_url = "https://gis.odot.state.or.us/arcgis1006/rest/services/transgis/catalog/MapServer/164"
odot_construction_url = "https://services.arcgis.com/uUvqNMGPm7axC2dD/ArcGIS/rest/services/ODOT_Traffic_Construction/FeatureServer/0"
odot_traffic_url = "https://services.arcgis.com/uUvqNMGPm7axC2dD/ArcGIS/rest/services/ODOT_Traffic_Incidents/FeatureServer/0"
# odot_railroad_url = "https://services.arcgis.com/uUvqNMGPm7axC2dD/ArcGIS/rest/services/railroadsgb/FeatureServer/0"
odot_railroad_url = "https://gis.odot.state.or.us/arcgis1006/rest/services/transgis/catalog/MapServer/143"

county_owned_roads_url = "https://gis.co.josephine.or.us/arcgis/rest/services/Public_Works/Josephine_County_Owned_Roads/MapServer/0"
county_state_owned_roads_url = "https://gis.co.josephine.or.us/arcgis/rest/services/Public_Works/State_jurisdiction/MapServer/0"
county_bridges_url = (
    "https://gis.co.josephine.or.us/arcgis/rest/services/Bridges/MapServer/0"
)

# ecso911 data
county_roads_url = (
    "https://gis.ecso911.com/server/rest/services/Hosted/Centerline/FeatureServer/0"
)

ecso911_ems_url = (
    "https://gis.ecso911.com/server/rest/services/Hosted/EMS_Polygon/FeatureServer/0"
)
ecso911_fire_url = (
    "https://gis.ecso911.com/server/rest/services/Hosted/Fire_Polygon/FeatureServer/0"
)
ecso911_law_url = (
    "https://gis.ecso911.com/server/rest/services/Hosted/Law_Polygon/FeatureServer/0"
)


# forest service wildfire
fs_wildfire_potential_def = {
    "id": "RMRS_WRC_WildfireHazardPotential_5283",
    "layerType": "ArcGISImageServiceLayer",
    "opacity": 0.5,
    "title": "Wildfire Hazard Potential (FS)",
    "url": "https://apps.fs.usda.gov/fsgisx01/rest/services/RDW_Wildfire/RMRS_WRC_WildfireHazardPotential/ImageServer",
    "visibility": False,
}

fs_wildfire_housing_def = {
    "id": "RMRS_WRC_HousingUnitRisk_1007",
    "layerType": "ArcGISImageServiceLayer",
    "opacity": 0.5,
    "title": "Wildfire Housing Unit Risk (FS)",
    "url": "https://apps.fs.usda.gov/fsgisx01/rest/services/RDW_Wildfire/RMRS_WRC_HousingUnitRisk/ImageServer",
    "visibility": False,
}

# aerial imagery
esri_image_def = {
    "id": "World_Imagery_9777",
    "layerType": "ArcGISTiledMapServiceLayer",
    "url": "https://services.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer",
    "visibility": False,
    "opacity": 1,
    "title": "2021 Imagery (ESRI)",
    "itemId": "10df2279f9684e4a9f6a7f08febac2a9",
    "showLegend": True,
    "layers": [],
}

aerials_2019_def = {
    "id": "2019_WGS_84",
    "layerType": "ArcGISTiledMapServiceLayer",
    "opacity": 1,
    "title": "2019 Imagery (City)",
    "url": "https://gisserver.grantspassoregon.gov/server/rest/services/Aerials/2019_WGS_84/MapServer",
    "visibility": False,
    "minScale": None,
    "maxScale": None,
}

aerials_2019_ndvi_def = {
    "id": "NDVI_2019_WGS_84_NDVI_8524",
    "layerType": "ArcGISTiledMapServiceLayer",
    "opacity": 1,
    "title": "2019 Imagery - NDVI (City)",
    "url": "https://gisserver.grantspassoregon.gov/server/rest/services/Aerials/NDVI_2019_WGS_84_NDVI/MapServer",
    "visibility": False,
    "minScale": None,
    "maxScale": None,
}

aerials_2017_def = {
    "id": "2017_Grants_Pass_Aerials_8659",
    "layerType": "ArcGISTiledMapServiceLayer",
    "opacity": 1,
    "title": "2017 Imagery (City)",
    "url": "https://gisserver.grantspassoregon.gov/server/rest/services/Aerials/2017_Grants_Pass_Aerials/MapServer",
    "visibility": False,
    "minScale": None,
    "maxScale": None,
}

aerials_2015_def = {
    "id": "aerial_imagery_2015_7026",
    "layerType": "ArcGISMapServiceLayer",
    "opacity": 1,
    "title": "2015 Imagery (City)",
    "url": "https://gisserver.grantspassoregon.gov/server/rest/services/Aerials/aerial_imagery_2015/MapServer",
    "visibility": False,
    "minScale": None,
    "maxScale": None,
}

aerials_2011_def = {
    "id": "aerial_imagery_2011_8032",
    "layerType": "ArcGISMapServiceLayer",
    "opacity": 1,
    "title": "2011 Imagery (City)",
    "url": "https://gisserver.grantspassoregon.gov/server/rest/services/Aerials/aerial_imagery_2011/MapServer",
    "visibility": False,
    "minScale": None,
    "maxScale": None,
}

aerials_2007_def = {
    "id": "aerial_imagery_2007_4753",
    "layerType": "ArcGISMapServiceLayer",
    "opacity": 1,
    "title": "2007 Imagery (City)",
    "url": "https://gisserver.grantspassoregon.gov/server/rest/services/Aerials/aerial_imagery_2007/MapServer",
    "visibility": False,
    "minScale": None,
    "maxScale": None,
}

aerials_2004_def = {
    "id": "aerial_imagery_2004_1894",
    "layerType": "ArcGISMapServiceLayer",
    "opacity": 1,
    "title": "2004 Imagery (City)",
    "url": "https://gisserver.grantspassoregon.gov/server/rest/services/Aerials/aerial_imagery_2004/MapServer",
    "visibility": False,
    "minScale": None,
    "maxScale": None,
}

aerials_2001_def = {
    "id": "aerial_imagery_2001_7024",
    "layerType": "ArcGISMapServiceLayer",
    "opacity": 1,
    "title": "2001 Imagery (City)",
    "url": "https://gisserver.grantspassoregon.gov/server/rest/services/Aerials/aerial_imagery_2001/MapServer",
    "visibility": False,
    "minScale": None,
    "maxScale": None,
}

aerials_1998_def = {
    "id": "aerial_imagery_1998_8124",
    "layerType": "ArcGISMapServiceLayer",
    "opacity": 1,
    "title": "1998 Imagery (City)",
    "url": "https://gisserver.grantspassoregon.gov/server/rest/services/Aerials/aerial_imagery_1998/MapServer",
    "visibility": False,
    "minScale": None,
    "maxScale": None,
}

aerials_1975_def = {
    "id": "aerial_imagery_1975_3482",
    "layerType": "ArcGISMapServiceLayer",
    "opacity": 1,
    "title": "1975 Imagery (City)",
    "url": "https://gisserver.grantspassoregon.gov/server/rest/services/Aerials/aerial_imagery_1975/MapServer",
    "visibility": False,
    "minScale": None,
    "maxScale": None,
}

aerials_1952_def = {
    "id": "aerial_imagery_1952_3501",
    "layerType": "ArcGISMapServiceLayer",
    "opacity": 1,
    "title": "1952 Imagery (City)",
    "url": "https://gisserver.grantspassoregon.gov/server/rest/services/Aerials/aerial_imagery_1952/MapServer",
    "visibility": False,
    "minScale": None,
    "maxScale": None,
}

aerials_1938_def = {
    "id": "aerial_imagery_1938_409",
    "layerType": "ArcGISMapServiceLayer",
    "opacity": 1,
    "title": "1938 Imagery (City)",
    "url": "https://gisserver.grantspassoregon.gov/server/rest/services/Aerials/aerial_imagery_1938/MapServer",
    "visibility": False,
    "minScale": None,
    "maxScale": None,
}

# street level imagery
street_imagery_url = "https://services2.arcgis.com/pc4beVTMEhYHqerq/arcgis/rest/services/street_imagery/FeatureServer/0"

# Planning

# oprd historic sites
oprd_historic_sites_url = "https://maps.prd.state.or.us/arcgis/rest/services/Cultural/HistoricSites/MapServer/0"
oprd_historic_sites_def = {
    "id": "HistoricSites_2746",
    "layerType": "ArcGISMapServiceLayer",
    "opacity": 0.5,
    "title": "Historic Sites (OPRD)",
    "url": "https://maps.prd.state.or.us/arcgis/rest/services/Cultural/HistoricSites/MapServer",
    "visibility": False,
}

# national park service
nps_historic_sites_url = "https://mapservices.nps.gov/arcgis/rest/services/cultural_resources/nrhp_locations/MapServer/0"
nps_public_buildings_url = "https://mapservices.nps.gov/arcgis/rest/services/NationalDatasets/NPS_Public_Buildings/MapServer/2"
nps_public_parking_url = "https://mapservices.nps.gov/arcgis/rest/services/NationalDatasets/NPS_Public_ParkingLots/MapServer/2"
nps_public_trails_url = "https://mapservices.nps.gov/arcgis/rest/services/NationalDatasets/NPS_Public_Trails/MapServer/"

# historic and cultural areas

historic_cultural_areas_base = "https://services2.arcgis.com/pc4beVTMEhYHqerq/ArcGIS/rest/services/historic_cultural_areas/FeatureServer/"
url_range = list(range(3, -1, -1))
historic_cultural_areas_urls = expand_urls(historic_cultural_areas_base, url_range)
url_range = [3, 1, 0]
historic_cultural_tourism_urls = expand_urls(historic_cultural_areas_base, url_range)
# historic_cultural_areas_urls.insert(2, oprd_historic_sites_url)

# zoning
zoning_base = "https://services2.arcgis.com/pc4beVTMEhYHqerq/ArcGIS/rest/services/zoning_group/FeatureServer/"
url_range = list(range(4, -1, -1))
zoning_urls = expand_urls(zoning_base, url_range)

# planning misc
# planning_group_base = "https://services2.arcgis.com/pc4beVTMEhYHqerq/ArcGIS/rest/services/planning_group/FeatureServer/"
planning_group_base = "https://gisserver.grantspassoregon.gov/server/rest/services/CommunityDevlp/planning/MapServer/"
url_range = list(range(5, -1, -1))
planning_urls = expand_urls(planning_group_base, url_range)

# marijuana and adult use
marijuana_adult_base = "https://services2.arcgis.com/pc4beVTMEhYHqerq/arcgis/rest/services/marijuana_adult_use/FeatureServer/"
url_range = list(range(13, -1, -1))
marijuana_adult_urls = expand_urls(marijuana_adult_base, url_range)

# revision of marijuana permitting buffers 3/02/2023
marijuana_permitting_base = "https://services2.arcgis.com/pc4beVTMEhYHqerq/arcgis/rest/services/marijuana_permitting/FeatureServer/"
url_range = list(range(19, -1, -1))
marijuana_permitting_urls = expand_urls(marijuana_permitting_base, url_range)

# agreements and financial
# agreements_base = "https://services2.arcgis.com/pc4beVTMEhYHqerq/arcgis/rest/services/agreements/FeatureServer/"
agreements_base = (
    "https://gisserver.grantspassoregon.gov/server/rest/services/agreements/MapServer/"
)
url_range = list(range(4, -1, -1))
agreements_urls = expand_urls(agreements_base, url_range)
# agreements_urls.remove(agreements_urls[0])


# transportation
# transportation_base = "https://services2.arcgis.com/pc4beVTMEhYHqerq/ArcGIS/rest/services/transportation1/FeatureServer/"
transportation_base = "https://gisserver.grantspassoregon.gov/server/rest/services/transportation/MapServer/"
url_range = list(range(16, -1, -1))
transportation_urls = expand_urls(transportation_base, url_range)
# transportation_signs_url = "https://gisserver.grantspassoregon.gov/server/rest/services/transportation_signs/MapServer/0"
# transportation_urls.insert(13, transportation_signs_url)
transportation_urls.insert(4, county_roads_url)
transportation_urls.insert(4, odot_roads_url)
transportation_urls.insert(6, transportation_urls[6])
transportation_urls.insert(6, transportation_urls[6])
transportation_urls.insert(0, odot_railroad_url)
transportation_urls.insert(0, odot_construction_url)
transportation_urls.insert(0, odot_traffic_url)

# transportation editing
street_adoption_editing = "https://gisserver.grantspassoregon.gov/server/rest/services/Editing/street_adoption/FeatureServer/0"
transportation_editing = [street_adoption_editing]

# utilities

# water

water_base = "https://gisserver.grantspassoregon.gov/server/rest/services/PublicWorks/water_utilities/MapServer/"
url_range = list(range(11, -1, -1))
water_urls = expand_urls(water_base, url_range)
# copy water mains layer twice (for ownership and pipe size symbology)
water_urls.insert(5, water_urls[5])
water_urls.insert(5, water_urls[5])
# copy water pressure zones for billing zones
water_urls.insert(2, water_urls[2])

# stormwater

# stormwater_base = "https://gisserver.grantspassoregon.gov/server/rest/services/PublicWorks/stormwater/MapServer/"
stormwater_base = "https://services2.arcgis.com/pc4beVTMEhYHqerq/arcgis/rest/services/stormwater/FeatureServer/"
url_range = list(range(11, -1, -1))
stormwater_urls = expand_urls(stormwater_base, url_range)

stormwater_editing_base = "https://gisserver.grantspassoregon.gov/server/rest/services/PublicWorks/stormwater/FeatureServer/"
stormwater_editing = expand_urls(stormwater_editing_base, url_range)

# sewer
# sewer_areas_base = "https://services2.arcgis.com/pc4beVTMEhYHqerq/arcgis/rest/services/sewer_areas/FeatureServer/"
# url_range = list(range(3, -1, -1))
# sewer_areas_urls = expand_urls(sewer_areas_base, url_range)
#
# sewer_base = "https://gisserver.grantspassoregon.gov/server/rest/services/PublicWorks/SS/FeatureServer/"
# url_range = list(range(7, 0, -1))
# sewer_urls = expand_urls(sewer_base, url_range)
#
# sewer_areas_urls.extend(sewer_urls)
# sewer_urls = sewer_areas_urls
sewer_base = "https://gisserver.grantspassoregon.gov/server/rest/services/PublicWorks/sewer_utilities/MapServer/"
sewer_editing_base = "https://gisserver.grantspassoregon.gov/server/rest/services/PublicWorks/sewer_utilities/FeatureServer/"
url_range = list(range(11, -1, -1))
sewer_urls = expand_urls(sewer_base, url_range)
sewer_editing = expand_urls(sewer_editing_base, url_range)

# power and gas
# protected by NDA, not for public distribution

power_gas_base = "https://gisserver.grantspassoregon.gov/server/rest/services/PublicWorks/power_gas_utilities/MapServer/"
url_range = list(range(3, -1, -1))
power_gas_urls = expand_urls(power_gas_base, url_range)

# cell towers
cell_towers_url = "https://services2.arcgis.com/pc4beVTMEhYHqerq/ArcGIS/rest/services/cell_towers/FeatureServer/0"


# merlin landfill
landfill_base = "https://services2.arcgis.com/pc4beVTMEhYHqerq/arcgis/rest/services/merlin_landfill/FeatureServer/"
url_range = list(range(6, -1, -1))
landfill_urls = expand_urls(landfill_base, url_range)

# as builts
as_builts_base = (
    "https://gisserver.grantspassoregon.gov/server/rest/services/as_builts/MapServer/"
)
url_range = [1, 0]
as_builts_urls = expand_urls(as_builts_base, url_range)

# parking
parking_base = "https://services2.arcgis.com/pc4beVTMEhYHqerq/arcgis/rest/services/parking/FeatureServer/"
url_range = [1, 0]
parking_urls = expand_urls(parking_base, url_range)

# parks
parks_base = "https://services2.arcgis.com/pc4beVTMEhYHqerq/ArcGIS/rest/services/parks/FeatureServer/"
url_range = [1, 0]
parks_urls = expand_urls(parks_base, url_range)

county_parks_url = (
    "https://gis.co.josephine.or.us/arcgis/rest/services/Parks/Park_Areas/MapServer/0"
)
parks_urls.insert(0, county_parks_url)
tourism_parks_urls = [transportation_urls[14], parks_urls[0], parks_urls[2]]

# topographic contours
contours_base = "https://gisserver.grantspassoregon.gov/server/rest/services/topographic_contours/MapServer/"
url_range = list(range(9, -1, -1))
contours_urls = expand_urls(contours_base, url_range)

# traffic reports
traffic_base = "https://gisserver.grantspassoregon.gov/server/rest/services/traffic_reports/MapServer/"
url_range = [1, 0]
traffic_urls = expand_urls(traffic_base, url_range)


# staff editing
# sketch points
sketch_base = "https://gisserver.grantspassoregon.gov/server/rest/services/Editing/markup_editing/FeatureServer/"
# sketch_base = "https://gisserver.grantspassoregon.gov/server/rest/services/PublicWorks/sketch_editing/FeatureServer/"
url_range = [2, 1, 0]
sketch_urls = expand_urls(sketch_base, url_range)
