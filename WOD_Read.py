#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Script: WOD_Read.py

This script interprets the WOD_LOG database.

Track performance over time of workouts.

Goal would be to predict time or reps likely to be accomplished to a new workout.

"""
import pandas

def get_CSV(FILENAME):
    """ Retrieves CSV file containing workout log information. """
    LOGFILE = pandas.read_csv(FILENAME, header=0, index_col=0)
    return LOGFILE

def read_log(LOGFILE):
    print(LOGFILE)


"""MAIN"""
print("WOD_Read.py started.")
USER_N = input("Enter USER NUMBER: ")
filename = 'WOD_LOG_' + str(USER_N) + '.csv'
try:
    userlog = get_CSV(filename)
except Exception as e:
    print(type(e))
    print(e.args)
    print(e)

read_log(userlog)
