with open('input') as f:
    raw = [l for l in f.read().split('\n\n')]

template = raw[0]
rules = {l.split(' -> ')[0]: l.split(' -> ')[1] for l in raw[1].split('\n')}
steps = 40

pair_counts = {rule: 0 for rule in rules.keys()}
for i in range(len(template) - 1):
    pair_counts[template[i:i+2]] += 1

for s in range(steps):
    new_pair_counts = {rule: 0 for rule in rules.keys()}
    for pair, count in pair_counts.items():
        monomer = rules[pair]
        new_pair_counts[pair[0] + monomer] += count
        new_pair_counts[monomer + pair[1]] += count
    pair_counts = new_pair_counts

monomer_counts = {m: 0 for m in set(rules.values())}
for pair, count in pair_counts.items():
    monomer_counts[pair[0]] += count / 2
    monomer_counts[pair[1]] += count / 2

monomer_counts[template[0]] += 1/2
monomer_counts[template[-1]] += 1/2

# too lazy to add in part 1
print("part 2:", int(max(monomer_counts.values()) - min(monomer_counts.values())))