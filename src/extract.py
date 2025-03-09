import pandas as pd
import requests
import json
from config import config


config.DEFAULT_CITY = input()
city = config.DEFAULT_CITY
api_key = config.API_KEY
def extract_weather_data():
    try:

        response = requests.get(f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?unitGroup=us&key={api_key}&contentType=json")
        print(f"data fetched without any issue :{response}")

    except requests.exceptions.HTTPError as e:
        return f"HTTP ERROR is {e}"
    except requests.exceptions.ConnectionError as c:
        return f"There is some connection issue please check"
    except requests.exceptions.TimeOut as t:
        return "Timed out"
    except requests.exceptions.RequestException as e:
        return f"An error occured: {e}"

    return  response.json()



