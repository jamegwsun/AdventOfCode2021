with open("input") as f:
    codes = [n.strip('\n') for n in f]
    transpose = [n for n in map(list, zip(*codes))]

# part 1
most_common_p1 = str()
least_common_p1 = str()
for line in transpose:
    k = max(line, key=line.count)
    most_common_p1 += k
    least_common_p1 += str(int(not (bool(int(k)))))
print("part 1:", int(most_common_p1, 2) * int(least_common_p1, 2))

# part 2
most_common_p2 = str()
most_common_indices = [i for i, _ in enumerate(range(len(transpose[0])))]
for line in transpose:
    line_most_common = [v for k, v in enumerate(line) if k in most_common_indices]
    count_one = line_most_common.count('1')
    count_zero = line_most_common.count('0')
    if count_one == count_zero:
        most_common_p2 += '1'
    else:
        most_common_p2 += str(int(count_one > count_zero))
    most_common_indices = [j for j, v in enumerate(line) if v == most_common_p2[-1] and j in most_common_indices]
    if len(most_common_indices) == 1:
        most_common_p2 = codes[most_common_indices[0]]
        break

least_common_p2 = str()
least_common_indices = [i for i, _ in enumerate(range(len(transpose[0])))]
for line in transpose:
    line_least_common = [v for k, v in enumerate(line) if k in least_common_indices]
    count_one = line_least_common.count('1')
    count_zero = line_least_common.count('0')
    if count_one == count_zero:
        least_common_p2 += '0'
    else:
        least_common_p2 += str(int(count_zero > count_one))
    least_common_indices = [j for j, v in enumerate(line) if v == least_common_p2[-1] and j in least_common_indices]
    if len(least_common_indices) == 1:
        least_common_p2 = codes[least_common_indices[0]]
        break

print("part 2:", int(most_common_p2, 2) * int(least_common_p2, 2))
