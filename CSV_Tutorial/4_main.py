# this example uses escapechar to ignore any deliminer character appearing after the escape character


import csv

with open('employee_address_3.txt') as csv_file:
	csv_reader = csv.DictReader(csv_file, delimiter=',', escapechar='|')
	line_count = 0
	for row in csv_reader:
		if line_count == 0:
			print(f'Column names are {", ".join(row)}')
			line_count += 1
		print(f'\t{row["name"]} lives at {row["address"]} and joined {row["date joined"]}.')
		line_count += 1
	print(f'Processed {line_count} lines.')