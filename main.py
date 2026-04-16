import numpy as np
from matplotlib import pyplot as plt

grid_size = 100
n_frames = 5000
n_choices_per_frame = n_frames // 50

grid = np.array([[np.random.choice([1,2,3,4]) for _ in range(grid_size)] for _ in range(grid_size)]) # multiply grid of ones by a random choice of 1,2,3,4 for all points in the grid (i.e. create noise).

plt.imshow(grid)
plt.show()

for _ in range(1):
    for _ in range(n_choices_per_frame):
        i = np.random.randint(0, grid_size-1)
        j = np.random.randint(0, grid_size-1)
        grid[i, j] += 1
    if True not in grid > 4:
        continue
    else:
        while True in grid > 4:
            idxs = np.where(grid > 4)
            i_idx = idxs[0]
            j_idx = idxs[1]
            #TODO choose random vertex over 4
            #TODO topple that vertex
            #TODO add to neighbor vertices
            #TODO handle edge cases (ignore; not parabolic)