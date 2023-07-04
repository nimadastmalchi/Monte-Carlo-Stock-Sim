# Monte Carlo Simulation of a Stock Portfolio

This code utilizes the Monte Carlo method to simulate the performance of a stock portfolio.
Historical stock price data is obtained from Yahoo Finance using the yfinance library.
The mean returns and covariance matrix are calculated based on the stock data.
Random weights are assigned to each stock in the portfolio.
The Monte Carlo simulation is run a specified number of times (MC_SIMS) over a given timeframe (T).
For each simulation, random variables (Z) are generated, and a Cholesky decomposition is performed on the covariance matrix to obtain correlated random returns for each stock.
The portfolio value is updated based on the computed returns using the assigned weights.
The portfolio values for each simulation are stored and used to calculate the average portfolio value over time.

## Sample output
<img width="638" alt="image" src="https://github.com/nimadastmalchi/Monte-Carlo-Stock-Sim/assets/60092567/1e6b584a-7e66-4add-8c5e-8912ccdb2bfa">
<img width="632" alt="image" src="https://github.com/nimadastmalchi/Monte-Carlo-Stock-Sim/assets/60092567/46a2653a-534e-4516-ac0d-c8c8490022f6">
