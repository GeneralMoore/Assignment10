# Name: Dylan Moore/ Max Smith
# email: moore4dl@mail.uc.edu
# Assignment Title: Assignment 10
# Course: IS 4010
# Semester/Year: Fall 2023
# Brief Description: use an API and connect to it via the web 
# Main

import json
import requests #web requests
from FunctionsPackage.Functions import *

if __name__ == "__main__": 
    print("These are the ships Luke Skywalker used: ")
    for ships in parsed_json['starships']:
        print (ships) #prints the ships has a hickup of how the data comes in but it works 
        