from extract import extract_weather_data
import pandas as pd
from extract import city



data_by_json = extract_weather_data()
daily_weather_df = pd.DataFrame(data_by_json['days'])

def transform_daily_data():
    daily_weather_df = pd.DataFrame(data_by_json['days'])
    daily_weather_df = daily_weather_df[['datetime', 'datetimeEpoch', 'tempmax', 'tempmin', 'temp',
               'feelslikemax', 'feelslikemin', 'feelslike', 'dew', 'humidity',
               'precip', 'precipprob', 'precipcover', 'preciptype', 'snow',
               'snowdepth', 'windgust', 'windspeed', 'winddir', 'pressure',
               'cloudcover', 'visibility', 'solarradiation', 'solarenergy', 'uvindex',
               'severerisk', 'sunrise', 'sunriseEpoch', 'sunset', 'sunsetEpoch',
               'moonphase', 'conditions', 'description', 'icon', 'stations', 'source',
               ]]
    daily_weather_df["Celsius/tempmax"] = (daily_weather_df["tempmax"] - 32)*5/9
    daily_weather_df["Celsius/tempmin"] = (daily_weather_df["tempmin"] - 32) * 5 / 9
    daily_weather_df["Celsius/temp"] = (daily_weather_df["temp"] - 32) * 5 / 9
    daily_weather_df['city'] = city

    return daily_weather_df

def hourly_data_transform():
    hourly_weathers = []
    for day in data_by_json.get('days',[]):
        date = day.get("datetime")
        for hour in day.get("hours",[]):
            hour["date"] = date
            hourly_weathers.append(hour)
    hourly_weather_df = pd.DataFrame(hourly_weathers)
    hourly_weather_df['city'] = city
    return hourly_weather_df

