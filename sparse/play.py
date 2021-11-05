import numpy as np
from matplotlib import pyplot as plt

import objects
from conway import iterate
from types_conway import Field, Grid

MAX_ITERATIONS = 50

X_MIN = 0
X_MAX = 10
Y_MIN = -10
Y_MAX = 0


def sanity_check():
    for item in (X_MIN, X_MAX, Y_MIN, Y_MAX):
        assert isinstance(item, int)
    for upper, lower in ((X_MAX, X_MIN), (Y_MAX, Y_MIN)):
        assert upper > lower


def convert_to_grid(field: Field) -> Grid:
    x = np.arange(X_MIN, X_MAX + 1)
    y = np.arange(Y_MIN, Y_MAX + 1)
    grid = np.zeros((len(x), len(y)))
    for cell in field:
        try:
            grid[cell[0] - X_MIN, cell[1] - Y_MIN] = 1
        except IndexError:
            pass
    return grid.T


field = objects.glider
fig: plt.Figure = plt.figure(figsize=(5, 5))
ax: plt.Axes = fig.add_axes([0, 0, 1, 1])

for i in range(MAX_ITERATIONS):
    grid = convert_to_grid(field)
    ax.imshow(grid, cmap="Greys")
    fig.savefig(str(i).zfill(len(str(MAX_ITERATIONS))) + ".png")
    ax.cla()
    field = iterate(field)
