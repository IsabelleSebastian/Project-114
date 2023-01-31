import plotly.express as pe
import pandas
import numpy

a = pandas.read_csv("data.csv")
toeData = a["TOEFL Score"].tolist()
chanceData = a["Chance of Admit "].tolist()

#--------------------------------------scatter graph of data ------------------
m = 1
c = 0
y = []
for x in toeData:
    y_value = m*x + c
    y.append(y_value)

graph = pe.scatter(x=toeData, y=chanceData)
graph.update_layout(shapes=[
    dict(
        type = 'line',
        y0= min(y), y1= max(y),
        x0= min(toeData), x1= max(toeData)
    )
])
graph.show()

#--------------------------------------
toeArray = numpy.array(toeData)
chanceArray = numpy.array(chanceData)

# slope & intercept using Numpy function
m, c = numpy.polyfit(toeArray, chanceArray, 1)
y = []
for x in toeArray:
    y_value = m*x + c
    y.append(y_value)

# plotting the points
graph2 = pe.scatter(x = toeArray, y = chanceArray)
graph2.update_layout(shapes=[
    dict(
        type = 'line',
        y0= min(y), y1= max(y),
        x0= min(toeArray), x1= max(toeArray)
    )
])
graph2.show()

# prediction!
x = 250
y = m*x + c
print(f"Chances of admission if the TOEFL score {x} is {y}")
