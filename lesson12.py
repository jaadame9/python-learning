import numpy as np

#numbers = [1, 2, 3, 4, 5]
#arr = np.array(numbers)

#print(arr)
#print(type(arr))

#regular_list = [1, 2, 3, 4, 5]
#numpy_array = np.array([1, 2, 3, 4, 5])

# Try this with a regular list first:
#print(regular_list * 2)   # this DUPLICATES the list, doesn't multiply each item

#print(numpy_array * 2)      # this multiplies EACH item by 2

prices = np.array([19.99, 5.50, 12.00, 8.25])

print(prices.sum())
print(prices.mean())
print(prices.max())
print(prices.min())
print(prices[prices > 10])   # filters — only values greater than 10

temperatures = np.array([72, 75, 79, 80, 82])

print(temperatures.mean())
print(temperatures.max())
print(temperatures[temperatures > temperatures.mean()])
