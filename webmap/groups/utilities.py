from webmap import webmap as w
from webmap import maps as m
from webmap import urls as u
from webmap.groups import water as wa
from webmap.groups import stormwater as s
import logging


def utilities(base, template, internal, public=False, basemap=False):
    """
    Utilities for the City of Grants Pass, Oregon.

    :param base: Group layer definition or map project target for layers.
    :param template: Reference template for map layers.
    :type template: JSON dictionary
    :param internal: Portal connection for internal access layers.
    :type internal: ArcGIS GIS connection.
    :param public: Indicates whether to build internal access layers.
    :type public: Boolean
    :param basemap: Indicates whether appending to group layer or project map.
    :type basemap: Boolean
    :return: Updates group layer definition with layers.
    :rtype: None
    """

    group_name = "Utilities"
    map_group = w.group_layer(group_name)

    w.add_single_layer(
        "cell_towers", u.cell_towers_url, map_group, template, visibility=False
    )
    logging.info("Cell towers added to %s.", group_name)
    m.as_builts_layers(map_group, template)
    m.impervious_layers(map_group, template, internal)
    logging.info("Impervious surface added to %s.", group_name)
    m.sewer_layers(map_group, template, internal)
    logging.info("Sewer layers added to %s.", group_name)
    s.stormwater(map_group, template, internal)
    logging.info("Stormwater layers added to %s.", group_name)
    wa.water(map_group, template, internal)
    logging.info("Water utilities layers added to %s.", group_name)
    if not public:
        m.power_gas_layers(map_group, template, internal)
        logging.info("Power and gas utilities layers added to %s.", group_name)

    logging.info("Appending layers to %s definition.", group_name)
    w.add_group(base, map_group, basemap)
