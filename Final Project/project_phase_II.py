"""
A program that answers one of the questions.

Currently WIP, we have to reach the following goals:

1. GitHub Repo contains python code:
There is a Python code that is related to solving at least one question that is used to answer that question.
(Instructions on how to use it with the data should be clear)

2. Progress Report in the README.md:
The file contains all the required information from sub-task 6. Descriptions are clearly understood.
The solution is complete, and it gives the full answer to the question with all the necessary figures and results.
Explanations are well thought out. The instructions on how to use the Python code are clearly explained.
"""
import sys
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

def parse_data(file_path):

    # opens and reads the csv file,
    # turns it into a pandas DataFrame,
    # and uses exception handling as a safeguard
    try:
        dataframe = pd.read_csv(file_path)
    except FileNotFoundError:
        print('File ', file_path, ' not found. Exiting program.')
        sys.exit(-1)

    return dataframe

if __name__ == "__main__":
    '''
    Executes the program
    '''
    # for ui purposes
    line = "-" * 114

    # reads the data, returns it as a dataframe after calling "parse_data()"
    EVPD_DataFrame = parse_data("Final Project/data/electric_vehicle_population_data.csv")
    # and then prints it
    print(line)
    print("Electric Vehicle Population Data dataset in the DataFrame form:")
    print(EVPD_DataFrame)

    # code below is to test some python code to learn how to access specific data from this .CSV file
    print(line)
    print(EVPD_DataFrame.iloc[0])
    print(line)
    print(EVPD_DataFrame.loc[0, "Make"])
    print(EVPD_DataFrame.loc[0, "Model"])

    # bottom line for ui purposes
    print(line)
