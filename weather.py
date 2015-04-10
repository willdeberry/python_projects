#!/usr/bin/python

from argparse import ArgumentParser
from prettytable import PrettyTable
import requests
import time

def get_weather(zipcode):
    ''' Retrieve json from openweather.org '''
    r = requests.get('http://api.openweathermap.org/data/2.5/forecast/daily?q={}&cnt=10&units=imperial&mode=json'.format(zipcode))
    if r.status_code == 200:
        return r.json()

def get_days(data):
    ''' Return full list of days from the weather json '''
    return data['list']

def build_table(forecast):
    ''' Iterate over list and build table a column for each day '''
    table = PrettyTable()
    table.add_column("Date",["High","Low","Forecast","Humidity","Wind Speed"])
    for day in range(len(forecast)):
        date = time.strftime('%Y.%m.%d', time.localtime(forecast[day]['dt']))
        degree = u'\N{DEGREE SIGN}'.encode('utf-8')
        high = forecast[day]['temp']['max']
        low = forecast[day]['temp']['min']
        desc = forecast[day]['weather'][0]['description']
        humidity = forecast[day]['humidity']
        wind = forecast[day]['speed']
        table.add_column("{}".format(date),["{}{}F".format(high,degree),"{}{}F".format(low,degree),"{}".format(desc),"{}%".format(humidity),"{} MPH".format(wind)])

    return table

def main(args):
    weather = get_weather(args.zipcode)
    days = get_days(weather)
    print(build_table(days))

if __name__ == "__main__":
    parser = ArgumentParser(description='Show the 10 day forecast')
    parser.add_argument('-z', '--zipcode', required=True, help='zipcode of the area to retrieve the forecast for')

    main(parser.parse_args())
