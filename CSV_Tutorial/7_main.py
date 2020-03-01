# appends data to Hours.csv as a new row.

from csv import DictWriter
 
def append_dict_as_row(file_name, dict_of_elem, field_names):
    try:
        # Open file in append mode
        with open(file_name, 'a+', newline='') as write_obj:
            # Create a writer object from csv module
            dict_writer = DictWriter(write_obj, fieldnames=field_names)
            # Add dictionary as wor in the csv
            dict_writer.writerow(dict_of_elem)
    except IOError:
        print("I/O error")

field_names = ['Org','Task','Time Spent']
row_dict = {'Org': 'St Louis', 'Task': 'Query','Time Spent': 56}
 
 
# Append a dict as a row in csv file
append_dict_as_row('Hours.csv', row_dict, field_names)
        
