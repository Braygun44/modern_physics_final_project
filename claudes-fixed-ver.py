import numpy as np
from matplotlib import pyplot as plt

grid_size = 100
n_frames = 5000
n_choices_per_frame = n_frames // 50

grid = np.random.randint(1, 5, size=(grid_size, grid_size))

fig, ax = plt.subplots()
im = ax.imshow(grid, vmin=0, vmax=6)
plt.ion()
plt.show()

for _ in range(n_frames):
    # Add sand
    is_rand = np.random.randint(0, grid_size, size=(n_choices_per_frame, 2))
    grid[is_rand[:, 0], is_rand[:, 1]] += 1

    # Topple until stable
    while np.any(grid > 4):
        unstable = grid > 4
        grid[unstable] -= 4

        # Shift in all 4 directions, zero-pad boundaries (sand falls off edges)
        grid[1:, :]  += unstable[:-1, :]   # from above
        grid[:-1, :] += unstable[1:, :]    # from below
        grid[:, 1:]  += unstable[:, :-1]   # from left
        grid[:, :-1] += unstable[:, 1:]    # from right

    im.set_data(grid)
    fig.canvas.flush_events()