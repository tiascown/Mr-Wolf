# A fastapi (website) called Mr Wolf where the user inputs a city and country to get the current time there
# TODO easier to have drop down options for country and city?
# TODO What's the weather Mr Wolf?

from fastapi import FastAPI
import requests

#create user interface

#ask for user to input a country
#time_zone = city
#ask for user to input a city
city = input("Enter a city to find out it's current time: ")
#using input, get time from web
response_json = requests.get(f"http://worldtimeapi.org/api/Europe/{city}.txt")
time = response_json
#display time to user
print(f"The current time in {city} is {time}")