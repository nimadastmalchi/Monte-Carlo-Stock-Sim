
"""
Monte Carlo Method to simulate a stock portfolio
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import yfinance as yf

# import data
def getData(stocks, start, end):
    stockData = yf.download(stocks, start=start, end=end)
    stockData = stockData['Close'] # only interested in day it changes
    returns = stockData.pct_change() # daily changes
    meanReturns = returns.mean()
    covMatrix = returns.cov()
    return meanReturns, covMatrix

stockList = ['CBA', 'BHP', 'TLS', 'NAB', 'WBC', 'STO']
NUM_STOCKS = len(stockList)
# yahoo expects '.AX'
stocks = [stock + '.AX' for stock in stockList]
endDate = dt.datetime.now()
startDate = endDate - dt.timedelta(days=300)

meanReturns, covMatrix = getData(stocks, startDate, endDate)

# Define weights for portfolio
weights = np.random.random(NUM_STOCKS) # 0-1 for each stock
# weights[i] is the fraction of stock i in the portfolio
weights /= np.sum(weights)

# Monte Carlo Method
MC_SIMS = 20
T = 100 # timeframe in days

# store info in each simulation
meanM = np.full(shape=(T,NUM_STOCKS), fill_value=meanReturns)
meanM = meanM.T

portfolioSims = np.full(shape=(T,MC_SIMS), fill_value=0.0)

INIT_PORTFOLIO = 10000

for m in range(0, MC_SIMS):
    # each simulation iteration generates random variables (Z)
    # and performs a Cholesky decomposition on the covariance
    # matrix. This step is necessary to generate random returns
    # for each stock that are correlated with each other.

    Z = np.random.normal(size=(T, NUM_STOCKS))
    L = np.linalg.cholesky(covMatrix) # find lower triangular matrix for cholesky decomposition

    # Compute correlated random returns for each stock
    dailyReturns = meanM + np.inner(L, Z)

    # Update portfolio
    portfolioSims[:,m] = np.cumprod(np.inner(weights,dailyReturns.T)+ 1) * INIT_PORTFOLIO

# Comptue average of all simulations
portfolioSimsAverage = np.full(shape=(T,1), fill_value=0.0)
for t in range(T):
    for s in range(MC_SIMS):
        portfolioSimsAverage[t] += portfolioSims[t][s]
    portfolioSimsAverage[t] /= MC_SIMS

import matplotlib.pyplot as plt

# Plot 1: Monte Carlo Simulations
fig1, ax1 = plt.subplots()
ax1.plot(portfolioSims)
ax1.set_ylabel('Portfolio Value ($)')
ax1.set_xlabel('Day')
ax1.set_title('Monte Carlo Simulations of a stock portfolio')

# Plot 2: Average of Monte Carlo Simulations
fig2, ax2 = plt.subplots()
ax2.plot(portfolioSimsAverage)
ax2.set_ylabel('Portfolio Value ($)')
ax2.set_xlabel('Day')
ax2.set_title('Average of all Monte Carlo Simulations')

plt.show()
