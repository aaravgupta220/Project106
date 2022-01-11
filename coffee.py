import csv
import numpy as np
import plotly.express as px

def getDataSource(data_path):
    coffee_in_ml = []
    sleep_in_hours = []
    with open(data_path) as csv_file :
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader :
            coffee_in_ml.append(float(row["Coffee in ml"]))
            sleep_in_hours.append(float(row["sleep in hours"]))
    return{"x" : coffee_in_ml, "y" : sleep_in_hours}

def findCorelation(datasource):
    corelation = np.corrcoef(datasource["x"], datasource["y"])
    print("Corelation is " , corelation[0,1])

def plotFigure(data_path):
    with open("coffee.csv") as f :
        reader = csv.DictReader(f)
        fig = px.scatter(reader, x="Days Present", y="Marks In Percentage")
        fig.show()

def setup() :
    data_path = "coffee.csv"
    datasource = getDataSource(data_path)
    findCorelation(datasource)
    plotFigure(data_path)

setup()