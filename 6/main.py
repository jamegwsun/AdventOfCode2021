days_p1 = 80
days_p2 = 256
ls = [0] * 9  # max incubation (8) + 1

with open('input') as f:
    for l in f.read().split(','):
        ls[int(l)] += 1

for d in range(days_p2):
    ls.append(ls.pop(0))
    ls[6] += ls[8]
    if (d + 1) == days_p1:
        print("Day {}: {}".format((d + 1), sum(ls)))  # part 1
print("Day {}: {}".format((d + 1), sum(ls)))  # part 2
