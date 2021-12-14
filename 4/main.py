def play_p1(nums: list, boards: list, win_conds: list):
    trackers = [list() for b in boards]
    for num in nums:
        for i, b in enumerate(boards):
            match = [j for j, v in enumerate(b) if v == num]
            trackers[i] += match
            pos_wc = [wc for wc in win_conds if any(m in wc for m in match)]
            if any(all(w in trackers[i] for w in wc) for wc in pos_wc):
                uncalled_sum = sum([v for j, v in enumerate(b) if not j in trackers[i]])
                print("part 1:", uncalled_sum * num)
                return


def play_p2(nums: list, boards: list, win_conds: list):
    trackers = [list() for b in boards]
    active_boards = boards
    for num in nums:
        print(num)
        round_winners = []
        for i, b in enumerate(active_boards):
            match = [j for j, v in enumerate(b) if v == num]
            trackers[i] += match
            pos_wc = [wc for wc in win_conds if any(m in wc for m in match)]
            if any(all(w in trackers[i] for w in wc) for wc in pos_wc):
                round_winners.append(i)
                if len(active_boards) == 1:
                    uncalled_sum = sum([v for j, v in enumerate(active_boards[0]) if not j in trackers[i]])
                    print("part 2:", uncalled_sum * num)
                    return
        round_winners.sort(reverse=True)
        for i in round_winners:
            active_boards.pop(i)
            trackers.pop(i)
    raise Exception('All boards did not finish')


with open("input") as f:
    boards = f.read().split('\n\n')
    nums = [int(n) for n in boards.pop(0).split(',')]

boards = [b.split('\n') for b in boards]
for i, b in enumerate(boards):
    boards[i] = [int(v) for v in ' '.join(b).split(' ') if v]

bdim = len(b)
rows = [list(range(i * bdim, i * bdim + bdim, 1)) for i in range(bdim)]
cols = [list(range(i, i + bdim ** 2, bdim)) for i in range(bdim)]
# diag1 = [i * (bdim + 1) for i in range(bdim)]
# diag2 = [(i+1) * bdim - i - 1 for i  in range(bdim)]
win_conds = rows + cols  # WTF WE'RE NOT PLAYING DIAGONALS?

play_p1(nums=nums, boards=boards, win_conds=win_conds)
play_p2(nums=nums, boards=boards, win_conds=win_conds)
