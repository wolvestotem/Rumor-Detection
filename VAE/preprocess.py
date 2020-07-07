import csv
import pandas as pd
import re

data = pd.read_csv("Rumor Data V2.csv", encoding='utf-8')
res = []

for index, rows in data.iterrows():
    my_list = [rows.Rumor, rows.Lable, rows.sentiment]
    m = re.search("[a-z A-Z]*$",my_list[2])
    wrow = []
    wrow.append(m.group(0))
    res.append(wrow)
# print(res)
df = pd.DataFrame(res,columns=["label"])
# print(df)
df.to_csv("tsne_senti2.csv",encoding="utf-8")

