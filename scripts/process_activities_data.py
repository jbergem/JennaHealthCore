import pandas as pd
import json

def process_activities_data(input_file, output_file):
    """Leser inn aktiviteter og lagrer alle data som JSON."""

    # Les CSV-filen med alle kolonner
    df = pd.read_csv(input_file, sep=',', encoding='utf-8')

    # Konverter til JSON-format
    activities_data = df.to_dict(orient='records')

    # Lagre som JSON
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(activities_data, file, ensure_ascii=False, indent=4)

    print(f"Aktivitetsdata behandlet og lagret som: {output_file}")

if __name__ == "__main__":
    input_csv = 'data/garmin/activities.csv'  # Tilpass stien til filen din
    output_json = 'data/garmin/json-files/activities_data.json'
    process_activities_data(input_csv, output_json)
