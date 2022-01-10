## Inspiration
Finding weather description can be handy especially when you plan to travel, or even sometimes when you are lazy enough to look out. 

## What it does
**WEATHERSCRIPTER** fetches weather description for given city 

## How we built it
This uses python as programming language, and utilizes OpenWeatherMap api and ipinfo.io api to fetch city and its weather condition 

## How to use it 
* Install required packages from requirements.txt 
* Create account and get api from [openweathermap](https://home.openweathermap.org)
* Add WEATHER_API_KEY with api key in .env file and give python call as 
```python 
python weather.py
```
 or 
```python
 python weather.py {city_name}
 ``` 
 without curly brackets 

## Challenges we ran into
If for some reason user doesn't provide city name then we can we do that for user 

## Accomplishments that we're proud of
Solving above challenge is plus, since it fetches city for user based on ip address 

## What we learned
We have learnt to use API, request and response thing to get weather description and reading that from json format

## What's next for WEATHERCRIPTER
**WEATHERSCRIPTER** can include machine learning model to predict future weather condition
