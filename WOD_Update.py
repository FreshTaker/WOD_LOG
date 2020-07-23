#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Script: WOD_Update.py

This script adds a log entry to the WOD_LOG.

Each row is a workout logged:
[date, name, type, total rounds, total time, total reps, [workout movements, reps]]
* Function will need to search and add columns to DF if not present already.


"""
import datetime
import pandas

def get_CSV(FILENAME):
    """ Retrieves CSV file containing workout log information. """
    LOGFILE = pandas.read_csv(FILENAME)
    return LOGFILE

def add_workout(type):
    print("")

print("WOD_Update.py started.")
USER_N = input("Enter USER NUMBER: ")
filename = 'WOD_LOG_' + str(USER_N) + '.csv'

try:
    userlog = get_CSV(filename)
except Exception as e:
    print(type(e))
    print(e.args)
    print(e)


print(userlog)



