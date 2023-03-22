# task 1 - TV
import math

p = 0.9
q = 1 - p
n = 100  # we suppose 100 TVs

min_p = int(0.85 * n)
max_p = int(0.95 * n)

# Bernully
prob = 0
for k in range(min_p, max_p+1):
    prob += math.comb(n, k) * p**k * q**(n-k)

print(f"Probability TV ok during service period [85; 95] supposing 100 cases: {prob:.2f}")
print()

# task2 - 40 selections
import numpy as np
import matplotlib.pyplot as plt
import statistics

elements = [10, 13, 10, 9, 9, 12, 12, 6, 7, 9, 8, 9, 11, 9, 14, 13, 9, 8, 8, 7, 10, 10, 11, 11, 11, 12, 8, 7, 9, 10, 14, 13, 8, 8, 9, 10, 11, 11, 12, 12]

unique, counts = np.unique(elements, return_counts=True)

n = len(elements)
freq = counts / n
prob = freq / sum(freq)

table = np.vstack((unique, counts, freq, prob)).T
print(table)

plt.bar(unique, freq, width=0.6, align='center')
plt.xticks(unique)
plt.xlabel('elements')
plt.ylabel('frequency')
plt.show()


mode = statistics.mode(elements)
print('mode:', mode)
median = statistics.median(elements)
print('median', median)
