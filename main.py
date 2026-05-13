import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

grid = np.zeros ((50, 50), dtype=int)

# blinker - vertical, centre column
grid[2, 3] = 1
grid[3, 4] = 1
grid[4, 2] = 1
grid[4, 3] = 1
grid[4, 4] = 1

def update(frame):
    global grid

    # get the neighbouars of the grid spots
    neighbours = (
        np.roll(grid, 1, axis=0) + # N
        np.roll(grid, -1, axis=0) + # S
        np.roll(grid, 1, axis=1) + # E
        np.roll(grid, -1, axis=1) + # W
        np.roll(np.roll(grid, 1, axis=0), 1, axis=1) +
        np.roll(np.roll(grid, 1, axis=0), -1, axis=1) +
        np.roll(np.roll(grid, -1, axis=0), 1, axis=1) +
        np.roll(np.roll(grid, -1, axis=0), -1, axis=1)
    )

    new_grid = np.zeros_like(grid)

    # rule: live cell with 2-3 neighbours survives
    new_grid[(grid == 1) & ((neighbours == 2) | (neighbours == 3))] = 1
    # rule: dead cell with exactly 3 neighbours becomes alive
    new_grid[(grid == 0) & (neighbours == 3)] = 1

    grid = new_grid

    im.set_data(grid)
    return (im,)

fig, ax = plt.subplots()
ax.axis('off')
im = ax.imshow(grid, cmap='binary', interpolation='nearest')

ani = animation.FuncAnimation(
    fig, update,
    frames=200, interval=100, blit=True
)

plt.show()
