with open("input") as f:
    depths = [int(d.strip('\n')) for d in f]

inc_counter_p1 = inc_counter_p2 = 0

# part 1
for i in range(1, len(depths)):
    if depths[i] > depths[i-1]:
        inc_counter_p1 += 1
print("Part 1: " + str(inc_counter_p1))

# part 2
for i in range(3, len(depths)):
    if sum(depths[i-2:i+1]) > sum(depths[i-3:i]):
        inc_counter_p2 += 1
print("Part 2: " + str(inc_counter_p2))
