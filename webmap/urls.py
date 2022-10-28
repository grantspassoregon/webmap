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

# city boundaries

boundaries_base = "https://services2.arcgis.com/pc4beVTMEhYHqerq/arcgis/rest/services/regulatory_boundaries/FeatureServer/"
url_range = list(range(7, -1, -1))
boundaries_urls = expand_urls(boundaries_base, url_range)

# school districts

# josephine county
school_locations = "https://gis.co.josephine.or.us/arcgis/rest/services/Planning/SchoolLocatons/MapServer/0"
# elementary schools
school_zones = "https://gis.co.josephine.or.us/arcgis/rest/services/Planning/School_Zones/MapServer/0"

# city schools data
school_districts_base = "https://services2.arcgis.com/pc4beVTMEhYHqerq/arcgis/rest/services/school_district/FeatureServer/"
url_range = list(range(5, -1, -1))
school_districts_urls = expand_urls(school_districts_base, url_range)
# elementary, middle and high school zones
school_districts_urls.insert(2, school_zones)
school_districts_urls.insert(2, school_zones)
school_districts_urls.insert(2, school_zones)
school_districts_urls.append(school_locations)


# library district
library_url = "https://gis.co.josephine.or.us/arcgis/rest/services/Assessor/Library_District/MapServer/0"


# addresses
county_addresses_url = "https://services6.arcgis.com/Hf6u9DI4oZH2QTg9/arcgis/rest/services/Josephine_County_Site_Address/FeatureServer/0"

# land use
land_use_base = "https://services2.arcgis.com/pc4beVTMEhYHqerq/arcgis/rest/services/land_use/FeatureServer/"
url_range = [2, 1, 0]
land_use_urls = expand_urls(land_use_base, url_range)
land_use_urls.insert(2, county_addresses_url)


# tax parcels
county_parcels_url = "https://gis.co.josephine.or.us/arcgis/rest/services/Assessor/Assessor_Taxlots/MapServer/0"
city_parcels_url = "https://services2.arcgis.com/pc4beVTMEhYHqerq/arcgis/rest/services/taxlots/FeatureServer/0"
assessment_maps_url = "https://services2.arcgis.com/pc4beVTMEhYHqerq/arcgis/rest/services/land_use/FeatureServer/3"
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

# Fish & Wildlife NWI Wetlands
fw_nwi_wetlands = (
    "https://www.fws.gov/wetlandsmapservice/rest/services/Wetlands/MapServer/0"
)

# NRCS Hydric Soils
# nrcs_hydric_soils = "https://gisdata.dsl.state.or.us/arcgis/rest/services/Maps/SWI_HydricSoil_2020_B/MapServer/0"
nrcs_hydric_soils = (
    "https://maps.dsl.state.or.us/arcgis/rest/services/HydricSoil/MapServer/0"
)

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

# deq
# drinking water sources
deq_drinking_water_source_base = "https://arcgis.deq.state.or.us/arcgis/rest/services/DEQ_Services/DrinkingWaterTestService/MapServer/"
url_range = [7, 6, 4, 3, 2]
deq_drinking_water_source_urls = expand_urls(deq_drinking_water_source_base, url_range)

# drinking water protection
deq_drinking_water_protection_base = "https://arcgis.deq.state.or.us/arcgis/rest/services/WQ/DrinkingWaterProtectionPCS/MapServer/"
url_range = list(range(31, 22, -1))
url_range.extend(list(range(21, -1, -1)))
deq_drinking_water_protection_urls = expand_urls(
    deq_drinking_water_protection_base, url_range
)

# surface water impaired
deq_hydro_2022_base = (
    "https://arcgis.deq.state.or.us/arcgis/rest/services/WQ/WQL_Hydro_2022/MapServer/"
)
url_range = [2, 1, 0]
deq_hydro_2022_urls = expand_urls(deq_hydro_2022_base, url_range)


# dsl essential salmon habitat
dsl_esh_base = "https://maps.dsl.state.or.us/arcgis/rest/services/ESH/MapServer/"
url_range = list(range(9, 0, -1))
dsl_esh_urls = expand_urls(dsl_esh_base, url_range)


