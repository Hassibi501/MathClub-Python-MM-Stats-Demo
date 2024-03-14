import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import matplotlib.colors as mcolors

import pandas as pd
import data

while True:
    print("\n")
    print("================================================================")
    print("                        Graph & Data Options")
    print("1. Main Data")
    print("2. Bar Graph (Greatest to Least)")
    print("3. Pie Chart")
    print("4. Exit")
    print("================================================================")
    print("\n")

    MMs = input("How would you like to display your data? ")

    print("\n")

    match MMs:
        case '1':
            df = data.mainData(show_table=True)
            print(df)
            continue
            
        case '2':
            sorted_df = data.sortedTable(showBarGraph=True)
            print(sorted_df )
            continue
        case '3':
            data.pieChart(showPieChart = True)
            print("Pie Chart has been displayed successfully.")
            continue
        case '4':
            break  
        case _:
            print("Error test")
            continue




print("End Of Program.")