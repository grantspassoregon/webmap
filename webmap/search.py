from webmap import urls as u
from arcgis.mapping import WebMap
import logging

# adapted from https://www.esri.com/arcgis-blog/products/apps/field-mobility/customize-feature-search-web-maps-python/


def search_item(url, field, matchExists=False, field_type="esriFieldTypeString"):
    """
    List of fields to specify search in a web map.

    :param url: Url for the target search layer.
    :type url: String
    :param field: Field in attribute table of layer to search.
    :type field: String
    :param matchExists: Indicates whether to search for exact matches only.
    :type matchExists: Boolean
    :param field_type: Esri data type of field parameter.
    :type field_type: String
    """
    item_list = [url, field, matchExists, field_type]
    return item_list


# search list for fields in a web map
# each element in list in a list specifying:
# 1) url, 2) field of layer to search, 3) exactMatch bool, 4) field type
search_list = [
    search_item(u.land_use_urls[3], "FULLADDR"),
    search_item(u.land_use_urls[2], "FULLADDR"),
    search_item(u.land_use_urls[2], "TAXLOT"),
    search_item(u.land_use_urls[1], "NAME"),
    search_item(u.land_use_urls[0], "FACILITYID"),
    search_item(u.land_use_urls[0], "MAPNUMX"),
    search_item(u.city_parcels_url, "MAPNUM"),
    search_item(u.city_parcels_url, "SITUS"),
    search_item(u.city_parcels_url, "NAME"),
    search_item(u.county_parcels_url, "MAPNUM"),
    search_item(u.county_parcels_url, "SITUS"),
    search_item(u.county_parcels_url, "NAME"),
    search_item(u.assessment_maps_url, "MAPNUMBE_1"),
    search_item(u.tax_code_url, "TaxCode"),
    search_item(u.bia_urls[1], "LARName"),
    search_item(u.bia_urls[0], "Land_Area_"),
    search_item(u.aiannha_urls[6], "NAME"),
    search_item(u.aiannha_urls[6], "AIANNH"),
    search_item(u.aiannha_urls[5], "NAME"),
    search_item(u.aiannha_urls[5], "AIANNH"),
    search_item(u.aiannha_urls[4], "NAME"),
    search_item(u.aiannha_urls[4], "AIANNH"),
    search_item(u.aiannha_urls[3], "NAME"),
    search_item(u.aiannha_urls[3], "AIANNH"),
    search_item(u.aiannha_urls[2], "NAME"),
    search_item(u.aiannha_urls[2], "AIANNH"),
    search_item(u.aiannha_urls[1], "NAME"),
    search_item(u.aiannha_urls[1], "AIANNH"),
    search_item(u.aiannha_urls[0], "NAME"),
    search_item(u.aiannha_urls[0], "AIANNH"),
    search_item(u.boundaries_urls[6], "NAME"),
    search_item(u.boundaries_urls[2], "AcctNum"),
    search_item(u.boundaries_urls[2], "MAPNUM"),
    search_item(u.school_locations, "Institution_Name_Line1"),
    search_item(u.school_locations, "Site_Address_Line1"),
    search_item(u.school_districts_urls[8], "ADDRESS"),
    search_item(u.school_districts_urls[8], "SCHOOL_DIS"),
    search_item(u.school_districts_urls[8], "SCHOOL_NAM"),
    search_item(u.school_districts_urls[7], "Name"),
    search_item(u.school_districts_urls[6], "Name"),
    search_item(u.school_districts_urls[5], "ADDRESS"),
    search_item(u.school_districts_urls[5], "SCHOOL_DIS"),
    search_item(u.school_districts_urls[5], "SCHOOL_NAM"),
    search_item(u.school_districts_urls[4], "EDUCATIONAL_SERVICE_DISTRICT_NAME"),
    search_item(u.school_districts_urls[4], "GRADE_K_NAME"),
    search_item(u.school_districts_urls[4], "SCHOOL_DISTRICT_NAME"),
    search_item(u.school_districts_urls[3], "GRADE_8_NAME"),
    search_item(u.school_districts_urls[2], "GRADE_12_NAME"),
    search_item(u.school_districts_urls[1], "DISTRICTNAME"),
    search_item(u.school_districts_urls[1], "NAME"),
    search_item(u.school_districts_urls[0], "NAME"),
    search_item(u.historic_cultural_areas_urls[3], "Artist"),
    search_item(u.historic_cultural_areas_urls[3], "FACILITYID"),
    search_item(u.historic_cultural_areas_urls[3], "Title_of_Piece"),
    search_item(u.historic_cultural_areas_urls[2], "OHSR_HX_NAME"),
    search_item(u.agreements_urls[4], "DOC_NO"),
    search_item(u.agreements_urls[4], "UNREC_NUM"),
    search_item(u.agreements_urls[3], "INSTRUMENT"),
    search_item(u.agreements_urls[2], "InstrumentNumber"),
    search_item(u.agreements_urls[1], "INSTRUMENT"),
    search_item(u.agreements_urls[0], "INST_NUM"),
    search_item(u.agreements_urls[0], "DISTRICT_1"),
    search_item(u.agreements_urls[0], "FINAL_ORDI"),
    search_item(u.agreements_urls[0], "FIRST_RESO"),
    search_item(u.marijuana_adult_urls[13], "BusinessAddress"),
    search_item(u.marijuana_adult_urls[13], "BusinessName"),
    search_item(u.marijuana_adult_urls[13], "BusinessOwner"),
    search_item(u.marijuana_adult_urls[12], "BusinessName"),
    search_item(u.marijuana_adult_urls[11], "FacilityAddress"),
    search_item(u.marijuana_adult_urls[11], "FacilityName"),
    search_item(u.marijuana_adult_urls[10], "FacilityName"),
    search_item(u.marijuana_adult_urls[9], "NAME"),
    search_item(u.marijuana_adult_urls[8], "NAME"),
    search_item(u.marijuana_adult_urls[7], "NAME"),
    search_item(u.marijuana_adult_urls[7], "CLASS"),
    search_item(u.marijuana_adult_urls[6], "NAME"),
    search_item(u.marijuana_adult_urls[5], "ADDRESS"),
    search_item(u.marijuana_adult_urls[5], "SCHOOL_NAM"),
    search_item(u.marijuana_adult_urls[4], "SCHOOL_NAM"),
    search_item(u.marijuana_adult_urls[1], "NAME"),
    search_item(u.marijuana_adult_urls[0], "NAME"),
    search_item(u.zoning_urls[4], "LAYER"),
    search_item(u.zoning_urls[2], "FOOD_ZONE"),
    search_item(u.zoning_urls[1], "ZONECLASS"),
    search_item(u.zoning_urls[1], "ZONEDESC"),
    search_item(u.zoning_urls[0], "COMPCLASS"),
    search_item(u.zoning_urls[0], "COMPDESC"),
    search_item(u.planning_urls[5], "NAME"),
    search_item(u.planning_urls[5], "ADDRESS"),
    search_item(u.planning_urls[5], "MAPNUM"),
    search_item(u.planning_urls[4], "NAME"),
    search_item(u.planning_urls[3], "RSIA_NAME"),
    search_item(u.transportation_urls[23], "TSSU_ID"),  # traffic signals
    search_item(u.transportation_urls[22], "FACILITYID"),  # antique street lights
    search_item(u.transportation_urls[20], "ATTACHID"),  # signs
    search_item(u.transportation_urls[20], "FACILITYID"),
    search_item(u.transportation_urls[19], "FACILITYID"),  # poles
    search_item(u.transportation_urls[19], "HistoricID"),
    search_item(u.transportation_urls[18], "LAYER"),  # bus stops
    search_item(u.transportation_urls[18], "ROUTE_NUMBER"),  # bus routes
    search_item(u.transportation_urls[15], "NAME"),  # trails
    search_item(u.transportation_urls[14], "ADOPTED_BY"),  # street adoption
    search_item(u.transportation_urls[14], "FULLNAME"),
    search_item(u.transportation_urls[13], "FULLNAME"),  # PCI
    search_item(u.transportation_urls[12], "AssetID"),  # Streets (City)
    search_item(u.transportation_urls[12], "FULLNAME"),
    search_item(u.transportation_urls[9], "full_name"),  # Streets (County)
    search_item(u.transportation_urls[5], "FACILITYID"),  # Sidewalks
    search_item(u.transportation_urls[4], "FACILITYID"),  # Sidewalk curb ramps
    search_item(u.transportation_urls[2], "RR_NAME"),  # Railroads
    search_item(u.power_gas_urls[1], "AVOID"),  # Gas Lines - Abandoned
    search_item(u.power_gas_urls[0], "AVOID"),  # Gas Lines - Current
    search_item(u.water_urls[14], "ACCOUNTID"),  # Water Meters
    search_item(u.water_urls[14], "AssociatedAddress"),
    search_item(u.water_urls[14], "AssocMapNum"),
    search_item(u.water_urls[14], "FACILITYID"),
    search_item(u.water_urls[13], "FACILITYID"),  # water fittings
    search_item(u.water_urls[12], "FACILITYID"),  # water valves
    search_item(u.water_urls[11], "FACILITYID"),  # water hydrants
    search_item(u.water_urls[10], "FACILITYID"),  # water sampling stations
    search_item(u.water_urls[10], "ADDRESS"),
    search_item(u.water_urls[9], "FACILITYID"),  # water service laterals
    search_item(u.water_urls[8], "FACILITYID"),  # water mains
    search_item(u.water_urls[5], "AssetID"),  # water network structures
    search_item(u.water_urls[4], "PERMITNUMB"),  # water network structures
    search_item(u.water_urls[3], "AssetID"),  # water pressure zones
    search_item(u.water_urls[0], "FZ"),  # water flush zones
    search_item(u.stormwater_urls[11], "FACILITYID"),  # stormwater manholes
    search_item(u.stormwater_urls[11], "HistoricID"),
    search_item(u.stormwater_urls[10], "FACILITYID"),  # stormwater inlets
    search_item(u.stormwater_urls[10], "HistoricID"),
    search_item(u.stormwater_urls[9], "FACILITYID"),  # stormwater cleanouts
    search_item(u.stormwater_urls[8], "FACILITYID"),  # stormwater valves
    search_item(u.stormwater_urls[7], "FACILITYID"),  # stormwater outfalls
    search_item(u.stormwater_urls[7], "HistoricID"),
    search_item(u.stormwater_urls[6], "FACILITYID"),  # stormwater fittings
    search_item(u.stormwater_urls[5], "FACILITYID"),  # stormwater culverts
    search_item(u.stormwater_urls[4], "FACILITYID"),  # stormwater open drains
    search_item(u.stormwater_urls[4], "HistoricID"),
    search_item(u.stormwater_urls[3], "FACILITYID"),  # stormwater gravity mains
    search_item(u.stormwater_urls[3], "HistoricID"),
    search_item(u.stormwater_urls[2], "FACILITYID"),  # stormwater detention
    search_item(u.stormwater_urls[2], "HistoricID"),
    search_item(u.stormwater_urls[1], "SUB_BASIN_ID"),  # stormwater sub-basins
    search_item(u.stormwater_urls[1], "SW_BASIN"),
    search_item(u.stormwater_urls[0], "SUB_BASIN_ID"),  # stormwater basins
    search_item(u.sewer_urls[11], "AssetID"),  # sewer manholes
    search_item(u.sewer_urls[11], "HistoricID"),
    search_item(u.sewer_urls[10], "FACILITYID"),  # sewer fittings
    search_item(u.sewer_urls[9], "AssetID"),  # sewer valves
    search_item(u.sewer_urls[9], "HistoricID"),
    search_item(u.sewer_urls[8], "AssetID"),  # sewer clean outs
    search_item(u.sewer_urls[8], "HistoricID"),
    search_item(u.sewer_urls[7], "FACILITYID"),  # sewer discharge points
    search_item(u.sewer_urls[7], "HistoricID"),
    search_item(u.sewer_urls[6], "AssetID"),  # sewer gravity mains
    search_item(u.sewer_urls[6], "FACILITYID"),
    search_item(u.sewer_urls[5], "FACILITYID"),  # sewer lateral lines
    search_item(u.sewer_urls[5], "HistoricID"),
    search_item(u.sewer_urls[4], "AssetID"),  # sewer pressurized mains
    search_item(u.sewer_urls[4], "FACILITYID"),
    search_item(u.sewer_urls[1], "AssetID"),  # sewer network structures
    search_item(u.sewer_urls[0], "AssetID"),  # sewer basins
    search_item(u.cell_towers_url, "Street_Add"),
    search_item(u.cell_towers_url, "NOTES"),
    search_item(u.parks_urls[2], "NAME"),  # parks (city)
    search_item(u.parks_urls[1], "FACILITYID"),  # landscape (city maintained)
    search_item(u.parks_urls[0], "NAME"),  # parks (county)
]


