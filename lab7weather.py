import requests
import os
from dotenv import load_dotenv
load_dotenv()

def get_weather_openweathermap(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric',
        'lang': 'ru'  
    }
    response = requests.get(base_url, params=params)
    response.raise_for_status() 
    weather_data = response.json()
    temperature = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    pressure = weather_data['main']['pressure']
    weather_description = weather_data['weather'][0]['description']
    wind_speed = weather_data['wind']['speed']
    city = weather_data['name']
    country = weather_data['sys']['country']
    print(f"ПОГОДА В ГОРОДЕ: {city}, {country}")
    print(f"Температура: {temperature}°C")
    print(f"Влажность: {humidity}%")
    print(f"Давление: {pressure} гПа")
    print(f"Описание: {weather_description.capitalize()}")
    print(f"Скорость ветра: {wind_speed} м/с")


if __name__ == "__main__":
    CITY = "Sankt-Peterburg"
    API_KEY = os.getenv('API1_KEY')
    
    get_weather_openweathermap(CITY, API_KEY)