import numpy as np
from matplotlib import pyplot as plt

grid_size = 100
n_frames = 5000
n_choices_per_frame = n_frames // 1000

grid = np.array([[np.random.choice([1,2,3,4]) for _ in range(grid_size)] for _ in range(grid_size)]) # multiply grid of ones by a random choice of 1,2,3,4 for all points in the grid (i.e. create noise).

fig, ax = plt.subplots()
im = ax.imshow(grid, vmin=0, vmax=6, cmap='gray')
plt.ion()
plt.show()

for _ in range(n_frames):
    for _ in range(n_choices_per_frame):
        i = np.random.randint(0, grid_size)
        j = np.random.randint(0, grid_size)
        grid[i, j] += 1
    if not np.any(grid > 4):
        continue
    else:
        while np.any(grid > 4):
            # Topple until stable
            while np.any(grid > 4):
                unstable = grid > 4
                grid[unstable] -= 4

                # Shift in all 4 directions, zero-pad boundaries (sand falls off edges)
                grid[1:, :] += unstable[:-1, :]  # from above
                grid[:-1, :] += unstable[1:, :]  # from below
                grid[:, 1:] += unstable[:, :-1]  # from left
                grid[:, :-1] += unstable[:, 1:]  # from right

    im.set_data(grid)
    fig.canvas.flush_events()