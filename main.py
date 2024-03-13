import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import matplotlib.colors as mcolors

import pandas as pd

def mainData():
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


MMs = input("How would you like your M&Ms data to be displayed?")

match MMs:
    case '1':
         print("Test 1")
    case '2':
        print("Test 2")
    case '3':
        print("Test 3")
    case '4':
        print("Test 4")
    case _:
            print("Error test")







#Creating two rows one rwo has "Total" and the other row has the sum of each column except for trial. I then concatnating the two rows into one by adding them.
mainData().loc[len(mainData())] = ["Sub-Total"] + [np.sum(mainData()[col]) for col in mainData().columns if col != "Trial"]


mainData().loc[len(mainData())] = ["Total", mainData().iloc[:, 1:].sum().sum()] + ['' for _ in range(len(mainData().columns) - 2)]


subTotalRow = mainData()[mainData()["Trial"] == "Sub-Total"].iloc[0]

colors = list(mainData().columns[1:])
valueMM = subTotalRow.values[1:]

sortedTable = pd.DataFrame({
    "M&Ms": colors,
    "Total": valueMM
})

sortedTable.sort_values(by = ["Total"], ascending = False,  inplace=True)

plt.bar(
       x = sortedTable["M&Ms"],
       height= sortedTable["Total"]
)




fig, ax = plt.subplots()
ax.set_axis_off()
table = ax.table(
    cellText = mainData().values, 
    colLabels = mainData().columns,
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
table.auto_set_column_width(col=list(range(len(mainData().columns))))

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
        cell.set_facecolor(color_mapping[mainData().columns[j]])
        cell.set_text_props(weight = "bold")
    elif i==15:
        cell.set_facecolor("gray")
        cell.set_text_props(weight = "bold")

    else:
        cell.set_facecolor((*mcolors.to_rgb(color_mapping[mainData().columns[j]]), 0.3))  





print("End Of Program.")