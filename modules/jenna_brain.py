import json

def load_data(file_path):
    """Laster inn data fra en JSON-fil."""
    with open(file_path, 'r') as file:
        return json.load(file)

def analyze_sleep(data):
    """Analyserer søvnkvalitet og returnerer anbefalinger."""
    total_sleep = sum([entry['duration'] for entry in data])
    if total_sleep < 6 * len(data):
        return "Du har sovet mindre enn 6 timer i snitt. Planlegg en tidlig kveld."
    return "Søvn ser bra ut! Fortsett det gode arbeidet."

def analyze_hrv(data):
    """Analyserer HRV og gir anbefalinger."""
    avg_hrv = sum([entry['hrv'] for entry in data]) / len(data)
    if avg_hrv < 50:
        return f"HRV-en din er lav ({avg_hrv:.1f}). Planlegg restitusjon."
    return f"HRV-en din er bra ({avg_hrv:.1f}). Fortsett det gode arbeidet!"

def analyze_pulse(data):
    """Analyserer hvilepuls og gir anbefalinger."""
    avg_pulse = sum([entry['resting_pulse'] for entry in data]) / len(data)
    if avg_pulse > 70:
        return f"Hvilepulsen din er høy ({avg_pulse:.1f}). Kanskje du bør roe ned?"
    return f"Hvilepulsen din er god ({avg_pulse:.1f}). Bra jobbet!"
