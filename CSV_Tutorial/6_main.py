# creates Hours.csv with data about what you've done and how long

import csv

fields = ['Org','Task','Time Spent']
dict_data = [
{'Org': 'ARC', 'Task': 'Files', 'Time Spent': 14},
{'Org': 'Tampa', 'Task': 'Call', 'Time Spent': 4},
{'Org': 'USO', 'Task': 'Query', 'Time Spent': 7},
{'Org': 'LLS', 'Task': 'Call', 'Time Spent': 78},
{'Org': 'Tampa', 'Task': 'Call', 'Time Spent': 43},
]
csv_file = "Hours.csv"
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields, lineterminator = '\n')
        writer.writeheader()
        for data in dict_data:
            writer.writerow(data)
except IOError:
    print("I/O error")
