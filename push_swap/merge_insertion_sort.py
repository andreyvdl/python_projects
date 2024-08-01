from push_swap import PushSwap


def merge_insertion_sort(ps: PushSwap):
    send_all_to_b(ps, len(ps.stack_a) & 1 == 0)
    sort_biggers(ps)
    sort_rest(ps)


def send_all_to_b(ps: PushSwap, even_flag: bool):
    if even_flag:
        while len(ps.stack_a) > 0:
            ps.push_b()

    else:
        while len(ps.stack_a) > 1:
            ps.push_b()


def sort_biggers(ps: PushSwap):
    ref = int()
    if len(ps.stack_a) == 0:
        if ps.stack_b[0] < ps.stack_b[1]:
            ps.swap_b()

        ps.push_a()
        ref = ps.stack_b[0]
        ps.rot_b()

    else:
        if ps.stack_b[0] < ps.stack_b[1]:
            ps.swap_b()

        ps.push_a()
        ref = ps.stack_b[0]
        if ps.stack_a[0] > ps.stack_a[1]:
            ps.rot_rot()

        else:
            ps.rot_b()

    while ps.stack_b[0] != ref:
        if ps.stack_b[0] < ps.stack_b[1]:
            ps.swap_b()

        repeat, func = non_binary_search_pos(ps)
        for _ in range(repeat):
            func()

        ps.push_a()
        ps.rot_b()
        func = ps.rev_rot_a if func is ps.rot_a else ps.rot_a
        while not ps.is_sorted():
            func()


def sort_rest(ps: PushSwap):
    while len(ps.stack_b) > 0:
        repeat, func = non_binary_search_pos(ps)
        for _ in range(repeat):
            func()

        ps.push_a()
        func = ps.rev_rot_a if func is ps.rot_a else ps.rot_a
        while not ps.is_sorted():
            func()


# fix banary search
def non_binary_search_pos(ps: PushSwap):
    i = int()
    while i < len(ps.stack_a):
        if ps.stack_a[i] > ps.stack_b[0]:
            break

        i += 1

    if i <= len(ps.stack_a) // 2:
        return i, ps.rot_a

    return len(ps.stack_a) - i, ps.rev_rot_a
