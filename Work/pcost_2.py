def portfolio_cost(filename):
    Total = 0

    f = open(filename, 'rt')
    headers = next(f)
    for line in f:
        row = line.split(',')
        try:
            share = int(row[1])
            price = float(row[2])
            Total += share * price
        except ValueError:
            print("Hiányzó adat", line)
    f.close()
    return Total

cost = portfolio_cost('Data/missing.csv')
print('Total cost', cost)