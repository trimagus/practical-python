# pcost.py
#
# Exercise 1.27

TotalSum = 0
f = open('Data/portfolio.csv', 'rt')
headers = next(f).split(',')
for line in f:
	row = line.split(',')
	db = int(row[1])
	cost = float(row[2])
	TotalSum = TotalSum + db * cost

print(round(TotalSum, 2))
f.close()