# transportation
odot_construction_url = "https://services.arcgis.com/uUvqNMGPm7axC2dD/ArcGIS/rest/services/ODOT_Traffic_Construction/FeatureServer/0"
odot_traffic_url = "https://services.arcgis.com/uUvqNMGPm7axC2dD/ArcGIS/rest/services/ODOT_Traffic_Incidents/FeatureServer/0"

county_roads = "https://gis.co.josephine.or.us/arcgis/rest/services/Public_Works/Josephine_County_Owned_Roads/MapServer/0"


# forest service wildfire
fs_wildfire_potential_def = {
    "id": "RMRS_WRC_WildfireHazardPotential_5283",
    "layerType": "ArcGISImageServiceLayer",
    "opacity": 1,
    "title": "Wildfire Hazard Potential (FS)",
    "url": "https://apps.fs.usda.gov/fsgisx01/rest/services/RDW_Wildfire/RMRS_WRC_WildfireHazardPotential/ImageServer",
    "visibility": False,
}

fs_wildfire_housing_def = {
    "id": "RMRS_WRC_HousingUnitRisk_1007",
    "layerType": "ArcGISImageServiceLayer",
    "opacity": 1,
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
    "title": "Aerial Photo - ESRI (2021)",
    "itemId": "10df2279f9684e4a9f6a7f08febac2a9",
    "showLegend": True,
    "layers": [],
}

# Planning

# oprd historic sites
oprd_historic_sites_url = "https://maps.prd.state.or.us/arcgis/rest/services/Cultural/HistoricSites/MapServer/0"

# national park service
nps_historic_sites_url = "https://mapservices.nps.gov/arcgis/rest/services/cultural_resources/nrhp_locations/MapServer/0"
nps_public_buildings_url = "https://mapservices.nps.gov/arcgis/rest/services/NationalDatasets/NPS_Public_Buildings/MapServer/2"
nps_public_parking_url = "https://mapservices.nps.gov/arcgis/rest/services/NationalDatasets/NPS_Public_ParkingLots/MapServer/2"
nps_public_trails_url = "https://mapservices.nps.gov/arcgis/rest/services/NationalDatasets/NPS_Public_Trails/MapServer/"

# historic and cultural areas

historic_cultural_areas_base = "https://services2.arcgis.com/pc4beVTMEhYHqerq/ArcGIS/rest/services/historic_cultural_areas/FeatureServer/"
url_range = list(range(3, -1, -1))
historic_cultural_areas_urls = expand_urls(historic_cultural_areas_base, url_range)
historic_cultural_areas_urls.insert(2, oprd_historic_sites_url)

# zoning
zoning_base = "https://services2.arcgis.com/pc4beVTMEhYHqerq/ArcGIS/rest/services/zoning_group/FeatureServer/"
url_range = list(range(4, -1, -1))
zoning_urls = expand_urls(zoning_base, url_range)

# planning misc
planning_group_base = "https://services2.arcgis.com/pc4beVTMEhYHqerq/ArcGIS/rest/services/planning_group/FeatureServer/"
url_range = list(range(5, -1, -1))
planning_urls = expand_urls(planning_group_base, url_range)

# marijuana and adult use
marijuana_adult_base = "https://services2.arcgis.com/pc4beVTMEhYHqerq/arcgis/rest/services/marijuana_adult_use/FeatureServer/"
url_range = list(range(13, -1, -1))
marijuana_adult_urls = expand_urls(marijuana_adult_base, url_range)

# agreements and financial
# agreements_base = "https://services2.arcgis.com/pc4beVTMEhYHqerq/arcgis/rest/services/agreements_financial/FeatureServer/"
agreements_base = "https://services2.arcgis.com/pc4beVTMEhYHqerq/arcgis/rest/services/agreements/FeatureServer/"
url_range = list(range(5, -1, -1))
agreements_urls = expand_urls(agreements_base, url_range)
