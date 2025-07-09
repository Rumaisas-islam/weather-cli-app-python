import requests
import datetime
import os
from dotenv import load_dotenv

API_KEY = "3e2b60acb2d292c10e518760cb577065"

load_dotenv()
API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
HISTORY_FILE = "history.txt"

def kelvin_to_celsius(kelvin):
    return round(kelvin - 273.15, 2)

def fetch_weather(city):
    params = {
        "q": city,
        "appid": API_KEY
    }
    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        if response.status_code == 200:
            temp = kelvin_to_celsius(data["main"]["temp"])
            desc = data["weather"][0]["description"].title()
            time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_to_history(city, temp, desc, time)
            print(f"\n🌤️ Weather in {city.title()} at {time}")
            print(f"Temperature: {temp}°C")
            print(f"Condition: {desc}")
        else:
            print(f"❌ Error: {data.get('message', 'Unknown error')}")
    except Exception as e:
        print("⚠️ Failed to fetch weather data:", e)

def save_to_history(city, temp, desc, time):
    try:
        with open(HISTORY_FILE, "a") as f:
            f.write(f"{time} | {city.title()} | {temp}°C | {desc}\n")
    except Exception as e:
        print("⚠️ Couldn't save history:", e)

def view_history():
    if os.path.exists(HISTORY_FILE):
        print("\n📜 Weather Search History:\n")
        with open(HISTORY_FILE, "r") as f:
            lines = f.readlines()
            if lines:
                for line in lines[-10:]:  # Last 10 entries
                    print("•", line.strip())
            else:
                print("History is empty.")
    else:
        print("No history yet.")

def main_menu():
    while True:
        print("\n--- Weather CLI App ---")
        print("1. Check Weather")
        print("2. View Search History")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ").strip()
        if choice == "1":
            city = input("Enter city name: ").strip()
            if city:
                fetch_weather(city)
        elif choice == "2":
            view_history()
        elif choice == "3":
            print("Goodbye! Stay weather-aware! ☁️")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()
