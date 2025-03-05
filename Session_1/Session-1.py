# Python Basics
#This section covers the fundamentals of python like variables, data types, control, list, dictionaries etc.

stock_price = 150.75
shares = 10
stock_name ="AAPL"
is_profitable = True

print(stock_price)
print(shares)
print(stock_name)
print(is_profitable)

stock_prices = [ 150.75, 152.30, 148, 151.00, 153, "closed", "closed"]
print(stock_prices)
print(type(stock_prices))
print(f"Length: {len(stock_prices)}")
print(stock_prices[0])

stock_info = { "stockName": "AAPL", "price": 150.75, "shares": 10}
print("stock_info.keys()", stock_info.keys())
print("stock_info.values()", stock_info.values())
print("stock_info.items()",  stock_info.items())
print("stock_info.get('price')", stock_info.get("price"))
print("stock_info.get('coutry', 'N/A')",   stock_info.get("coutry", "N/A"))

print(stock_info["stockName"])

#functions
def calculate_total_value(price, numofShares):
    return price * numofShares


total_value = calculate_total_value(stock_price, shares)
print(f"${total_value}")

total_value = calculate_total_value(1000, 10)
print(f"${total_value}")

print(f"total value: {total_value}")
if total_value > 3000 and total_value < 5999:
    print("this is somewhat profitable")
elif total_value > 5000:
    print("this is very profitable")
else:
    print("Not profitable")



#Loops

for price in stock_prices:
   
    if isinstance(price, str):
        print(f"{price}")
    else:
        print(f"${price}")    