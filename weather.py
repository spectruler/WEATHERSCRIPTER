import os 
import sys 
import json
import requests 
from dotenv import load_dotenv

def get_city(debug=False):
    url = 'https://ipinfo.io/json'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        ip = data['ip']
        org = data['org']
        city  = data['city']
        country = data['country']
        region = data['region']
        if debug:
            print(f'IP: {ip}\n Org: {org}\nCity: {city}\nCountry: {country}\nRegion: {region}')
        return city,region,country
    else:
        raise Exception('Couldn\'t find city please enter manually')

def get_weather(key,city,region=None,country=None,debug=False):
    BASE_URL =  'https://api.openweathermap.org/data/2.5/weather?q='
    url = f'{BASE_URL}{city}{","+region if region else ""}{","+country if country else ""}&appid={key}'
    if debug:
        print(url) 
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        temp = main['temp']
        humidty  = main['humidity']
        pressure = main['pressure']
        report = data['weather']
        description = report[0]['description']
        if debug:
            print(" Temperature (in kelvin unit) = " +
                    str(temp) +
          "\n atmospheric pressure (in hPa unit) = " +
                    str(pressure) +
          "\n humidity (in percentage) = " +
                    str(humidty) +
          "\n description = " +
                    str(description))
        return (temp,humidty,pressure,description)
    else:
        raise Exception("Error can't find weather")


if __name__ == "__main__":
    if len(sys.argv)>1:
        city = sys.argv[1]
    else:
        city, region, country = get_city(debug=False)
    load_dotenv(".env")
    key = os.getenv('WEATHER_API_KEY')
    # print(key)
    temp,humidty,pressure,weather = get_weather(key,city,debug=False)
    print(" Temperature (in kelvin unit) = " + str(temp) +
          "\n Atmospheric pressure (in hPa unit) = " +
                    str(pressure) +
          "\n Humidity (in percentage) = " +
                    str(humidty) +
          "\n Weather description = " +
                    str(weather))


# API_KEY = '900be3276a7666827ecb67e5bb870459'
