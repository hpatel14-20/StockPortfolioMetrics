# # Raw Package
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
# pd.set_option('display.max_rows', None) #display all columns when using pandas dataframe... can set to rows too
import pandas_datareader as pdr
import datetime as dt

#input tickers you'd like beta values for from yahoo. Choose a time frame as well.
tickers = ['AAPL', 'MSFT', 'META', 'TSLA','BYND', '^NDX']
start = dt.datetime(2019, 9, 22)
end = dt.datetime(2022, 9, 22)
data = pdr.get_data_yahoo(tickers, start, end, interval="d")
data = data['Adj Close']
data

# Convert historical stock prices to daily percent change
price_change = data.pct_change()
print(price_change)

#Drops NaN values from data. This could change the time period depending on ticker choice since some stocks may not have been trading during that time frame
df = price_change.dropna()
df #keep in mind a stock thats more recent will drop certain time periods in start/end above


#Loop through all tickers and print Beta value
for column in df:
    x = np.array(df[column]).reshape((-1,1))
    y = np.array(df['^NDX'])
    model = LinearRegression().fit(x, y)

# Prints the beta to the screen with the ticker
    print(column, 'Beta: ', model.coef_)

#Notes on beta of a stock:
    #benchmark above is Nasdaq which represents the "overall market" I am measuring against. Another good one to use is '^SPX'
    #Beta indicates how volatile a stock's price is in comparison to the overall stock market. 
        #A beta greater than 1 indicates a stock's price swings more wildly (i.e., more volatile) than the overall market. A beta of less than 1 indicates that a stock's price is less volatile than the overall market.
    #You can define the benchmark or overall market as anything you deem safe. Typicall index funds are great to use as it represents overall market movements



#------------------------------------------------------------------------------------------------#


#Calculate overall portfolio beta value 
#Will need to input beta values from linear regression model above so use the same time period
#Simulate a portfolio you have currently or one you'd like to simulate below

#Adjust your portfolio tickers here
portfolio_tickers = ['TSLA', 'BYND']
portfolio = {'Ticker':  ['TSLA', 'BYND'], 'Number Of Shares': [10, 20]} #make sure #shares matches order of stock tickers column
portfolio = pd.DataFrame(portfolio)
print(portfolio)

#Choose time frame you want to look at. We will use beta values from the previous example so keep the time frame similar to the portfolio time frame you're looking at here
start = dt.datetime(2022, 9, 22)
end = dt.datetime(2022, 9, 22)



#Data cleansing
yahoo_data = pdr.get_data_yahoo(portfolio_tickers, start, end, interval="d")
share_price = yahoo_data['Adj Close']
share_price = share_price.reset_index()
share_price = share_price.drop(['Date'], axis=1)
share_price = share_price.T
share_price = share_price.rename({0 : 'Share Price'}, axis=1)
share_price['Ticker'] = portfolio_tickers 
portfolio = pd.merge(share_price, portfolio, how='inner', on='Ticker')
portfolio

#Calculations
portfolio["total value"] = portfolio['Number Of Shares'] * portfolio['Share Price']
portfolio['Portfolio Share'] = portfolio['total value'] / portfolio['total value'].sum()
portfolio

#manually insert beta values from previous coefficeints above + Weighted Beta Calc
    #Note: the order should match the order of tickers you have chosen so that beta value aligns with the correct ticker
d = pd.Series([0.2492687,0.12483716], index=[0,1])
portfolio['Beta'] = d.values
portfolio["Weighted Beta"] = portfolio['Portfolio Share'] * portfolio['Beta']
portfolio


#Print portfolio Beta value
print('Portfolio Beta:', portfolio['Weighted Beta'].sum())



#Extra Notes:


# High Beta
# A high beta stock — one that tends to rise and fall along with the market often — has a value of greater than 1. So if a stock has a beta of 1.2 and is benchmarked to the S&P 500, it is 20% more volatile than the broader measure.
# If the S&P 500 rises or falls 10%, then the stock would conversely rise or fall 12%. The same would be true for portfolio beta. While there’s more downside risk with high-beta stocks, they can also generate bigger returns when the market rallies – a principle of Modern Portfolio Theory.
# Low Beta
# A low beta stock with a Beta of 0.5 would be half as volatile as the market. So if the S&P 500 moved 1%, the stock would post a 0.5% swing. Such a stock may have less volatility, but it also may have less potential to post large gains as well.
# Still, investors often prefer lower volatility securities. Low Beta investment strategies have shown strong risk-adjusted returns over time, too.
# Negative Beta
# Stocks or portfolios with a negative beta value inversely correlate with the rest of the market. So when the S&P 500 rises, shares of these companies would go down or vice versa.
# Gold, for instance, often moves in the opposite direction as stocks, since investors tend to turn to the metal as a haven during stock volatility. Therefore, a portfolio of gold-mining companies could have a negative beta.
# So-called defensive stocks like utility companies also sometimes have negative Beta, as investors buy their shares when seeking assets less tied to the health of the economy. A downside to negative Beta is that expected returns on negative beta securities tend to be weak – even less than the risk-free interest rate.
# Zero Beta
# A stock or portfolio can also have a beta of zero, which means it’s uncorrelated with the market. Some hedge funds seek a market-neutral strategy. Being market-neutral means attempting to perform completely indifferent to how an index like the S&P 500 behaves.


#a total portfolio beta of 1.22, benchmarked to the S&P 500, means when the index moves 1%, this portfolio as a whole is 22% more risky than the index.


















# Calculate ALPHA of portfolio



# With all of that aside, I will assist you in finding the following details about the stocks:
# 1. Average annual returns based on historical data
# 2. Annual Returns on a yearly basis since the day the company got listed (to check volatility)
# 3. How individual stocks in the portfolio are related to each other (correlation)
# 4. Risk associated with the stock (deviation in average returns)
# 5. How stocks are performing with respect to the index like S&P 500 (Beta calculator)








