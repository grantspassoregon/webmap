def missing_sidewalks_layer_names(post):
    """
    Create list of key names for layer definition data.
    """
    layer_stub = [
        "park_street_sidewalks_export",
        "private_street_sidewalks_export",
        "state_street_sidewalks_export",
        "arterial_sidewalks_export",
        "collector_sidewalks_export",
        "local_collector_sidewalks_export",
        "local_street_sidewalks_export",
        "streets",
        "sidewalks",
        "addresses",
        "hillslope",
        "taxlots",
    ]
    layer_name = []
    for lyr in layer_stub:
        layer_name.append("missing_sidewalks_" + lyr + post)
    # layer order is reversed from menu order
    layer_name.reverse()
    return layer_name
