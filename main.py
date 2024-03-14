import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import matplotlib.colors as mcolors

import pandas as pd
import data

def sortedTable():
    df = data.mainData()
    subTotalRow = df[df["Trial"] == "Sub-Total"].iloc[0]

    colors = list(df.columns[1:])
    valueMM = subTotalRow.values[1:]

    sorted_df = pd.DataFrame({
    "M&Ms": colors,
    "Total": valueMM
    })

    sorted_df.sort_values(by = ["Total"], ascending = False,  inplace=True)
    return sorted_df




MMs = input("How would you like your M&Ms data to be displayed?")

match MMs:
    case '1':
         df = data.mainData()
         print(df)
         exit()
        
    case '2':
        print(sortedTable())
    case '3':
        print("Test 3")
    case '4':
        print("Test 4")
    case _:
            print("Error test")




plt.bar(
       x = sortedTable["M&Ms"],
       height= sortedTable["Total"]
)









print("End Of Program.")