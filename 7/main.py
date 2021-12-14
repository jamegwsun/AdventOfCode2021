def calc_fuel_p1(dest: int, pos: list) -> int:
    return sum([abs(a - b) for a, b in zip(pos, [dest] * len(pos))])


def calc_fuel_p2(dest: int, pos: list) -> int:
    return sum([sum(range(abs(a - b) + 1)) for a, b in zip(pos, [dest] * len(pos))])


with open('input') as f:
    pos = [int(p) for p in f.read().split(',')]

# part 1
guess = int((max(pos) + min(pos)) / 2)
dir = 1 if calc_fuel_p1(guess + 1, pos) < calc_fuel_p1(guess, pos) else -1
# assumes local min == global min since this is a 1st order problem
while calc_fuel_p1(guess + dir, pos) < calc_fuel_p1(guess, pos):
    guess += dir
print("part 1:", calc_fuel_p1(guess, pos))

# part 2
guess = int((max(pos) + min(pos)) / 2)
dir = 1 if calc_fuel_p2(guess + 1, pos) < calc_fuel_p2(guess, pos) else -1
# hoping local min is still global min, and yup it is
while calc_fuel_p2(guess + dir, pos) < calc_fuel_p2(guess, pos):
    guess += dir
print("part 2:", calc_fuel_p2(guess, pos))
