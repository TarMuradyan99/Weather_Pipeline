import pandas as pd
import requests
from config import Config

class WeatherDataExctract(Config):
    def __init__(self):
        super().__init__()
        self.data_frame = pd.DataFrame()
    def extract_weather_data_daily(self):
        all_data = []
        try:
            for city in self.DEFAULT_CITY:
                response = requests.get(f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?unitGroup=us&key={self.API_KEY}&contentType=json")
                print(f"data fetched without any issue :{response}")
                batch_of_data = response.json()
                df = pd.DataFrame(batch_of_data['days'])
                df["city"] = batch_of_data["address"]
                all_data.append(df)
        except requests.exceptions.HTTPError as e:
            return f"HTTP ERROR is {e}"
        except requests.exceptions.ConnectionError as c:
            return f"There is some connection issue please check"
        except requests.exceptions.Timeout as t:
            return f"Timed out {t}"
        except requests.exceptions.RequestException as e:
            return f"An error occured: {e}"

        return  pd.concat(all_data,ignore_index=True) if all_data else pd.DataFrame()


    def extract_weather_data_hourly(self):
        all_data = []
        try:
            for city in self.DEFAULT_CITY:
                response = requests.get(f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?unitGroup=us&key={self.API_KEY}&contentType=json")
                print(f"data fetched without any issue :{response}")
                batch_of_data = response.json()
                hourly = batch_of_data.get('days',[])
                for hour in hourly:
                    hours_data = hour.get('hours',[])
                    df = pd.DataFrame(hours_data)
                    df["city"] = batch_of_data["address"]
                    all_data.append(df)
        except requests.exceptions.HTTPError as e:
            return f"HTTP ERROR is {e}"
        except requests.exceptions.ConnectionError as c:
            return f"There is some connection issue please check"
        except requests.exceptions.Timeout as t:
            return f"Timed out{t}"
        except requests.exceptions.RequestException as e:
            return f"An error occured: {e}"
        return pd.concat(all_data,ignore_index = True) if all_data else  pd.DataFrame()




