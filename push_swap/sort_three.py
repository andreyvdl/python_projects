from push_swap import PushSwap


def sort_three(ps: PushSwap):
    while not ps.is_sorted():
        a, b, c = ps.stack_a.numbers
        if a > b and a < c:
            ps.swap_a()

        elif a > b and a > c:
            ps.rot_a()

        elif a < b and a > c:
            ps.rev_rot_a()

        elif a < b and a < c:
            ps.swap_a()
