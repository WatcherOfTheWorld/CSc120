def col_end_ok_at_iteration_i(grid, i, n, col):
    return len(col) == 0 or grid[i-1][n] == col[-1]