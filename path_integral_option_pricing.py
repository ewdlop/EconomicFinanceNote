def payoff(S, K):
    return np.maximum(S - K, 0)

def integrand(S, S0, K, T, r, sigma):
    return payoff(S, K) * np.exp(-(np.log(S / S0) - (r - 0.5 * sigma**2) * T)**2 / (2 * sigma**2 * T)) / (S * sigma * np.sqrt(2 * np.pi * T))

def path_integral_option_pricing(S0, K, T, r, sigma):
    # Calculate the option price using numerical integration
    option_price, _ = quad(integrand, 0, np.inf, args=(S0, K, T, r, sigma))
    option_price *= S0 * np.exp(-r * T)
    return option_price

# Parameters for the Black-Scholes model
S0 = 100  # Current stock price
K = 105   # Strike price
T = 1     # Time to maturity (1 year)
r = 0.05  # Risk-free rate
sigma = 0.2  # Volatility of the underlying asset

# Calculate the European call option price
call_price = path_integral_option_pricing(S0, K, T, r, sigma)
print(f"European Call Option Price: {call_price:.2f}")
