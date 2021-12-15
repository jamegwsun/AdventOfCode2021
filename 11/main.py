import numpy as np


def find_flashes(emap: np.array) -> list:
    tens = np.where(emap >= 10)
    return [(y, x) for y, x in zip(tens[0], tens[1])]


with open('input') as f:
    emap = np.array([[int(c) for c in row] for row in f.read().split()], dtype=int)

y_max = len(emap)
x_max = len(emap[0])
flash_counts = []
p1_steps = 100
p2_steps = 100000

for step in range(p2_steps):
    emap += 1
    new_flashes = find_flashes(emap=emap)
    flash_loc = set(new_flashes)
    while len(new_flashes) > 0:
        for y, x in new_flashes:
            emap[max(y-1, 0):min(y+2, y_max), max(x-1, 0):min(x+2, x_max)] += 1
        new_flashes = [l for l in find_flashes(emap=emap) if l not in flash_loc]
        flash_loc = flash_loc | set(new_flashes)
    flash_counts.append(len(flash_loc))
    emap = np.where(emap > 9, 0, emap)
    if step == p1_steps - 1:
        print("part 1:", sum(flash_counts))
    if len(flash_loc) == 100:
        print("part 2:", step + 1)
        break

