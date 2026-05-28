stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGLE": 150
}

total = 0

print("Available Stocks:")
print(stocks)

while True:

    stock_name = input("Enter stock name (or 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name in stocks:

        quantity = int(input("Enter quantity: "))

        price = stocks[stock_name]

        investment = price * quantity

        total += investment

        print("Investment added:", investment)

    else:
        print("Stock not found!")

print("Total Investment Value:", total)