import numpy as np

# Imagine this is 3 days of temperatures, measured 4 times a day
grid = np.array([
    [68, 72, 75, 70],
    [65, 70, 74, 69],
    [70, 76, 80, 75]
])

#print(grid)
#print(grid.shape)      # (3, 4) — 3 rows, 4 columns
#print(grid[0])          # first row
#print(grid[0][2])       # first row, third column
#print(grid[:, 0])       # every row, first column — i.e. all "morning" readings

print(grid.mean(axis=1))  # mean temperature for each day
print(grid.mean(axis=0))  # mean temperature for each day
