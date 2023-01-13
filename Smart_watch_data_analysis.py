#M.MANVANTH
#CS20B1113
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv("dailyActivity_merged.csv")
#printing the data head
print(data.head())

#knowing the no.of entries with shape
print(data.shape)

#To know about the data types of the Columns/attributes
print(data.info())


'''
The column containing the date of the record is an object.
We may need to use dates to calculate the day, let’s convert this column
into a datetime column
'''
#changing the data type of ActivityDate
data["ActivityDate"] = pd.to_datetime(data["ActivityDate"],format="%m/%d/%Y")
print(data.info())

#To check whether any attribute is containing NULL values or not
print(data.isnull().sum())
#No null values so we can continue with the analysis


#Adding up all the Active minutes
data["TotalMinutes"] = data["VeryActiveMinutes"] + data["FairlyActiveMinutes"] + data["LightlyActiveMinutes"] + data["SedentaryMinutes"]
#printing a sample of the column TotalMinutes
print(data["TotalMinutes"].sample(5))

#Descriptive statistics of the dataset
print(data.describe())

#dataset has a “Calories” column
#relationship between calories burned and the total steps walked in a day
figure = px.scatter(
                        data_frame = data,
                        x="Calories",
                        y="TotalSteps",
                        size="VeryActiveMinutes", 
                        trendline="ols", 
                        title="Relationship between Calories & Total Steps"
                    )
figure.show()

#linear relationship between the total number
#of steps and the number of calories burned in a day
#the average total number of active minutes in a day

label = ["Very Active Minutes", "Fairly Active Minutes", 
         "Lightly Active Minutes", "Inactive Minutes"]
counts = data[["VeryActiveMinutes", "FairlyActiveMinutes", 
               "LightlyActiveMinutes", "SedentaryMinutes"]].mean()
colors = ['gold','lightgreen', "pink", "blue"]

fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Total Active Minutes')
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30,marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()

#finding the weekdays of the records by ActivityDate and add a new column to '
#this dataset as “Day”
data["Day"] = data["ActivityDate"].dt.day_name()
print(data["Day"].head())

#very active, fairly active, and lightly active minutes on each day of the week
fig = go.Figure()
fig.add_trace(go.Bar(
                        x=data["Day"],
                        y=data["VeryActiveMinutes"],
                        name='Very Active',
                        marker_color='blue'
                    )
              )
fig.add_trace(go.Bar(
                        x=data["Day"],
                        y=data["FairlyActiveMinutes"],
                        name='Fairly Active',
                        marker_color='green'
                    )
              )
fig.add_trace(go.Bar(
                        x=data["Day"],
                        y=data["LightlyActiveMinutes"],
                        name='Lightly Active',
                        marker_color='pink'
                    )
              )
fig.show()

#the number of inactive minutes on each day of the week
day = data["Day"].value_counts()
label = day.index
counts = data["SedentaryMinutes"]
colors = ['gold','lightgreen', "pink", "blue", "skyblue", "cyan", "orange"]

fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Inactive Minutes Daily')
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=2)))
fig.show()

#the number of calories burned on each day of the week
calories = data["Day"].value_counts()
label = calories.index
counts = data["Calories"]
colors = ['gold','lightgreen', "pink", "blue", "skyblue", "cyan", "orange"]

fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Calories Burned Daily')
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()


#Observations:

#There is a linear relationship between the total number of steps and the number of calories burned in a day.

#81.3% of Total inactive minutes in a day
#15.8% of Lightly active minutes in a day
#On an average, only 21 minutes (1.74%) were very active
#1.11% (13 minutes) of fairly active minutes in a day

#Thursday is the most inactive day according to the lifestyle of all the individuals recorded in the dataset.

#Tuesday is one of the most active days for all individuals given in the dataset, as the highest number of calories were burned on Tuesdays.
