import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modules.jenna_brain import load_data, analyze_sleep, analyze_hrv, analyze_pulse

if __name__ == "__main__":
    # Laste inn data
    data = load_data('data/garmin/extended_data.json')

    # Analysere søvn
    sleep_result = analyze_sleep(data['sleep'])
    print(sleep_result)

    # Analysere HRV
    hrv_result = analyze_hrv(data['hrv'])
    print(hrv_result)

    # Analysere hvilepuls
    pulse_result = analyze_pulse(data['pulse'])
    print(pulse_result)
