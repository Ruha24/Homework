import csv
import json

a = []

with open('fail.csv',encoding='utf-8') as f:
    reader = csv.reader(f)
    for i in reader:
        a.append(i)

with open('files1.json', 'w') as F:
    json.dump(a, F, sort_keys=True, indent=1)


with open('files1.json') as Fi:
    print(Fi.read())