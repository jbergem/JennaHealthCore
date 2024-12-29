import pandas as pd
import json

def convert_time_to_minutes(time_str):
    """Konverterer tid (f.eks. '6h 40min') til minutter."""
    if isinstance(time_str, str):
        parts = time_str.split()
        total_minutes = 0
        for part in parts:
            if 'h' in part:
                total_minutes += int(part.replace('h', '')) * 60
            elif 'min' in part:
                total_minutes += int(part.replace('min', ''))
        return total_minutes
    return 0

def process_stress_data(csv_file, output_file):
    """Leser stressdata fra Garmin CSV-fil og konverterer til JSON."""
    # Les CSV-filen med riktig separator
    df = pd.read_csv(csv_file, sep=';')
    
    # Sjekk kolonnenavnene
    print("Kolonnenavn:", df.columns)
    
    # Endre navn på kolonner for konsistens
    df.rename(columns={
        'Date': 'Date',
        'Avg': 'Average',
        'Rest': 'Resting',
        'Low': 'Low Stress',
        'Medium Stress': 'Medium Stress',
        'High Stress': 'High Stress'
    }, inplace=True)
    
    # Konverter tid fra tekst til minutter for relevante kolonner
    for col in ['Resting', 'Low Stress', 'Medium Stress', 'High Stress']:
        df[col] = df[col].apply(convert_time_to_minutes)
    
    # Lagre som JSON
    stress_data = df.to_dict(orient='records')
    with open(output_file, 'w') as file:
        json.dump(stress_data, file, indent=4)
    
    print(f"Stressdata behandlet og lagret i: {output_file}")

if __name__ == "__main__":
    # Tilpass filstier basert på hvor CSV-en ligger
    input_csv = 'data/garmin/stress.csv'
    output_json = 'data/garmin/json-files/stress_data.json'
    process_stress_data(input_csv, output_json)
