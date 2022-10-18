# A fastapi 'Mr Wolf' where the user inputs a city to get the current time there
# TODO: update mrwolf.db with more timezones

from fastapi import FastAPI
import requests
import sqlite3

app = FastAPI(docs_url="/")

@app.get("/what-is-the-time-mr-wolf")
def city_time(city):
    #TODO: remove the below
    '''try:
        tz = cities[city]
    except KeyError:
        return (f"choose from {cities.keys()}")'''
    # connect to mrwolf.db to search for requested city, and return it's timezone
    # cursor allows you to execute SQL from within python
    with sqlite3.connect('mrwolf.db') as conn:
        cursor = conn.cursor()
        cursor.execute(f"""
        SELECT timezone FROM city
        WHERE name = '{city}'
        """)
        result = cursor.fetchone()
        # if city does not exist in mrwolf.db, returns the below error message
        # if it does exist, print the result not as a tuple
        if not result:
            return f"Unsupported city {city}"
        else:
            tz = result[0]
        print(tz)
        #inputs the required timezone into the url and returns the time (and other data)
        response = requests.get(f"https://worldtimeapi.org/api/timezone/{tz}")
        data = response.json()
        return data
