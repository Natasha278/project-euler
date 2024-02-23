
def count_paths(grid, i, j):
  if i == len(grid) - 1 and j == len(grid) - 1:
    return 1
  elif i == len(grid) - 1:
    return count_paths(grid, i, j + 1)
  elif j == len(grid) - 1:
    return count_paths(grid, i + 1, j)
  else:
    if grid[i][j] == 0:
      grid[i][j] = count_paths(grid, i + 1, j) + count_paths(grid, i, j + 1)
    return grid[i][j]

grid = [[0] * 21 for _ in range(21)]
number_of_paths = count_paths(grid, 0, 0)

print(number_of_paths)


