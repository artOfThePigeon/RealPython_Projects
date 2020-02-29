from csv import writer
from csv import DictWriter

def append_list_as_row(file_name, list_of_elem):
    with open(file_name, 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(list_of_elem)

def append_dict_as_row(file_name, dict_of_elem, field_names):
    with open(file_name, 'a+', newline = '') as write_obj:
        dict_writer = DictWriter(write_obj, fieldnames=field_names)
        dict_writer.writerow(dict_of_elem)

def man():
     print('*** Append new row to an existing csv file using csv.writer() in python ***')
 
    # List of strings
    row_contents = [32,'Shaun','Java','Tokyo','Morning']
 
    # Append a list as new line to an old csv file
    append_list_as_row('students.csv', row_contents)
 
    print('** Append new row to an existing csv file with less items using csv.writer()  in python **')
 
    # A list with missing entries
    row_contents = [33, 'Sahil', 'Morning']
 
    # Appending a row to csv with missing entries
    append_list_as_row('students.csv', row_contents)
 
    print('Append dictionary as a row to an existing csv file using DictWriter in python')
 
    field_names = ['Id','Name','Course','City','Session']
    row_dict = {'Id': 81,'Name': 'Sachin','Course':'Maths','City':'Mumbai','Session':'Evening'}
 
    # Append a dict as a row in csv file
    append_dict_as_row('students.csv', row_dict, field_names)
 
    print('Append a dictionary with missing entries as a new row to an existing csv file using DictWriter**')
 
    # If empty entries are missed then DictWriter will handle them automatically
    field_names = ['Id','Name','Course','City','Session']
    row_dict = {'Id': 33, 'Name':'Eva', 'Session':'Evening'}
 
    # Append a dict missing entries as a row in csv file
    append_dict_as_row('students.csv', row_dict, field_names)
 
 
if __name__ == '__main__':
    main()
