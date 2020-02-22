# This uses the openpyxl module to create an excel sheet
# and store the following data into its cells.

from openpyxl import Workbook

workbook = Workbook()
sheet = workbook.active

sheet["A1"] = "Organization"
sheet["B1"] = "Time"
sheet["C1"] = "Task"
sheet["A2"] = "USO"
sheet["B2"] = "20 min"
sheet["C2"] = "Calendar bug"
sheet["A3"] = "ARC"
sheet["B3"] = "45 min"
sheet["C3"] = "Login issue"
sheet["A4"] = "JLTampa"
sheet["B4"] = "10 min"
sheet["C4"] = "Query Tutorial"

workbook.save(filename="timeclock_test.xlsx")
