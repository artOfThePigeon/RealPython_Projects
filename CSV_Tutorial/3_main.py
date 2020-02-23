# this example uses quotechar to handle a " in the csv.


import csv

with open('employee_address_3.txt') as csv_file:
	csv_reader = csv.DictReader(csv_file, delimiter=',', quotechar='"')
	line_count = 0
	for row in csv_reader:
		if line_count == 0:
			print(f'Column names are {", ".join(row)}')
			line_count += 1
		print(f'\t{row["name"]} lives at {row["address"]} and joined {row["date joined"]}.')
		line_count += 1
	print(f'Processed {line_count} lines.')