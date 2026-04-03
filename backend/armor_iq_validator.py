def validate_safety_rules(signal, sensor_data):
    """
    ArmorIQ rules engine.
    Returns True if it's safe to clear the signal (Green Wave), False if blocked.
    """
    # Hard safety rule: Pedestrians active
    # We simulate reading from the signal's mock state
    if signal.get("pedestrian_blocked", False):
        return False
        
    # Example safety rule: Cross-traffic anomaly from sensor payload
    if sensor_data.get("intersection_clearance", 1.0) < 0.5:
        return False
        
    return True
