# ⛅ Weather CLI App (Python)

![GitHub Repo stars](https://img.shields.io/github/stars/Rumaisas-islam/weather-cli-app?style=flat-square)
![GitHub forks](https://img.shields.io/github/forks/Rumaisas-islam/weather-cli-app?style=flat-square)
![GitHub license](https://img.shields.io/github/license/Rumaisas-islam/weather-cli-app?style=flat-square)
![GitHub last commit](https://img.shields.io/github/last-commit/Rumaisas-islam/weather-cli-app?style=flat-square)
![Python](https://img.shields.io/badge/Made%20with-Python-blue?style=flat-square)

> A sleek **Weather CLI Application** using Python and OpenWeatherMap API.  
> Built with real-time weather updates, search history, `.env` support — great for beginners & API learners!

---

## 📌 Features

- 🌤️ Real-time weather data by city name
- 🌡️ Temperature in Celsius (converted from Kelvin)
- ✅ API integration using `.env` file
- 📝 Saves search history (last 10 entries)
- 📂 Creates `history.txt` automatically
- ⚠️ Error handling for wrong cities & network issues
- 🧠 Beginner-friendly, modular, secure

---

## 🚀 How to Run

### 1. Clone the repo

```bash
git clone https://github.com/Rumaisas-islam/weather-cli-app.git
cd weather-cli-app
```

### 2. Install dependencies

```bash
pip install requests python-dotenv
```

### 3. Create a `.env` file in the root

```env
API_KEY=your_openweathermap_api_key_here
```

> ❗ Don’t share this file — it's already excluded by `.gitignore`.

### 4. Run the application

```bash
python weather_app.py
```

---

## ⚙️ Project Structure

```
weather-cli-app/
├── weather_app.py          # Main Python script
├── .env                    # Contains your API key (excluded from Git)
├── .env.example            # Sample template
├── history.txt             # Created automatically on first run
├── .gitignore
├── LICENSE
├── README.md
└── test/
    └── test_weather_app.py (optional)
```

---

## 📷 Sample Output

```plaintext
--- Weather CLI App ---
1. Check Weather
2. View Search History
3. Exit

Enter your choice (1-3): 1
Enter city name: Karachi

🌤️ Weather in Karachi at 2025-07-09 06:55:53
Temperature: 28.33°C
Condition: Scattered Clouds
```

---

## 🧠 Technologies Used

* Python 3.x
* OpenWeatherMap API
* `requests`, `python-dotenv`
* File Handling
* Command Line Interface

---

## 🏗️ Future Enhancements

* Add ASCII/emoji icons for weather
* Weekly forecasts
* Export to CSV/JSON
* Add color styling with `colorama`
* GUI version using Tkinter

---

## 🧾 License

Licensed under the **MIT License** — see the [LICENSE](LICENSE) file.

---

## 🙌 Support

If this helped you, give the repo a ⭐ and share with others!
PRs and contributions are warmly welcome.

---

## 🏷️ Tags

`#python` `#weather-api` `#cli-app` `#openweathermap` `#file-handling` `#api-integration` `#beginner-project`