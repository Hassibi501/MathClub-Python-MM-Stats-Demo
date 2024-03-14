import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import matplotlib.colors as mcolors

import pandas as pd

def mainData(show_table=False):
    data = {
    "Trial": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 
    "Red": [1, 2, 3, 3, 3, 2, 2, 5, 3, 2, 1, 4, 2],
    "Orange": [1,1,2,4,1,4,3,1,3,1,0,3,3],
    "Yellow": [1, 5, 3, 4, 3, 2, 4, 2, 4, 4, 6, 3, 1],
    "Green": [2, 3, 5, 1, 2, 1, 4, 0, 1, 2, 3, 2, 4],
    "Blue": [2, 2, 2, 4, 4, 2, 4, 3, 3, 2, 2, 4, 0],
    "Brown": [5, 2, 0, 1, 0, 2, 0, 1, 2, 3, 2, 1, 4]
    }
    df = pd.DataFrame(data)

    #Creating two rows one rwo has "Total" and the other row has the sum of each column except for trial. I then concatnating the two rows into one by adding them.
    df.loc[len(df)] = ["Sub-Total"] + [np.sum(df[col]) for col in df.columns if col != "Trial"]


    df.loc[len(df)] = ["Total", df.iloc[:, 1:].sum().sum()] + ['' for _ in range(len(df.columns) - 2)]

    if show_table:
        fig, ax = plt.subplots()
        ax.set_axis_off()
        table = ax.table(
            cellText = df.values, 
            colLabels = df.columns,
            loc = "center",
            cellLoc = "center",
        )

        for key, cell in table.get_celld().items():
            row, col = key
            if col == 0:
                cell.set(width = 0.05)
            else:
                cell.set(width = 0.1)

        table.auto_set_font_size(False)
        table.set_fontsize(10)
        table.auto_set_column_width(col=list(range(len(df.columns))))

        color_mapping = {
            "Trial": "lightgray",
            "Red": "red",
            "Orange": "orange",
            "Yellow": "yellow",
            "Green": "green",
            "Blue": "blue",
            "Brown": "brown",
        }

        for (i, j), cell in table.get_celld().items():
            if i == 0 or i == 14:
                cell.set_facecolor(color_mapping[df.columns[j]])
                cell.set_text_props(weight = "bold")
            elif i==15:
                cell.set_facecolor("gray")
                cell.set_text_props(weight = "bold")

            else:
                cell.set_facecolor((*mcolors.to_rgb(color_mapping[df.columns[j]]), 0.3))  

        plt.show()
    return df


def sortedTable(showBarGraph = False):
    df = mainData()
    subTotalRow = df[df["Trial"] == "Sub-Total"].iloc[0]

    colors = list(df.columns[1:])
    valueMM = subTotalRow.values[1:]

    sorted_df = pd.DataFrame({
    "M&Ms": colors,
    "Total": valueMM
    })
  
    sorted_df.sort_values(by = ["Total"], ascending = False,  inplace=True)
    if showBarGraph:

        color_mapping = {
            'Red': 'red',
            'Orange': 'darkorange',  
            'Yellow': 'yellow',
            'Green': 'green',
            'Blue': 'blue',
            'Brown': 'saddlebrown'  
        }
        plt.bar(
        x = sorted_df["M&Ms"],
        height= sorted_df["Total"],
        color=[color_mapping[color] for color in sorted_df["M&Ms"]]
        )
        plt.title("M&Ms Bar Graph")
        plt.xlabel("M&Ms")
        plt.ylabel("Total Amount of M&Ms")
        plt.show()

    return sorted_df

def pieChart (showPieChart = False):
    if showPieChart:
        sorted_df = sortedTable()

        labels = sorted_df["M&Ms"].tolist()
        sizes = sorted_df["Total"].tolist()

        fig1, ax1 = plt.subplots()
        ax1.pie(
            sizes,
            labels = labels,
            colors = labels,
            autopct = '%1.1f%%',
            startangle = 90
        )

        plt.title("M&Ms Pie Chart")
        ax1.axis("equal")

    
    return plt.show()