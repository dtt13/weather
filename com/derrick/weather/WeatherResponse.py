import json
from datetime import datetime
from enum import Enum

class TempUnit(Enum):
    Kelvin = 1
    Celcius = 2
    Fahrenheit = 3

class WeatherResponse:

    def __init__(self, json_response):
        self.__json = json.loads(json_response)
        self.timestamp = datetime.utcnow()

    def get_sunrise(self):
        return datetime(second=self.__json['sys']['sunrise'])

    def get_sunset(self):
        return datetime(second=self.__json['sys']['sunset'])

    def get_current_temp(self, unit=TempUnit.Fahrenheit):
        return self.__convert_temp_units(self.__json['main']['temp'], unit)

    def get_max_temp(self, unit=TempUnit.Fahrenheit):
        return self.__convert_temp_units(self.__json['main']['temp_max'], unit)

    def get_min_temp(self, unit=TempUnit.Fahrenheit):
        return self.__convert_temp_units(self.__json['main']['temp_min'], unit)

    def get_current_pressure(self):
        return self.__json['main']['pressure']

    def get_current_humidity(self):
        return self.__json['main']['humidity']

    def get_wind_speed(self):
        return self.__json['wind']['speed']

    def get_wind_direction(self):
        return self.__json['wind']['deg']

    def get_conditions(self):
        return self.__json['weather'][0]['main']

    @staticmethod
    def __convert_temp_units(kelvin, unit):
        if unit == TempUnit.Celcius:
            return kelvin - 273.0
        elif unit == TempUnit.Fahrenheit:
            return ((9 * (kelvin - 273.0)) / 5.0) + 32.0
        return kelvin

    def __eq__(self, other):
        if isinstance(other, WeatherResponse):
            return self.__json == other.__json and self.timestamp == other.timestamp
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return json.dumps(self.__json, indent=4)
