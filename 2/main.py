with open("input") as f:
    instrs = [tuple(d.strip('\n').split(' ')) for d in f]

# part 1
loc_p1 = [0, 0]  # [horizontal, depth]
instr_dict_p1 = {
    "forward": [1, 0],
    "backward": [-1, 0],
    "down": [0, 1],
    "up": [0, -1]
}

for (instr, dist) in instrs:
    dist = [int(dist) for _ in range(len(loc_p1))]
    loc_p1 = [a * b + c for a, b, c in zip(instr_dict_p1[instr], dist, loc_p1)]
print("part 1: " + str(loc_p1[0] * loc_p1[1]))

# part 2
loc_p2 = [0, 0, 0]  # [horizontal, depth, aim]
instr_dict_p2 = {
    "forward": [1, 1, 0],
    "backward": [-1, -1, 0],
    "down": [0, 0, 1],
    "up": [0, 0, -1]
}
for instr, dist in instrs:
    dist = [int(dist) for _ in range(len(loc_p2))]
    aim_multi = [1, loc_p2[2], 1]
    loc_p2 = [a * b * d + c for a, b, c, d in zip(instr_dict_p2[instr], dist, loc_p2, aim_multi)]
print("part 2: " + str(loc_p2[0] * loc_p2[1]))
