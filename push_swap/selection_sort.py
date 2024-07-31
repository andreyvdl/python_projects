from push_swap import PushSwap
from sort_three import sort_three


def selection_sort(ps: PushSwap):
    point = int()

    while len(ps.stack_a) > 3:
        for i in range(len(ps.stack_a)):
            if ps.sorted[point] == ps.stack_a[i]:
                move_and_push(ps, ps.stack_a[i], get_rot(ps, i))
                break

        point += 1

    sort_three(ps)
    for _ in range(len(ps.stack_b)):
        ps.push_a()


def get_rot(ps: PushSwap, dist: int):
    if dist <= len(ps.stack_a) // 2:
        return ps.rot_a

    return ps.rev_rot_a


def move_and_push(ps: PushSwap, num: int, rot):
    while ps.stack_a[0] != num:
        rot()

    ps.push_b()
