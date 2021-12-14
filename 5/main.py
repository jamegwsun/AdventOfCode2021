with open('input') as f:
    lines = [l.strip('\n').split(' -> ') for l in f]

lines = [[tuple([int(v) for v in line[0].split(',')]),
          tuple([int(v) for v in line[1].split(',')])] for line in lines]

span_dict_hv = dict()
span_dict_diag = dict()
for p1, p2 in lines:
    span = set()
    # part 1
    if p1[0] == p2[0] or p1[1] == p2[1]:
        span = {(x, p1[1]) for x in range(p1[0], p2[0] + 1)} | {(x, p1[1]) for x in range(p2[0], p1[0] + 1)} | \
               {(p1[0], y) for y in range(p1[1], p2[1] + 1)} | {(p1[0], y) for y in range(p2[1], p1[1] + 1)}
        for s in list(span):
            span_dict_hv[s] = 1 if s not in span_dict_hv.keys() else span_dict_hv[s] + 1
    # part 2
    elif (p1[0] - p2[0]) / (p1[1] - p2[1]) == 1:
        span = {(p1[0] + i, p1[1] + i) for i in range(p2[0] - p1[0] + 1)} | \
               {(p2[0] + i, p2[1] + i) for i in range(p1[0] - p2[0] + 1)}
    elif (p1[0] - p2[0]) / (p1[1] - p2[1]) == -1:
        span = {(p1[0] + i, p1[1] - i) for i in range(p2[0] - p1[0] + 1)} | \
               {(p1[0] - i, p1[1] + i) for i in range(p1[0] - p2[0] + 1)}
    for s in list(span):
        span_dict_diag[s] = 1 if s not in span_dict_diag.keys() else span_dict_diag[s] + 1

print("part 1:", len([s for s, v in span_dict_hv.items() if v > 1]))
print("part 2:", len([s for s, v in span_dict_diag.items() if v > 1]))

