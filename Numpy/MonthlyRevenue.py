import numpy as np

# Monthly revenue data (12 months)
revenue = np.array([50000, 55000, 60000, 58000, 62000, 65000,
                    70000, 72000, 68000, 75000, 80000, 85000])

print("Monthly Revenue Report")
print("-" * 30)

print("Revenue Data:\n", revenue)

print("Total Annual Revenue:", np.sum(revenue))
print("Average Monthly Revenue:", np.mean(revenue))
print("Highest Revenue:", np.max(revenue))
print("Lowest Revenue:", np.min(revenue))
print("Monthly Revenue increases 5% is:",revenue*1.05)