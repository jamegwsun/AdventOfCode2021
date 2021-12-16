import numpy as np

with open('input') as f:
    raw = [l for l in f.read().split('\n\n')]

points = [tuple(int(n) for n in l.split(',')) for l in raw[0].split('\n')]
folds = []
for l in raw[1].split('\n'):
    instr = l.strip('fold along ').split('=')
    folds.append((instr[0], int(instr[1])))

y_max = max([p[1] for p in points]) + 1
x_max = max([p[0] for p in points]) + 1

grid = np.zeros((y_max, x_max), dtype=int)

for p in points:
    grid[p[1], p[0]] = 1

for i, (direction, coordinate) in enumerate(folds):
    if direction == 'y':
        grid = grid[0:coordinate, :] | np.flip(grid[coordinate+1:y_max, :], 0)
    else:
        grid = grid[:, 0:coordinate] | np.flip(grid[:, coordinate+1:x_max], 1)
    if i == 0:
        print('part 1', np.sum(grid))

grid = grid.astype('str')
grid = np.where(grid == '0', ',', grid)
grid = np.where(grid == '1', '#', grid)
print('part 2:')
last = 0
for x in range(int(grid.shape[1]/8), grid.shape[1] + int(grid.shape[1]/8), int(grid.shape[1]/8)):
    print(grid[:, last:x-1], '\n')
    last = x
