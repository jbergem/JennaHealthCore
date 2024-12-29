import json

def fetch_garmin_data():
    """Henter GarminDB-data (simulert)."""
    garmin_data = {
        "activities": [
            {"date": "2024-12-28", "steps": 10543, "calories": 2563, "distance": 8.5},
            {"date": "2024-12-27", "steps": 9872, "calories": 2345, "distance": 7.9}
        ],
        "sleep": [
            {"date": "2024-12-28", "duration": 8, "quality": "good"},
            {"date": "2024-12-27", "duration": 7.75, "quality": "fair"}
        ],
        "heartRate": [
            {"date": "2024-12-28", "restingHR": 60, "averageHR": 75, "maxHR": 150},
            {"date": "2024-12-27", "restingHR": 62, "averageHR": 80, "maxHR": 155}
        ]
    }

    with open('data/garmin/garmin_data.json', 'w') as file:
        json.dump(garmin_data, file)

if __name__ == "__main__":
    fetch_garmin_data()
