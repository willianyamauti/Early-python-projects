import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels = len(data[data["Primary Fur Color"] == 'Gray'])
black_squirrels = len(data[data["Primary Fur Color"] == 'Black'])
red_squirrels = len(data[data["Primary Fur Color"] == 'Cinnamon'])

dict_fur_colors = {
    "Fur Color": ["Gray", "Black", "Red"],
    "Count": [grey_squirrels, black_squirrels, red_squirrels]
}

df = pandas.DataFrame(dict_fur_colors)
df.to_csv("squirrel_count.csv")
