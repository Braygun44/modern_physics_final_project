import numpy as np
from matplotlib import pyplot as plt

GRID_SIZE = 100
N_FRAMES = 5000
N_CHOICES_PER_FRAME = N_FRAMES // 100
THRESHOLD = 4
SLOPE_STRENGTH = 0.6  # 0 = flat, <1 = sloped (must be <1 or uphill factor goes negative)

# grid = (np.exp(-(((np.mgrid[-1:1:GRID_SIZE*1j, -1:1:GRID_SIZE*1j] - np.array([-1, 0])[:, None, None])**2).sum(axis=0) / 0.5)) * THRESHOLD).astype(int)
grid = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)

fig, ax = plt.subplots()
im = ax.imshow(grid, vmin=0, vmax=6, cmap='gray')
plt.ion()
plt.show()

cx, cy = GRID_SIZE // 2, GRID_SIZE // 2 # this is the loc of the peak

for _ in range(N_FRAMES):
    # Drop grains at the peak
    grid[cx, cy] += N_CHOICES_PER_FRAME

    # Topple until stable
    while np.any(grid > THRESHOLD):
        unstable = grid > THRESHOLD
        grid[unstable] -= 4

        grid[1:,  :]  += (unstable[:-1, :] * (1 + SLOPE_STRENGTH)).astype(int)  # downhill
        grid[:-1, :]  += (unstable[1:,  :] * (1 - SLOPE_STRENGTH)).astype(int)  # uphill
        grid[:,  1:]  += unstable[:, :-1]  # east
        grid[:, :-1]  += unstable[:, 1:]   # west

    im.set_data(grid)
    fig.canvas.flush_events()
    plt.pause(0.01)