import asyncio
import os
from statistics import mean

from dotenv import load_dotenv

import requests

load_dotenv()


async def get_weather_1():
    print('Getting weather from weatherapi.com')
    r = requests.get(f'https://api.weatherapi.com/v1/forecast.json?key={os.getenv("WEATHER_1")}&q=London&days=1&aqi=no&alerts=no')
    data = r.json()
    forecastday = data['forecast']['forecastday'][0]
    avg_temp_c = forecastday['day']['avgtemp_c']
    return avg_temp_c


async def get_weather_2():
    print('Getting weather from weather.visualcrossing.com')
    r = requests.get(f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/london?unitGroup=metric&key={os.getenv("WEATHER_2")}&contentType=json')
    data = r.json()
    return data['days'][0]['temp']


async def get_weather_3():
    print('Getting weather from tomorrow.io')
    r = requests.get(f'https://api.tomorrow.io/v4/weather/forecast?location=london&apikey={os.getenv("WEATHER_3")}')
    data = r.json()
    temperature_avg = data['timelines']['daily'][1]['values']['temperatureAvg']
    return temperature_avg


async def get_avg_value():
    tasks = [
        get_weather_1(),
        get_weather_2(),
        get_weather_3(),
    ]
    results = await asyncio.gather(*tasks)
    return mean(results)


async def main():
    avg = await get_avg_value()
    print(f"Average weather in London for today is: {round(avg, 2)} °С")


if __name__ == '__main__':
    asyncio.run(main())
