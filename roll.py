import csv
import numpy as np
import plotly.express as px

def getDataSource(data_path):
    marks_in_percentage = []
    days_present = []
    with open(data_path) as csv_file :
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader :
            marks_in_percentage.append(float(row["Marks In Percentage"]))
            days_present.append(float(row["Days Present"]))
    return{"x" : marks_in_percentage, "y" : days_present}

def findCorelation(datasource):
    corelation = np.corrcoef(datasource["x"], datasource["y"])
    print("Corelation is " , corelation[0,1])

def plotFigure(data_path):
    with open("roll.csv") as f :
        reader = csv.DictReader(f)
        fig = px.scatter(reader, x="Days Present", y="Marks In Percentage")
        fig.show()

def setup() :
    data_path = "roll.csv"
    datasource = getDataSource(data_path)
    findCorelation(datasource)
    plotFigure(data_path)

setup()