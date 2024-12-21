import requests

api_key = "b7feb2d20b3e8856fe04e4df57fe4bc7"
lang = "kr"

def get_weather_info(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&lang={lang}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

get_weather_info("ulsan")