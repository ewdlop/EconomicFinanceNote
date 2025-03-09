import matplotlib.pyplot as plt
import math

def compound_interest(principal, rate, time, n = 1):
    return principal * (1 + rate / n) ** (n * time)

def natural_interest(principal, rate, time):
    return principal * math.exp(rate * time)

# Calculate the compound interest
principal = 1024
rate = 0.05
time = 3
n = 1
compound_interest_value = compound_interest(principal, rate, time, n)
print(f"Compound Interest: {compound_interest_value:.2f}")

# plot the compound interest
time_range = range(0, 10)
compound_interests = [compound_interest(principal, rate, t, n) for t in time_range]
plt.plot(time_range, compound_interests)
plt.xlabel('Time (years)')
plt.ylabel('Compound Interest')
plt.title('Compound Interest Over Time')
plt.show()

# Calculate the natural interest
natural_interests = [natural_interest(principal, rate, t) for t in time_range]
plt.plot(time_range, natural_interests)
plt.xlabel('Time (years)')
plt.ylabel('Natural Interest')
plt.title('Natural Interest Over Time')
plt.show()
