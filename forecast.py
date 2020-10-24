from day_name import get_day
import requests

api_key = "YOUR API KEY"  # Your api key with the weatherbit.io website


class Day:
    """
    A class used to save the data about a day forecast.
    """
    def __init__(self, date, maxt, mint, weather, icon, day_name):
        self.date = date
        self.day_name = day_name
        self.maxt = maxt
        self.mint = mint
        self.weather = weather
        self.icon = icon


class Forecast:
    """
    A class used to make the forecast

    ...

    Attributes
    ----------
    city : str
        a string represent the city we want the forecast to be on
    days : str
        a number represent how much days weather we want to get.
    content: list
        a list contains Days variables with the forecast data.


    Methods
    -------
    make_content
        create the content attribute with the correct data according the days and city attributes.
    """
    def __init__(self, city, days):
        self.city = city
        self.days = days

    def make_content(self):
        self.content = []
        req = requests.get(f"http://api.weatherbit.io/v2.0/forecast/daily?city={self.city}&key={api_key}&lang=iw&days={self.days}")
        if req.reason == 'OK':
            data = req.json()['data']
            for day in data:
                new_day = Day(day['datetime'], day['max_temp'], day['min_temp'], day['weather']['description'], day['weather']['icon'], get_day(day['datetime']))
                self.content.append(new_day)

