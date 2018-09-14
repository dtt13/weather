from com.derrick.weather.WeatherRequest import WeatherRequest
from com.derrick.weather.WeatherResponse import WeatherResponse
import requests


class WeatherClient:

    def __init__(self):
        self.api_keys = ['78bc09b444f73387ccf0770ea92fbe07']
        self.key_index = 0

    def request_weather(self, request):
        if not isinstance(request, WeatherRequest):
            raise TypeError('Request is not a WeatherRequest object')
        #  look up the city id and generate a URL
        url = 'http://api.openweathermap.org/data/2.5/weather?'
        city_id = request.find_id()
        if len(city_id) > 0:
            url += 'id=%s' % city_id
        else:
            url += 'city=%s' % request.city
        # create a request to the weather api
        # headers = {'x-api-key': self.__get_next_api_key()}
        headers = {}
        response = requests.get(url, headers=headers)
        # load json into WeatherResponse
        if response.status_code != 200:
            raise IOError('Request could not be completed')
        return WeatherResponse(response.text)

    def __get_next_api_key(self):
        next_key = self.api_keys[self.key_index]
        self.__increment_key_index()
        return next_key

    def __increment_key_index(self):
        self.key_index += 1
        if self.key_index >= len(self.api_keys):
            self.key_index = 0
