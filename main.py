import requests

def get_weather_forecast(api_key, city_name):
    base_url = "http://api.openweathermap.org/data/2.5/forecast"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"  # You can change this to "imperial" for Fahrenheit
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error fetching weather data.")
        return None

def main():
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    city_name = input("Enter city name: ")

    weather_data = get_weather_forecast(api_key, city_name)

    if weather_data:
        print(f"Weather forecast for {city_name}:")
        for forecast in weather_data["list"]:
            timestamp = forecast["dt_txt"]
            temperature = forecast["main"]["temp"]
            weather_description = forecast["weather"][0]["description"]
            print(f"At {timestamp}: Temperature: {temperature}°C, Description: {weather_description}")

if __name__ == "__main__":
    main()
