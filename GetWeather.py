from requests import get


def convert(seconds, time_zone):
    seconds = seconds % (24 * 3600)
    hour = (seconds + time_zone) // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return "%d:%02d:%02d" % (hour, minutes, seconds)


class WeatherInfo:
    def __init__(self, city_name, API_key='2656690346203e6706d0b586863add0d'):
        # GET INFO
        self.name = city_name
        self.API_key = API_key
        self.url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(city_name, API_key)
        self.res = get(self.url)
        self.data = self.res.json()
        self.country = self.data['sys']['country']

        # WEATHER VARIABLES
        self.timezone = self.data['timezone']
        self.temperature = round((self.data['main']['temp']) - 273.15, 1)
        self.sensed_temperature = round(int(self.data['main']['feels_like']) - 275.15, 1)
        self.pressure = self.data['main']['pressure']
        self.humidity = self.data['main']['humidity']
        self.sunrise = convert(int(self.data['sys']['sunrise']), self.timezone)
        self.sunset = convert(int(self.data['sys']['sunset']), self.timezone)
        self.description = self.data['weather'][0]['main']

    # GET STRING WITH INFORMATION AND UNIT
    def getTemperature(self):
        return str(self.temperature) + "°C"

    def getSensedTemperature(self):
        return str(self.sensed_temperature) + "°C"

    def getPressure(self):
        return str(self.pressure) + "hPa"

    def getHumidity(self):
        return str(self.humidity) + "%"

    def getSunrise(self):
        return str(self.sunrise)

    def getSunset(self):
        return str(self.sunset)

    def getDescription(self):
        return str(self.description)

    def summary(self):
        print("Temperature: {}\n".format(self.getTemperature()) +
              "Sensed temperature: {}\n".format(self.getSensedTemperature()) +
              "Pressure: {}\n".format(self.getPressure()) +
              "Humidity: {}\n".format(self.getHumidity()) +
              "Sunrise: {}\n".format(self.getSunrise()) +
              "Sunset: {}\n".format(self.getSunset()) +
              "Description: {}\n".format(self.description) +
              "Timezone: {}".format(self.timezone)
              )

        print("\nData generated for {}, {}".format(self.name, self.country))


if __name__ == '__main__':
    data = WeatherInfo('New York')
    data.summary()
