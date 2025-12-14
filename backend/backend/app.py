# app.py
from ai_models.intrusion_detection import analyze_traffic

def run_backend():
    result = analyze_traffic(packet_size=1200, failed_logins=3)
    print("Backend analysis result:", result)

if __name__ == "__main__":
    run_backend()
