#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Script: WOD_Create.py
Create a database as a CSV to store workouts.  This is run for a new user only.
"""
import datetime
import csv


def CreateCSV(USER_N, DATE):
    filename = 'WOD_LOG_'+str(USER_N)+'.csv'
    with open(filename, 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=' ')
        filewriter.writerow(['USER_N', str(USER_N)])
        filewriter.writerow(['Date Created', str(DATE)])
    print("Created Log file for " + str(USER_N))


print("WOD_Create.py started.")
USER_N = input("Enter USER NUMBER: ")

if USER_N != "":
    DATE = datetime.datetime.today()
    DATE = DATE.date()
    print(DATE)
    CreateCSV(USER_N, DATE)
else:
    print("USER NUMBER not valid.  Please run script again.")


