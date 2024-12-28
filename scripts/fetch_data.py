import json

def fetch_extended_dummy_data():
    """Simulerer utvidet data for testing."""
    extended_data = {
        "sleep": [
            {"date": "2024-12-28", "duration": 5},
            {"date": "2024-12-27", "duration": 7},
            {"date": "2024-12-26", "duration": 4},
        ],
        "hrv": [
            {"date": "2024-12-28", "hrv": 45},
            {"date": "2024-12-27", "hrv": 55},
            {"date": "2024-12-26", "hrv": 60},
        ],
        "pulse": [
            {"date": "2024-12-28", "resting_pulse": 65},
            {"date": "2024-12-27", "resting_pulse": 62},
            {"date": "2024-12-26", "resting_pulse": 64},
        ],
    }
    with open('data/garmin/extended_data.json', 'w') as file:
        json.dump(extended_data, file)
        
if __name__ == "__main__":
    fetch_extended_dummy_data()

