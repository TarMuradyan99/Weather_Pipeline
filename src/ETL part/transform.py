from extract import WeatherDataExctract

class TransformWeatherData(WeatherDataExctract):
    def __init__(self):
        super().__init__()
        self.daily_weather_df = self.extract_weather_data_daily()  # Store daily weather data
        self.hourly_weather_df = self.extract_weather_data_hourly()
    def transform_daily_data(self):
        self.daily_weather_df = self.daily_weather_df[['datetime', 'datetimeEpoch', 'tempmax', 'tempmin', 'temp',
                   'feelslikemax', 'feelslikemin', 'feelslike', 'dew', 'humidity',
                   'precip', 'precipprob', 'precipcover', 'preciptype', 'snow',
                   'snowdepth', 'windgust', 'windspeed', 'winddir', 'pressure',
                   'cloudcover', 'visibility', 'solarradiation', 'solarenergy', 'uvindex',
                   'severerisk', 'sunrise', 'sunriseEpoch', 'sunset', 'sunsetEpoch',
                   'moonphase', 'conditions', 'description', 'icon', 'stations', 'source','city'
                   ]]
        self.daily_weather_df["Celsius/tempmax"] = (self.daily_weather_df["tempmax"] - 32)*5/9
        self.daily_weather_df["Celsius/tempmin"] = (self.daily_weather_df["tempmin"] - 32) * 5 / 9
        self.daily_weather_df["Celsius/temp"] = (self.daily_weather_df["temp"] - 32) * 5 / 9

        return self.daily_weather_df

    def hourly_data_transform(self):
        self.hourly_weather_df = self.hourly_weather_df[['datetime','datetimeEpoch','temp','feelslike',
                                               'humidity','dew','precip','precipprob','snow','snowdepth',
                                               'preciptype','windgust','windspeed','winddir','pressure','visibility',
                                               'cloudcover','solarradiation','solarenergy','uvindex','severerisk','conditions',
                                               'icon','stations','source','city'
    ]]
        self.hourly_weather_df['precipprob'] = self.hourly_weather_df['precipprob'].fillna('sunny')
        return self.hourly_weather_df



