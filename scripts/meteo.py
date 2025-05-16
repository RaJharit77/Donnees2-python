import requests
import pandas as pd
from datetime import datetime
import os

# Configuration
API_KEY = "1aeb4aad4fd664aff93ff8b9aa0284d0"  # Remplacez par votre clé API OpenWeather
CITY = "Antananarivo"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
UNITS = "metric"
OUTPUT_DIR = "data"  # Dossier où sauvegarder les fichiers CSV

# Créer le dossier de sortie s'il n'existe pas
os.makedirs(OUTPUT_DIR, exist_ok=True)

def get_weather_data():
    """Extrait les données météo depuis l'API OpenWeather"""
    params = {
        'q': CITY,
        'units': UNITS,
        'appid': API_KEY
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Lève une exception pour les codes HTTP 4xx/5xx
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la requête API: {e}")
        return None


def transform_data(weather_data):
    """Transforme les données brutes en DataFrame"""
    if not weather_data:
        return None

    # Extraction des données pertinentes
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    transformed_data = {
        'ville': weather_data.get('name', ''),
        'température (°C)': weather_data.get('main', {}).get('temp', ''),
        'humidité (%)': weather_data.get('main', {}).get('humidity', ''),
        'pression (hPa)': weather_data.get('main', {}).get('pressure', ''),
        'description': weather_data.get('weather', [{}])[0].get('description', ''),
        'date_requête': current_time
    }

    # Création du DataFrame
    df = pd.DataFrame([transformed_data])
    return df


def save_to_csv(df):
    """Sauvegarde les données dans un fichier CSV"""
    if df is None or df.empty:
        print("Aucune donnée à sauvegarder")
        return

    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"meteo_{today}.csv"
    filepath = os.path.join(OUTPUT_DIR, filename)

    # Sauvegarde en CSV (sans index et en mode 'w' pour écraser le fichier existant)
    df.to_csv(filepath, index=False, mode='w')
    print(f"Données sauvegardées dans {filepath}")


def main():
    # ETL Process
    print("Début de l'extraction des données météo...")

    # Extraction
    weather_data = get_weather_data()

    # Transformation
    weather_df = transform_data(weather_data)

    # Chargement
    if weather_df is not None:
        save_to_csv(weather_df)
        print("\nDonnées extraites:")
        print(weather_df)
    else:
        print("Aucune donnée à sauvegarder.")


if __name__ == "__main__":
    main()