import pandas as pd
import json

def process_sleep_data(csv_file, output_file):
    """Leser Garmin Sleep CSV-data og konverterer til JSON."""
    
    # Les CSV-filen med riktig separasjon og encoding
    df = pd.read_csv(csv_file, sep=',', encoding='utf-8', decimal=',')  # 'decimal' for å håndtere komma i tall

    # Sjekk kolonneoverskriftene
    print(f"Kolonnenavn funnet i CSV: {list(df.columns)}")
    
    # Fjern eventuelle whitespace fra kolonnenavnene
    df.columns = df.columns.str.strip()

    # Konverter 'Date'-kolonnen til datetime
    df['Date'] = pd.to_datetime(df['Date'] + ' 2024', format='%d %b %Y', errors='coerce')

    # Sjekk for gyldige datoer
    if df['Date'].isna().all():
        print("Ingen gyldige datoer funnet. Sjekk CSV-filen for formatfeil.")
        return
    
    # Funksjon for å konvertere tid (f.eks. '6h 40min') til minutter
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

    # Kolonner som trenger tid-konvertering
    time_columns = ['Duration', 'Sleep Need', 'Bedtime', 'Wake Time']
    for col in time_columns:
        if col in df.columns:
            df[col] = df[col].apply(convert_time_to_minutes)
    
    # Håndter spesialtegn og feil i dataene
    df = df.replace({'--': None}, regex=True)  # Fjerner '--'
    
    # Fjern eventuelle whitespace og erstatt "grad"-tegn
    for col in df.columns:
        if df[col].dtype == object:
            df[col] = df[col].str.replace('°', '', regex=False)
            df[col] = df[col].str.replace(',', '.', regex=False)  # Bytt komma til punktum for tall
    
    # Konverter dataframe til JSON-format
    sleep_data = df.to_dict(orient='records')

    # Lagre som JSON
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(sleep_data, file, ensure_ascii=False, indent=4)

    print(f"Søvn-data behandlet og lagret i: {output_file}")

if __name__ == "__main__":
    # Tilpass filstier basert på hvor CSV-en ligger
    input_csv = 'data/garmin/sleep.csv'
    output_json = 'data/garmin/json-files/sleep_data.json'
    process_sleep_data(input_csv, output_json)
