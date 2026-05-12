# combine loops and conditionals to analyze data
prices = [50, 120, 80, 200]

for price in prices:
    if price > 100:
        print(price, "High price")
    else:
        print(price, "Normal price")