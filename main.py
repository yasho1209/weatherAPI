import requests

API_KEY = "YOUR_API_KEY"

geo_url = "http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&limit={limit}&appid={API_KEY}"

weather_url = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"

def get_city_info():
    # Examples: city_name = "New York", state_code = "NY", country_code = "US", limit = 1
    # Examples: city_name = "Mumbai", state_code = "Maharashtra", country_code = "India", limit = 1
    city_name = input("Enter the name of the city: ")
    state_code = input("Enter the state code: ")
    country_code = input("Enter the country code: ")
    limit = input("Enter the limit: ") # Can change tit to always be 1
    return get_geo_info(city_name, state_code, country_code, limit)

def get_geo_info(city_name, state_code, country_code, limit):
    url = geo_url.format(city_name=city_name, state_code=state_code, country_code=country_code, limit=limit, API_KEY=API_KEY)
    response = requests.get(url)
    lat = response.json()[0]["lat"]
    lon = response.json()[0]["lon"]
    return get_weather_info(lat, lon)

def get_weather_info(lat, lon):
    url = weather_url.format(lat=lat, lon=lon, API_KEY=API_KEY)
    response = requests.get(url)
    print(response.json())

get_city_info()