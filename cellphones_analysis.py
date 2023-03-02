# import the necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# read and get a general description of the data
cellphones = pd.read_csv("/home/user/Downloads/ships/cellphones.csv")
print(cellphones.head())
print(cellphones.info())

# Qn1: Order the brands according to the number of users
brand_reach = cellphones.groupby("brand")["user_id"].count().sort_values(ascending=False).reset_index(name="count")
print(brand_reach)

# plot 
sns.set()
sns.barplot(data=brand_reach, x="count", y="brand")
plt.title("Phones and The Distribution of Users")

# Qn2: The distribution of each brand across genders
gender = cellphones.groupby("gender")["gender"].count()
print("The gender distribution is made up of:", gender)
gender_reach = cellphones.groupby("brand")["gender"].value_counts().reset_index(name="count")
print(gender_reach)

# scatter plot
sns.set(font_scale=2)
sns.color_palette("flare", as_cmap=True)
fig, ax = plt.subplots(figsize=(25, 15), nrows=1, ncols=1)
sns.scatterplot(data=gender_reach, x="count", y="gender", hue="brand", size="brand", sizes=(5, 220), legend="full")