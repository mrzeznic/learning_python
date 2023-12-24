# Gordon Dividend Model
#
# Given a set of inputs, this function will calculate the price of a stock using the Gordon Dividend Model
#
# Inputs:
#   - dividend_per_share: The dividend per share of the stock (float)
#   - growth_rate: The growth rate of the stock's dividends (float)
#   - required_return: The required return of the stock (float)
#   - current_price: The current price of the stock (float)
#
# Output:
#   - price: The price of the stock based on the Gordon Dividend Model (float)

def gordon_dividend_model(dividend_per_share, growth_rate, required_return, current_price):
    price = (dividend_per_share * (1 + growth_rate)) / (required_return - growth_rate)
    return price


# Sample usage
'''
dividend_per_share = 0.5
growth_rate = 0.1
required_return = 0.15
current_price = 10
'''
dividend_per_share = 0.06 # 0.6% annually, or 0.006 as a decimal
growth_rate = 0.0779
required_return = 0.10
current_price = 154.5

price = gordon_dividend_model(dividend_per_share, growth_rate, required_return, current_price)
#print(price) # Output: 12.5

#def gordon_dividend_model(dividend_per_share, growth_rate, required_return):
#    fair_price = (dividend_per_share / (required_return - growth_rate))
#    return fair_price



fair_price = gordon_dividend_model(dividend_per_share, growth_rate, required_return, current_price)

if current_price < fair_price:
    print("The stock is undervalued, current price:", current_price, "fair price:", fair_price)
elif current_price > fair_price:
    print("The stock is overvalued, current price:", current_price, "fair price:", fair_price)
else:
    print("The stock is correctly valued, current price:", current_price, "fair price:", fair_price)

print("Fair price:" + str(fair_price))
print("Price:" + str(price))
