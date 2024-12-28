import math
import matplotlib.pyplot as plt

def prices_law(total_people):
    return math.sqrt(total_people)

# Example group sizes
group_sizes = [10, 50, 100, 500, 1000, 5000, 10000]

# Calculate productive people for each group size
productive_people = [prices_law(size) for size in group_sizes]

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(group_sizes, productive_people, marker='o')
plt.title("Price's Law Visualization")
plt.xlabel('Total Number of People')
plt.ylabel('Number of Productive People')
plt.grid(True)
plt.xscale('log')  # Use logarithmic scale for better visualization
plt.yscale('log')  # Use logarithmic scale for better visualization
plt.show()
