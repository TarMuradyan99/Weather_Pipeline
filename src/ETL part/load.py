from transform import TransformWeatherData
from config import Config

config = Config()  # ✅ Create an instance first


class LoadWeatherData(TransformWeatherData):
    def __init__(self):
        super().__init__()
        self.daily_weather = self.transform_daily_data()
        self.hourly_weather = self.hourly_data_transform()

    def load_weather_data(self,datafame,db_table_name):
        try:
            datafame.to_sql(
                db_table_name,
                con = config.DATA_BASE_PATH,
                if_exists = 'replace',
                index = False,
                schema = 'weath'
            )
        except Exception as e:
            print(f"Something went wrong:{e}")


s = LoadWeatherData()
print(s.load_weather_data(s.daily_weather_df,"daily_data_weather"))
print(s.load_weather_data(s.hourly_weather_df,"hourly_data_weather"))