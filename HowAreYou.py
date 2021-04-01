from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.storage.jsonstore import JsonStore
from kivymd.uix.dialog import MDDialog
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase
from kivy.core.window import Window
from plots import *

from helpers import screen_helper
from GetWeather import *
Builder.load_string(screen_helper)  # load code in kv language from different file


# declare Screens and Tabs
class MenuScreen(Screen):
    pass


class SettingsScreen(Screen):
    pass


class Tab(MDFloatLayout, MDTabsBase):
    pass


class HowAreYouApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.size = (800, 640)
        self.sm = ScreenManager()
        self.store = JsonStore('user_data.json')
        if not self.store.get('user')['first']:
            city = self.store.get('user')['city']
            self.weather = WeatherInfo(city)

    def build(self):
        self.sm.add_widget(SettingsScreen(name='settings'))
        self.sm.add_widget(MenuScreen(name='menu'))         # add screens
        self.sm.current = 'menu'

        if self.store.get('user')['first']:
            self.sm.current = 'settings'        # if it is first usage - show settings

        self.theme_cls.primary_palette = self.store.get('user')['color']                    # set color and theme
        self.theme_cls.theme_style = self.store.get('user')['theme']

        return self.sm

    # SETTINGS FUNCTIONS
    def save_user_data(self):
        user_input = {'name': self.sm.get_screen('settings').ids.username.text,
                      'city': self.sm.get_screen('settings').ids.location.text,
                      'feeling': self.sm.get_screen('settings').ids.feeling_rate.text,
                      'color': self.sm.get_screen('settings').ids.set_color.text
                      }

        colors = [
            'Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue',
            'Cyan', 'Teal', 'Green', 'LightGreen', 'Lime', 'Yellow', 'Amber', 'Orange',
            'DeepOrange', 'Brown', 'Gray', 'BlueGray'
        ]

        dialog = MDDialog(size_hint=(0.5, None))
        flag = 0

        # check name
        if user_input['name'] == "":
            name = "None"
            dialog.title = "Name should be at least one character."
            dialog.text = "Name set to None."
            dialog.open()
            flag = 1
        else:
            name = user_input['name'][0:20]

        # check city
        if user_input['city'] == "":
            city = "Poznań"
            dialog.title = "Name of the city should be at least one character."
            dialog.text = "City name set to Poznań."
            dialog.open()
            flag = 1
        else:
            city = user_input['city']

        # download weather data
        try:
            self.weather = WeatherInfo(city)
        except KeyError:
            dialog.title = "ERROR: The city was not found!"
            dialog.text = "Hint: Try to check if the name is proper or type the name of bigger city..."
            dialog.open()
            flag = 1

        # check if feeling rate is a number
        try:
            feeling = int(user_input['feeling'])
        except ValueError:
            feeling = 1
            dialog.title = "Feeling rate should be a number!"
            dialog.text = "Feeling rate set to one."
            dialog.open()
            flag = 1

        if user_input['color'] in colors:
            self.theme_cls.primary_palette = user_input['color']
            color = user_input['color']
        else:
            color = "Orange"
            dialog.title = "Try different color :("
            dialog.text = "Available options are: ‘Red’, ‘Pink’, ‘Purple’, ‘DeepPurple’, " \
                          "‘Indigo’, ‘Blue’, ‘LightBlue’, ‘Cyan’, ‘Teal’, ‘Green’, ‘LightGreen’," \
                          " ‘Lime’, ‘Yellow’, ‘Amber’, ‘Orange’, ‘DeepOrange’, ‘Brown’, ‘Gray’, ‘BlueGray’."
            dialog.open()
            flag = 1

        # put the data in the storage
        self.store.put('user',
                       name=name,
                       city=city,
                       feeling=max(1, min(feeling, 10)),
                       theme=self.theme_cls.theme_style,
                       color=color,
                       first=False  # if user once entered the data the screen will not appear as a welcome screen
                       )

        # if no problems load the spinner and leave the settings
        if flag == 0:
            spinner = self.sm.get_screen('settings').ids.save_spinner

            spinner.active = False          #
            spinner.determinate = True      # animation of spinner
            spinner.active = True           #

            self.sm.get_screen('settings').ids.menu_button.disabled = False  # enable go to menu button

    def switch_theme(self):
        if self.theme_cls.theme_style == "Dark":
            self.theme_cls.theme_style = "Light"
        else:
            self.theme_cls.theme_style = "Dark"

    # MENU FUNCTIONS
    def sync_icons_labels(self):
        icons = {'Clear': 'white-balance-sunny',
                 'Clouds': 'weather-partly-cloudy',
                 'Drizzle': 'weather-pouring',
                 'Rain': 'weather-partly-rainy',
                 'Thunderstorm': 'weather-lightning',
                 'Snow': 'weather-snowy-heavy',
                 'Mist': 'weather-fog',                         # Description from OpenWeather: Icon KivyMD
                 'Smoke': 'weather-fog',
                 'Haze': 'weather-fog',
                 'Dust': 'weather-fog',
                 'Fog': 'weather-fog',
                 'Sand': 'weather-fog',
                 'Ash': 'weather-fog',
                 'Squall': 'weather-windy-variant',
                 'Tornado': 'weather-hurricane',
                 'error': 'weather-cloudy-alert'
                 }

        description = self.weather.getDescription()
        temperature = self.weather.getTemperature()
        sensed_temperature = self.weather.getSensedTemperature()
        sunrise = self.weather.getSunrise()                             # save weather data
        sunset = self.weather.getSunset()
        humidity = self.weather.getHumidity()
        pressure = self.weather.getPressure()

        weather_ico = self.sm.get_screen('menu').ids.weather_icon
        weather_label1 = self.sm.get_screen('menu').ids.weather_label1
        weather_label2 = self.sm.get_screen('menu').ids.weather_label2
        sunrise_label = self.sm.get_screen('menu').ids.sunrise_label            # create variables for icons and labels
        sunset_label = self.sm.get_screen('menu').ids.sunset_label
        pressure_label = self.sm.get_screen('menu').ids.pressure_label
        humidity_label = self.sm.get_screen('menu').ids.humidity_label
        text = self.sm.get_screen('menu').ids.hello_label

        try:
            weather_ico.icon = icons[description]
        except KeyError:
            weather_ico.icon = icons['error']
        weather_label1.text = temperature
        weather_label2.text = sensed_temperature            # set icons and text
        sunrise_label.text = sunrise
        sunset_label.text = sunset
        pressure_label.text = pressure
        humidity_label.text = humidity
        text.text = "Hi {}, how are you today?".format(self.store.get('user')['name'])

    def save_survey(self):
        survey_input = {'feeling': self.sm.get_screen('menu').ids.feeling_rate1.text,
                        'sleep': self.sm.get_screen('menu').ids.sleep_rate.text,
                        'activity': self.sm.get_screen('menu').ids.activity_rate.text,
                        }

        dialog = MDDialog(size_hint=(0.5, None))

        try:
            feeling = int(survey_input['feeling'])
        except ValueError:
            feeling = 1
            dialog.title = "Feeling rate should be a number!"
            dialog.text = "Feeling rate set to one."
            dialog.open()

        try:
            sleep_rate = int(survey_input['sleep'])
        except ValueError:
            sleep_rate = 7
            dialog.title = "Hours should be a number."
            dialog.text = "Hours set to 7."
            dialog.open()

        ratings = {'very low': 0, 'low': 3, 'medium': 5, 'high': 8, 'very high': 10}
        if survey_input['activity'] in ratings.keys():
            activity_rate = ratings[survey_input['activity']]
        else:
            activity_rate = 'medium'
            dialog.title = "Wrong input. Activity rate set to medium."
            dialog.text = "Type very low, low, medium, high or very high."
            dialog.open()

        feeling_data = self.store.get('plots')['feeling_data']
        sleep_data = self.store.get('plots')['sleep_data']         # get the actual data
        activity_data = self.store.get('plots')['activity_data']

        if len(feeling_data) > 31:
            feeling_data.pop(0)
        feeling_data.append(feeling)

        if len(sleep_data) > 31:
            sleep_data.pop(0)                   # store the data only from one month
        sleep_data.append(sleep_rate)

        if len(activity_data) > 31:
            activity_data.pop(0)
        activity_data.append(activity_rate)

        temperature = self.weather.temperature
        sensed_temperature = self.weather.sensed_temperature
        humidity = self.weather.humidity
        pressure = self.weather.pressure

        temperature_rate = round(5 * temperature / 15, 2)  # 15 celcius degrees is average temperatue on the Earth
        sensed_temperature_rate = round(5 * sensed_temperature / 15, 2)
        humidity_rate = round(5 * humidity / 60, 2)  # 60% is average humidity on the Earth
        pressure_rate = round(5 * pressure / 1013, 2)  # 1013hPa is average pressure on the Earth

        temperature_data = self.store.get('plots')['temperature_data']
        sensed_temperature_data = self.store.get('plots')['sensed_temperature_data']
        humidity_data = self.store.get('plots')['humidity_data']
        pressure_data = self.store.get('plots')['pressure_data']

        if len(temperature_data) > 31:
            temperature_data.pop(0)
        temperature_data.append(temperature_rate)

        if len(sensed_temperature_data) > 31:
            sensed_temperature_data.pop(0)
        sensed_temperature_data.append(sensed_temperature_rate)

        if len(humidity_data) > 31:
            humidity_data.pop(0)
        humidity_data.append(humidity_rate)

        if len(pressure_data) > 31:
            pressure_data.pop(0)
        pressure_data.append(pressure_rate)

        self.store.put('plots',
                       feeling_data=feeling_data,
                       sleep_data=sleep_data,
                       activity_data=activity_data,
                       temperature_data=temperature_data,
                       sensed_temperature_data=sensed_temperature_data,
                       humidity_data=humidity_data,
                       pressure_data=pressure_data
                       )

    def update_plots(self):
        feeling_data = self.store.get('plots')['feeling_data']
        sleep_data = self.store.get('plots')['sleep_data']                      # get the actual data
        activity_data = self.store.get('plots')['activity_data']
        temperature_data = self.store.get('plots')['temperature_data']
        sensed_temperature_data = self.store.get('plots')['sensed_temperature_data']
        humidity_data = self.store.get('plots')['humidity_data']
        pressure_data = self.store.get('plots')['pressure_data']

        days = len(feeling_data)  # every lst has the same length

        if self.theme_cls.theme_style == "Dark":
            plotData(days, feeling_data, sleep_data, data_1_label="Feeling rate", data_2_label="Sleep hours", filename="feel-sleep.png", dark=True)
            plotData(days, feeling_data, activity_data, data_1_label="Feeling rate", data_2_label="Activity rate", filename="feel-activ.png", dark=True)
            plotData(days, feeling_data, temperature_data, data_1_label="Feeling rate", data_2_label="Temperature", filename="feel-temp.png", dark=True)
            plotData(days, feeling_data, sensed_temperature_data, data_1_label="Feeling rate", data_2_label="Sensed temperature", filename="feel-sens.png", dark=True)
            plotData(days, feeling_data, humidity_data, data_1_label="Feeling rate", data_2_label="Humidity", filename="feel-humi.png", dark=True)
            plotData(days, feeling_data, pressure_data, data_1_label="Feeling rate", data_2_label="Pressure", filename="feel-pres.png", dark=True)

        else:
            plotData(days, feeling_data, sleep_data, data_1_label="Feeling rate", data_2_label="Sleep hours", filename="feel-sleep.png")
            plotData(days, feeling_data, activity_data, data_1_label="Feeling rate", data_2_label="Activity rate", filename="feel-activ.png")
            plotData(days, feeling_data, temperature_data, data_1_label="Feeling rate", data_2_label="Temperature", filename="feel-temp.png")
            plotData(days, feeling_data, sensed_temperature_data, data_1_label="Feeling rate", data_2_label="Sensed temperature", filename="feel-sens.png")
            plotData(days, feeling_data, humidity_data, data_1_label="Feeling rate", data_2_label="Humidity", filename="feel-humi.png")
            plotData(days, feeling_data, pressure_data, data_1_label="Feeling rate", data_2_label="Pressure", filename="feel-pres.png")




HowAreYouApp().run()