def get_layer_id(layers, layer_url):
    layer_id = None
    for lyr in layers:
        logging.debug("Searching layer %s for url.", lyr["title"])
        if lyr["layerType"] == "GroupLayer" and layer_id is None:
            layer_id = get_layer_id(lyr["layers"], layer_url)
        elif "url" in lyr:
            if lyr["url"] == layer_url:
                layer_id = lyr["id"]
    return layer_id
    #     else:
    #         raise Exception("Wrong url in layer %s", lyr["id"])
    # else:
    #     raise Exception("No url in layers.")


def add_search_field(properties, id, field, match, field_type):
    d = dict()
    d.update({"id": id})
    f = dict()
    f.update({"name": field})
    f.update({"exactMatch": match})
    f.update({"type": field_type})
    d.update({"field": f})
    properties.append(d)


def search_fields(item, search_list=search_list):
    properties = list()
    wm = WebMap(item)
    lyrs = wm.layers
    for srch in search_list:
        lyr_id = get_layer_id(lyrs, srch[0])
        if lyr_id is not None:
            add_search_field(properties, lyr_id, srch[1], srch[2], srch[3])
        else:
            logging.debug("Layer %s not found.", srch[0])
    return properties


def add_search(project_map, search_list=search_list):
    properties = search_fields(project_map, search_list)
    map_def = project_map.get_data()
    map_def["applicationProperties"]["viewing"]["search"] = {
        "enabled": True,
        "disablePlaceFinder": False,
        "hintText": "Address or Fields",
        "layers": properties,
    }
    project_map.update({"text": str(map_def)})
