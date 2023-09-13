import pandas as pd
import json
csvfile = pd.read_csv('dummy.csv')

data = {}
for key in list(csvfile.columns):
    data[key] = list(csvfile[key])
#print(data)

with open('data.json', 'a') as f:
    f.write(json.dumps(data, ensure_ascii=False, indent=4))