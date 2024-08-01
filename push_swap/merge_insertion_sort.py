from push_swap import PushSwap

'''
1. Group the elements of X into _n/2_ pairs of elements, arbitrarily,
leaving one element unpaired if there is an odd number of elements.
2. Perform [n/2] comparisons, one per pair, to determine the larger of the
two elements in each pair.
3. Recursively sort the _n/2_ larger elements from each pair, creating a
sorted sequence S of _n/2_ of the input elements, in ascending order.
4. Insert at the start of S the element that was paired with the first and
smallest element of S.
5. Insert the remaining ^n/2^-1 elements of X\\S into one at a time, with a
specially chosen insertion ordering described below. Use binary search in
subsequences of S to determine the position at which each element should
be inserted.
'''


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

        repeat, func = binary_search_pos(ps)
        for _ in range(repeat):
            func()

        ps.push_a()
        if ps.stack_a[0] > ps.stack_a[1]:
            ps.swap_a()
        ps.rot_b()
        if func is ps.rot_a:
            for _ in range(repeat):
                ps.rev_rot_a()

        else:
            for _ in range(repeat):
                ps.rot_a()


def sort_rest(ps: PushSwap):
    print(ps)
    while len(ps.stack_b) > 0:
        repeat, func = binary_search_pos(ps)
        print(repeat)
        for _ in range(repeat):
            func()

        ps.push_a()
        if ps.stack_a[0] > ps.stack_a[1]:
            ps.swap_a()

        if func is ps.rot_a:
            for _ in range(repeat):
                ps.rev_rot_a()

        else:
            for _ in range(repeat):
                ps.rot_a()

        print(ps)


# fix banary search
def binary_search_pos(ps: PushSwap):
    left = int()
    right = len(ps.stack_a)
    mid = 42

    while left < right and mid != 0:
        mid = (right - left) // 2
        if ps.stack_a[left + mid] < ps.stack_b[0]:
            left = left + mid + 1

        else:
            right = left + mid - 1

    if left <= len(ps.stack_a) // 2:
        return left, ps.rot_a

    return left, ps.rev_rot_a
