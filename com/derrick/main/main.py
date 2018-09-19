from com.derrick.weather import *


def main():
    client = WeatherClient.WeatherClient()
    request = WeatherRequest.WeatherRequest("Nashville")
    response = client.request_weather(request)
    print response
    print "Nashville Weather:"
    print "\tcurrent temp: %.1fF" % response.get_current_temp()
    print "\tmax temp:     %.1fF" % response.get_max_temp()
    print "\tmin temp:     %.1fF" % response.get_min_temp()
    print "\tconditions:   %s" % response.get_conditions()
    print "\tpressure:     %d" % response.get_current_pressure()
    print "\thumidity:     %d" % response.get_current_humidity()
    print "\twind speed:   %.1f mph" % response.get_wind_speed()

if __name__ == '__main__':
    main()