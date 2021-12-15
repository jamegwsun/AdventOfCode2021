_possible_pos = {
    2: ['cf'],
    3: ['acf'],
    4: ['bcdf'],
    5: ['acdeg', 'acdfg', 'abdfg'],
    6: ['abcefg', 'abdefg', 'abcdfg'],
    7: ['abcdefg']
}


def decode(c_in: list) -> dict:
    decode_dict = dict()
    digits = {v: list() for v in range(2, 8)}

    for c in c_in:
        digits[len(c)].append(c)

    # 2 segments - unique
    decode_dict[digits[2][0]] = 1
    one_list = list(digits[2][0])

    # 3 segments - unique
    decode_dict[digits[3][0]] = 7
    seven_list = list(digits[3][0])

    # 4 segments - unique
    decode_dict[digits[4][0]] = 4
    four_list = list(digits[4][0])

    # 5 segments - not unique
    for d in set(digits[5]):
        # if 5 segment digit contain the number 1, the digit is 3
        if all(c in list(d) for c in one_list):
            decode_dict[d] = 3
        # How many segments does the 5 seg digit share with number 4? If 3 -> number 5, if 2 -> number 2
        elif len([c for c in list(d) if c in four_list]) == 3:
            decode_dict[d] = 5
        else:
            decode_dict[d] = 2

    # 6 segments - not unique
    for d in set(digits[6]):
        # if 6 segment digit contain the number 4, the digit is 9
        if all(c in list(d) for c in four_list):
            decode_dict[d] = 9
        # otherwise if 6 segment digit contain the number 4, the digit is 0
        elif all(c in list(d) for c in one_list):
            decode_dict[d] = 0
        # last option is number 6
        else:
            decode_dict[d] = 6

    # 7 segments - unique
    decode_dict[digits[7][0]] = 8

    return decode_dict


with open('input') as f:
    cin = [c.split(' | ') for c in f.read().split('\n')]

c_left = list()
c_right = list()
for line in cin:  # sorting code in alphabetical order
    c_left.append([''.join(sorted(char)) for char in line[0].split(' ')])
    c_right.append([''.join(sorted(char)) for char in line[1].split(' ')])

#  part 1
valid_digits = [2, 3, 4, 7]
count = 0
for c in c_right:
    count += len([s for s in c if len(s) in valid_digits])
print("part 1:", count)

# part 2: of course I need to decipher this
code_sum = 0
for i, cr in enumerate(c_right):
    decode_dict = decode(c_in=c_left[i]+c_right[i])
    cr_nums = [decode_dict[c] for c in cr]
    code_sum += int(''.join([str(n) for n in cr_nums]))
print("part 2:", code_sum)

