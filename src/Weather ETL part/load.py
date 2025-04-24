import os.path

from transform import TransformWeatherData
from config import Config
from sqlalchemy import create_engine
import pandas as pd
import logging

config = Config()
engine = create_engine(config.DATA_BASE_PATH)


log_dir = r"C:\Users\User\PycharmProjects\Weather_Pipeline\src\Weather ETL part\logs"

file_path = os.path.join(log_dir,"etl.log")

logging.basicConfig(
    filename=file_path,
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    filemode='a'
)



class LoadWeatherData(TransformWeatherData):
    def __init__(self):
        super().__init__()
        self.daily_weather = self.transform_daily_data()
        self.hourly_weather = self.hourly_data_transform()

    def load_weather_data(self, dataframe, table_name, key_columns):
        try:
            quoted_keys = ', '.join([f'"{col}"' for col in key_columns])
            query = f'SELECT {quoted_keys} FROM weath."{table_name}"'
            existing = pd.read_sql(query, engine)
        except Exception as e:
            print(f"[ERROR] Failed to fetch existing records: {e}")
            logging.error(f"[ERROR] Failed to fetch existing records: {e}")
            return

        try:
            df = dataframe.merge(existing, on=key_columns, how='left', indicator=True)
            new_rows = df[df['_merge'] == 'left_only'].drop(columns=['_merge'])

            if new_rows.empty:
                print(f"[INFO] No new rows for {table_name}.")
                return

            new_rows.to_sql(table_name, con=engine, if_exists='append', index=False, schema='weath')  # 🔥 use global engine
            print(f"[INFO] Inserted {len(new_rows)} rows into {table_name}.")

        except Exception as e:
            print(f"[ERROR] Insert failed: {e}")
            logging.error(f"Insert failed for {table_name}: {e}")


logging.info("🚀 ETL job started")
s = LoadWeatherData()
s.load_weather_data(s.daily_weather, "daily_data_weather", ["city", "datetime"])
s.load_weather_data(s.hourly_weather, "hourly_data_weather", ["city", "datetimeEpoch"])
logging.info(" ETL job completed\n")
