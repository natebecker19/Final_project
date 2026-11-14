"""
A program that answers one of the questions.
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

    print(line)
    print(EVPD_DataFrame.iloc[0])
    print(line)
    print(EVPD_DataFrame.loc[0, "Make"])
    print(EVPD_DataFrame.loc[0, "Model"])

    print(line)