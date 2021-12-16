def find_path_recursively_p1(current_path: list, start_point: str, path_dict: dict) -> list:
    paths_taken = []
    for next_node in path_dict[start_point]:
        if next_node == 'end':
            paths_taken.append(current_path + [next_node])
        elif next_node.islower() and next_node in current_path:
            continue
        else:
            new_paths = find_path_recursively_p1(current_path=current_path + [next_node],
                                                 start_point=next_node,
                                                 path_dict=path_dict)
            paths_taken += new_paths
    return paths_taken


def find_path_recursively_p2(current_path: list, start_point: str, path_dict: dict) -> list:
    paths_taken = []
    for next_node in path_dict[start_point]:
        if next_node == 'end':
            paths_taken.append(current_path + [next_node])
            continue
        elif next_node.islower() and next_node in current_path:
            if check_duplicate_lowercase(current_path=current_path):
                continue
        new_paths = find_path_recursively_p2(current_path=current_path + [next_node],
                                             start_point=next_node,
                                             path_dict=path_dict)
        paths_taken += new_paths
    return paths_taken


def check_duplicate_lowercase(current_path: list) -> bool:
    lower_list = [n for n in current_path if n.islower()]
    return any(lower_list.count(n) > 1 for n in lower_list)


with open('input') as f:
    connects = [tuple(l.split('-')) for l in f.read().split('\n')]

nodes = sorted({x for x, y in connects} | {y for x, y in connects})
path_dict = {n: set() for n in nodes}

# build up path_dict
for x, y in connects:
    if not y == 'start':
        path_dict[x] = path_dict[x] | {y}
    if not x == 'start':
        path_dict[y] = path_dict[y] | {x}

valid_paths_p1 = find_path_recursively_p1(current_path=[], start_point='start', path_dict=path_dict)
print("part 1:", len(valid_paths_p1))

valid_paths_p2 = find_path_recursively_p2(current_path=[], start_point='start', path_dict=path_dict)
print("part 2:", len(valid_paths_p2))
