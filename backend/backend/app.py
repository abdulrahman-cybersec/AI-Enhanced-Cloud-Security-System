"""
AI-Enhanced Cloud Security System
Main Application File
"""

from monitoring.traffic_monitor import collect_traffic
from ai_models.intrusion_detection import detect_intrusion
from alerts.alert_system import send_alert

def main():
    print("Starting AI-Enhanced Cloud Security System...")

    traffic_data = collect_traffic()
    result = detect_intrusion(traffic_data)

    if result["threat_detected"]:
        send_alert(result["threat_type"])
        print("Threat detected:", result["threat_type"])
    else:
        print("Network traffic is normal")

if __name__ == "__main__":
    main()
