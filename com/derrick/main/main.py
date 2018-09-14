from com.derrick.weather import *


def main():
    client = WeatherClient.WeatherClient()
    request = WeatherRequest.WeatherRequest("test") #TODO
    print(client.request_weather(request))


if __name__ == '__main__':
    main()