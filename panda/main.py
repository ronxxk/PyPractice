# import csv

# with open("weather_data.csv") as data:
#     data = csv.reader(data)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             print(row[1])


import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20260612.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data ["Primary Fur Color"] == "Black"])

print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)



data_dict = {
"Fur Color": ["Gray", "Cinnamon", "Black"],
"Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}


df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")