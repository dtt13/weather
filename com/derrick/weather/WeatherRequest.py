class WeatherRequest:

    def __init__(self, city):
        self.city = city

    def __eq__(self, other):
        if isinstance(other, WeatherRequest):
            return self.city == other.city
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return 'Request for %s, %s' % (self.city)

    def find_id(self):
        #TODO
        if self.city == 'Nashville':
            return '5003243'
        elif self.city == 'test':
            return '2172797'
        return ''