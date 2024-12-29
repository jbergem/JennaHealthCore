import json
import pandas as pd
from datetime import datetime

# Funksjon for å lese JSON-filer og konvertere til DataFrame
def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return pd.DataFrame(data)

# Funksjon for å kombinere dataene basert på dato
def combine_health_data(sleep_file, stress_file, activities_file):
    sleep_data = load_json(sleep_file)
    stress_data = load_json(stress_file)
    activities_data = load_json(activities_file)

    # Konverter datoformat til datetime for enkel matching
    sleep_data['Date'] = pd.to_datetime(sleep_data['Date'])
    stress_data['Date'] = pd.to_datetime(stress_data['Date'])
    activities_data['Date'] = pd.to_datetime(activities_data['Date'])

    # Kombiner alle datasettene basert på dato
    combined_data = sleep_data.merge(stress_data, on='Date', how='outer').merge(activities_data, on='Date', how='outer')

    return combined_data

# Generer helseanalyse-rapport
def generate_health_report(combined_data):
    report = []

    for _, row in combined_data.iterrows():
        date = row['Date'].strftime('%Y-%m-%d')
        summary = f"Helseanalyse for {date}:\n"

        # Søvnanalyse
        if 'Duration' in row and pd.notna(row['Duration']):
            sleep_hours = row['Duration']
            summary += f"  - Søvn: {sleep_hours} timer. "
            if sleep_hours < 7:
                summary += "Anbefaling: Prøv å sove mer for bedre restitusjon.\n"
            else:
                summary += "Søvnkvaliteten ser bra ut!\n"

        # Stressanalyse
        if 'Avg Stress' in row and pd.notna(row['Avg Stress']):
            stress = row['Avg Stress']
            summary += f"  - Gjennomsnittlig stressnivå: {stress}. "
            if stress > 50:
                summary += "Anbefaling: Prøv stressreduserende aktiviteter som meditasjon.\n"
            else:
                summary += "Stressnivået ditt er lavt. Bra jobbet!\n"

        # Aktivitetsanalyse
        if 'Distance' in row and pd.notna(row['Distance']):
            distance = row['Distance']
            summary += f"  - Treningsdistanse: {distance} km. Fortsett det gode arbeidet!\n"

        report.append(summary)

    return report

if __name__ == "__main__":
    # Tilpass filstiene til de nye mappene
    sleep_file = 'data/garmin/json-files/sleep_data.json'
    stress_file = 'data/garmin/json-files/stress_data.json'
    activities_file = 'data/garmin/json-files/activities_data.json'

    # Kombiner dataene
    combined_data = combine_health_data(sleep_file, stress_file, activities_file)

    # Generer rapport
    health_report = generate_health_report(combined_data)

    # Skriv ut rapporten
    for entry in health_report:
        print(entry)
