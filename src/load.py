import pandas as pd
import sqlalchemy
from transform import transform_daily_data,hourly_data_transform
from config import config
import psycopg2


daily_weather = transform_daily_data()
hourly_weather = hourly_data_transform()

def load_weather_data(datafame,db_table_name):
    datafame.to_sql(
        db_table_name,
        con = config.DATA_BASE_PATH,
        if_exists = 'replace',
        index = False,
        schema = 'weath'
    )

load_weather_data(daily_weather,"daily_data_weather")
load_weather_data(hourly_weather,"hourly_data_weather")