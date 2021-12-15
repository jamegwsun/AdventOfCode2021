pairs = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}

rev_pairs = {v: k for k, v in pairs.items()}

p2_values = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

with open('input') as f:
    lines = [line for line in f.read().split('\n')]

errors = list()
repairs = list()
for i, line in enumerate(lines):
    buffer = []
    repair = 0
    error = None
    for char in line:
        if char in ['(', '[', '{', '<']:
            buffer.append(char)
        elif buffer[-1] == pairs[char]:
            buffer.pop(-1)
        else:
            error = char
            break
    if error:
        errors.append(error)
    else:
        for char in reversed(buffer):
            repair = repair * 5 + p2_values[rev_pairs[char]]
        repairs.append(repair)

print("part 1:", errors.count(')') * 3 + errors.count(']') * 57 + errors.count('}') * 1197 + errors.count('>') * 25137)
print("part 2:", sorted(repairs)[int((len(repairs)-1)/2)])