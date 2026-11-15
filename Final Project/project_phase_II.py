"""
A program that answers one of the questions:

Question 1: Which model and make of EV is the most popular?
Answer for Question 1: EVs manufactured by Tesla.
Justification/Proof of Concept for Question 1: The dataset contains the make and model of each EV,
such as a Tesla Model Y for example. By counting how many times a make and model of an EV appears
and comparing it to other EVs, we can see which one is the most popular.
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

def most_popular_vehicles (dataframe, n = 10):
    """
    A function that finds the most popular EVs in the dataset.
    "n" is how many spots are in the list, so "n = 10" would
    create the top 10 most popular electric vehicles list. "n"
    has a default value set to 10, but it can be overridden. 
    """

    # creates a new dataframe that consists of the top n vehicles
    # based on how many exist in the original dataframe
    most_popular_electric_vehicles = (
        dataframe[["Make", "Model"]]
        .value_counts()
        .nlargest(n)
        .reset_index()
    )

    # adds "Rank" as a regular column at position 0
    most_popular_electric_vehicles.insert(0, "Rank", range(1, len(most_popular_electric_vehicles) + 1))

    # for ui purposes
    line = "-" * 114
    print(line)
    # prints the top n most popular cars list while hiding the index
    print(f"Top {n} most popular electric vehicles:")
    print(most_popular_electric_vehicles.to_string(index = False))

    return most_popular_electric_vehicles

def plot_ev_bar_graph (dataframe):

    # counts how many vehicles are present in the dataframe
    n = len(dataframe)

    # creates lists to define data
    vehicles = []
    num_of_vehicles = []

    # creates variables for the for loop
    vehicle = None
    num_of_vehicle = None

    # iterates through the dataframe to add the list of vehicles into the
    # vehicles list, and the number of said vehicle in the num_of_vehicles list
    for i, row in dataframe.iterrows():
        vehicle = f"{row["Make"]} {row["Model"]}"
        num_of_vehicle = row["count"]
        vehicles.append(vehicle)
        num_of_vehicles.append(num_of_vehicle)

    # creates a new canvas (figure) in Matplotlib
    # and sets its dimensions to 8 inches wide and 5 inches tall
    plt.figure(figsize=(9, 6))

    # creates the bar graph
    plt.barh(vehicles, num_of_vehicles)

    # adds the title and axis labels
    plt.title(f"Top {n} most popular electric vehicles:")
    plt.xlabel("Number of Electric Vehicles")
    plt.ylabel("Electric Vehicle Model")

    # flips the y-axis so the most popular vehicle is at the top
    plt.gca().invert_yaxis()

    # automatically adjusts subplot parameters so that plots fit cleanly
    # within the figure area without overlapping, makes the plot look nicer
    plt.tight_layout()

    # display the graph
    plt.show()

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

    # creates a variable to store a new dataframe that shows
    # the top n (default = 10) most popular electric vehicles
    most_popular_evs = most_popular_vehicles(EVPD_DataFrame)

    # plots the top n most popular evs dataframe 
    plot_ev_bar_graph(most_popular_evs)

    # for ui purposes
    print(line)
