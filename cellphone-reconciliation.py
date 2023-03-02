import pandas as pd
 
users = pd.read_csv("/home/user/Downloads/cell phones/cellphones users.csv")
ratings = pd.read_csv("/home/user/Downloads/cell phones/cellphones ratings.csv")
data = pd.read_csv("/home/user/Downloads/cell phones/cellphones data.csv")

join = pd.merge(users, ratings, on="user_id")
print(join.head())
three_way = pd.merge(join, data, on="cellphone_id").drop_duplicates()
print(three_way.head())
three_way.to_csv("cellphones", index=False)