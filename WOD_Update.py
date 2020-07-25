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
    LOGFILE = pandas.read_csv(FILENAME, header=0, index_col=0)
    return LOGFILE

def add_workout(WOD_LOG):
    """1st level, select workout"""
    print("Recording Workout")
    workout_type = input("Select Workout Type #: 1) AMRAP, 2) AFAP, 3) MAX WEIGHT: ")
    if workout_type == "":
        print("No workout selected")
        end_program()
    elif workout_type == "1":
        print("AMRAP was selected")
        WOD_LOG = add_AMRAP(WOD_LOG)
    elif workout_type == "2":
        print("AFAP was selected")
        WOD_LOG = add_AFAP(WOD_LOG)
    elif workout_type == "3":
        print("MAX WEIGHT was selected")
        WOD_LOG = add_MAX_WEIGHT(WOD_LOG)
    else:
       print("Invalid workout selected")
       end_program()
    return WOD_LOG

def add_AMRAP(WOD_LOG):
    """2nd level, add AMRAP items
    AMRAP = As Many Rounds/Reps As Possible
    Score = Rounds/Reps completed
    """

def add_AFAP(WOD_LOG):
    """2nd level, add AFAP items
    AFAP = As Fast as Possible
    Score = time
    """

def add_MAX_WEIGHT(WOD_LOG):
    """2nd level, add MAX WEIGHT items
    Score = weight & reps
    """
    # Future: read log and display already logged options
    print("Moves Available: ")
    moves = ['Back Squat', 'Front Squat', 'Deadlift', 'Sumo Deadlift', 'Power Clean', 'Hang Clean',
             'Bench Press']
    imoves = range(0,len(moves))
    for m,n in zip(moves,imoves):
        print(n,m)
    move_selected = input('Select move # from list: ')
    reps_done = input('Enter # of Reps of final set: ')
    weight = input('Enter # of pounds of final set: ')
    notes = input('Enter any notes, rep scheme, etc: ')
    # assuming inputs are valid
    date = todays_date()

    df1 = pandas.DataFrame({"Date": [str(date)],
                            "Workout Type": ["Max Weight"],
                            "Move": [moves[int(move_selected)]],
                            "Reps": [int(reps_done)],
                            "Weight": [float(weight)],
                            "Notes": [str(notes)]
                            })
    print("New Workout Record:")
    print(df1)
    WOD_LOG = pandas.concat([WOD_LOG, df1])
    WOD_LOG.reset_index(drop=True, inplace=True)
    return WOD_LOG

def end_program():
    """Ending the program"""
    print("Ending program.  Good bye")

def save_CSV(WOD_LOG, filename):
    """Save to the CSV"""
    WOD_LOG.to_csv(filename)
    print("Saved to CSV")

def todays_date():
    """Returns today's date"""
    date = datetime.datetime.today()
    date = date.date()
    return date


"""MAIN"""
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
userlog = add_workout(userlog)
save_CSV(userlog,filename)
print(userlog)


