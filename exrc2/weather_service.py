import requests
print(requests.__version__)

def get_weather_data(city):
 """Fonction qui fait un appel API réel"""
 url = f"http://api.weather.com/v1/weather?city={city}"
 response = requests.get(url)
 return response.json()

def get_temperature(city):
 """Fonction qui utilise get_weather_data"""
 weather_data = get_weather_data(city)
 return weather_data.get('temperature', 'N/A')

def is_sunny(city):
 """Fonction qui utilise get_weather_data"""
 weather_data = get_weather_data(city)
 return weather_data.get('condition') == 'sunny'
