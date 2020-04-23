fromm collections import defaultdict

incomes = [('Books', 1250.00),
           ('Books', 1300.00),
           ('Books', 1420.00),
           ('Tutorials', 560.00),
           ('Tutorials', 630.00),
           ('Tutorials', 750.00),
           ('Courses', 2500.00),
           ('Courses', 2430.00),
           ('Courses', 2750.00),]

dd = defaultdict(float)
for product, income in incomes:
    dd[product] += income

for product, income in dd.items():
    print(f'Total income for {product}: ${income:,.2f}')
