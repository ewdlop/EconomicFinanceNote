#!/usr/bin/env python3

#!pip install numpy pandas matplotlib scipy

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm

# Define the expected returns and covariance matrix of the assets
# Define the expected returns and covariance matrix of the assets

expected_returns = np.array([0.12, 0.18])
cov_matrix = np.array([[0.1, 0.02], [0.02, 0.08]])

# Define the weights of the assets in the portfolio
weights = np.array([0.6, 0.4])

# Calculate the portfolio return
portfolio_return = np.dot(weights, expected_returns)

# Calculate the portfolio risk (standard deviation)
portfolio_risk = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))

print(f"Expected Portfolio Return: {portfolio_return:.2f}")
print(f"Portfolio Risk (Standard Deviation): {portfolio_risk:.2f}")

# Generate random portfolios
num_portfolios = 10000
results = np.zeros((3, num_portfolios))

for i in range(num_portfolios):
    weights = np.random.random(2)
    weights /= np.sum(weights)
    portfolio_return = np.dot(weights, expected_returns)
    portfolio_risk = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
    results[0,i] = portfolio_return
    results[1,i] = portfolio_risk
    results[2,i] = results[0,i] / results[1,i]  # Sharpe Ratio

# Plot the efficient frontier
plt.scatter(results[1,:], results[0,:], c=results[2,:], cmap='viridis')
plt.colorbar(label='Sharpe Ratio')
plt.xlabel('Risk (Standard Deviation)')
plt.ylabel('Return')
plt.title('Efficient Frontier')
plt.show()

def black_scholes_call(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    call_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    return call_price

# Parameters for the Black-Scholes model
S = 100  # Current stock price
K = 105  # Strike price
T = 1    # Time to maturity (1 year)
r = 0.05  # Risk-free rate
sigma = 0.2  # Volatility of the underlying asset

# Calculate the call option price
call_price = black_scholes_call(S, K, T, r, sigma)
print(f"Call Option Price: {call_price:.2f}")
