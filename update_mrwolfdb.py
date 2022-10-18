# update_mrwolfdb.py
import os
import sqlite3
import csv
import sys
from turtle import rt
import requests

db_filename = 'mrwolf.db'
schema_filename = 'mrwolf_schema.sql'

db_is_new = not os.path.exists(db_filename)

def insert_timezones():
    #get the timezones from worldapi
    response = requests.get("https://worldtimeapi.org/api/timezone")
    #convert response to json
    timezones = response.json()
    #for each timezone insert into timezone table
    with sqlite3.connect(db_filename) as conn:
        for tz in timezones:
            conn.executescript(f"""
            INSERT INTO timezone(name)
            VALUES ('{tz}')
            """)

# adding cities to mrwolf.db with a shared timezone
def import_cities(filename, timezone):
    with sqlite3.connect(db_filename) as conn:
        with open(filename, 'rt') as f:
                    reader = csv.reader(f)
                    for row in reader:
                        print(".", end="")
                        conn.executescript(f"""
                        insert into city (name, timezone)
                        values ("{row[0]}", '{timezone}');
                        """)

# creates a database using associated schema (if database doesn't exist yet)
def create_db():
    with sqlite3.connect(db_filename) as conn:
        if db_is_new:
            print('Creating schema')
            with open(schema_filename, 'rt') as f:
                schema = f.read()
            conn.executescript(schema)

            print('Inserting initial data')
            #TODO remove the below
            '''with open('canada.csv', 'rt') as f:
                reader = csv.reader(f)
                for row in reader:
                    print(".", end="")
                    conn.executescript(f"""
                    insert into city (name, timezone)
                    values ("{row[0]}", 'America/Anchorage');
                    """)'''
        else:
            print('Database exists, assume schema does, too.')

# runs the required function, comment/uncomment when needed
if __name__ == "__main__":
    #create_db()
    #insert_timezones()
    import_cities('denmark.csv', 'Europe/Copenhagen')