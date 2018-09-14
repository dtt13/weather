import json

class WeatherResponse:

    def __init__(self, json):
        self.json = json

    def __eq__(self, other):
        if isinstance(other, WeatherResponse):
            return self.json == other.json
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return json.dumps(self.json, indent=4)