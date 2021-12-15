with open('input') as f:
    hmap = list()
    for l in f.read().split('\n'):
        hmap.append([int(h) for h in l])

low_spots = list()
x_max = len(hmap[0]) - 1
y_max = len(hmap) - 1

# part 1
for y, line in enumerate(hmap):
    for x, height in enumerate(line):
        if x_max > x and height >= line[x + 1]:
            continue
        if x > 0 and height >= line[x-1]:
            continue
        if y_max > y and height >= hmap[y + 1][x]:
            continue
        if y > 0 and height >= hmap[y-1][x]:
            continue
        low_spots.append((y, x, height))
print("part 1:", sum([s[2] for s in low_spots]) + len(low_spots))

# part 2: basin search
basin_counts = list()
for y, x, height in low_spots:
    total_basin = set()  # eliminate duplicate basins
    new_basin_list = [(y, x, height)]
    while len(new_basin_list) > 0:
        total_basin = total_basin | set(new_basin_list)
        basin_list = new_basin_list
        new_basin_list = []
        for yb, xb, hb in basin_list:
            if x_max > xb and hb < hmap[yb][xb + 1] < 9:
                new_basin_list.append((yb, xb + 1, hmap[yb][xb + 1]))
            if xb > 0 and hb < hmap[yb][xb - 1] < 9:
                new_basin_list.append((yb, xb - 1, hmap[yb][xb - 1]))
            if y_max > yb and hb < hmap[yb + 1][xb] < 9:
                new_basin_list.append((yb + 1, xb, hmap[yb + 1][xb]))
            if yb > 0 and hb < hmap[yb - 1][xb] < 9:
                new_basin_list.append((yb - 1, xb, hmap[yb - 1][xb]))

    basin_counts.append(len(total_basin))
    if len(basin_counts) > 3:
        basin_counts = sorted(basin_counts)[1:]
print("part 2:", basin_counts[0] * basin_counts[1] * basin_counts[2])
