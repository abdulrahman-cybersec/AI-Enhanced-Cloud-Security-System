"""
AI-based Intrusion Detection Module
"""

def detect_intrusion(traffic_data):
    """
    Simple rule-based detection (placeholder for AI model)
    """
    if traffic_data["failed_logins"] > 20:
        return True
    if traffic_data["packet_rate"] > 1500:
        return True
    return False
