# Name: Dylan Moore/ Max Smith
# email: moore4dl@mail.uc.edu
# Assignment Title: Assignment 10
# Course: IS 4010
# Semester/Year: Fall 2023
# Brief Description: use an API and connect to it via the web 
# Functions

import json
import requests #web requests
#We did not need a key for this data
response = requests.get('https://swapi.dev/api/people/1/')
json_string = response.content
    
parsed_json = json.loads(json_string) # Now we have a python dictionary
#loads the data
