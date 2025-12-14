import random

def collect_traffic():
    traffic = {
        "packet_rate": random.randint(100, 2000),
        "failed_logins": random.randint(0, 50),
        "data_volume": random.randint(10, 1000)
    }
    return traffic
