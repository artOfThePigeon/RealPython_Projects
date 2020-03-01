from csv import writer
# This appends a row of dictionary information about how you spent your time working to a csv.
# It will create the csv if it doesnt already exist. 

from csv import DictWriter


def append_dict_as_row(csv_file, hours_data, fields):
    try:
        with open(csv_file, 'a+', newline = '') as csvfile:
            writer = DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            for data in hours_data:
                writer.writerow(data)
    except IOError:
        print("I/O error")

def main():
    print('Appending dictionary entries to csv.')
 
    fields = ['Org','Task','Time Spent']
    hours_data = [
    {'Org': 'ARC', 'Task': 'Files', 'Time Spent': 14},
    {'Org': 'Tampa', 'Task': 'Call', 'Time Spent': 4},
    {'Org': 'USO', 'Task': 'Query', 'Time Spent': 7},
    {'Org': 'LLS', 'Task': 'Call', 'Time Spent': 78},
    {'Org': 'Tampa', 'Task': 'Call', 'Time Spent': 43},
    ]
    # Append a dict as a row in csv file, or create the csv first.
    append_dict_as_row('hours.csv', hours_data, fields)
 
    print('Append a dictionary with missing entries as a new row to an existing csv file using DictWriter**')
 
    # If empty entries are missed then DictWriter will handle them automatically
    fields = ['Org','Task','Time Spent']
    hours_data = [{'Task':'MC Update','Time Spent': 30}]
 
    # Append a dict missing entries as a row in csv file
    append_dict_as_row('hours.csv', hours_data, fields)
 
 
if __name__ == '__main__':
    main()
