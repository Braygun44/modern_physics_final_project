import numpy as np
from matplotlib import pyplot as plt

grid_size = 100
n_frames = 50000
n_choices_per_frame = n_frames // 50

grid = np.array([[np.random.choice([1,2,3,4]) for _ in range(grid_size)] for _ in range(grid_size)]) # multiply grid of ones by a random choice of 1,2,3,4 for all points in the grid (i.e. create noise).

plt.imshow(grid)
plt.show()

for _ in range(n_frames):
    for _ in range(n_choices_per_frame):
        i = np.random.randint(0, grid_size-1)
        j = np.random.randint(0, grid_size-1)