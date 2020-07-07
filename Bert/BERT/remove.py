import csv
import pandas as pd
import re

data = pd.read_csv("RawData(2).csv", encoding='utf-8')
res = []

for index, rows in data.iterrows():
    my_list = [rows.Rumor[:-2], rows.Label[:-2], rows.Source[:-2], rows.Date[:-2]]
    if(index<10):
        print(my_list)
#     res.append(my_list)
# df = pd.DataFrame(res,columns=["Rumor","Label","Source","Date"])
# df.to_csv("RawData(2).csv",encoding='utf-8')