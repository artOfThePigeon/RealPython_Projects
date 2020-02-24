import csv

with open('employee_file_dict.csv', mode='w') as employee_file:
	fieldnames = ['name', 'dept', 'birth_month']
	employee_writer = csv.DictWriter(employee_file, fieldnames=fieldnames, lineterminator = '\n')
	
	employee_writer.writeheader()
	employee_writer.writerow({'name': 'Adam Smith', 'dept': 'Accounting', 'birth_month': 'August'})
	employee_writer.writerow({'name': 'Jane Fonda', 'dept': 'Firefighting', 'birth_month': 'March'})
