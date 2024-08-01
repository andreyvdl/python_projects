from push_swap import PushSwap


def radix_sort(ps: PushSwap):
    bit = 1
    while not ps.is_sorted():
        send_to_b(ps, bit)
        bring_back(ps)
        bit <<= 1


def send_to_b(ps: PushSwap, bit: int):
    for _ in range(len(ps.stack_a)):
        if ps.stack_a[0] & bit == 0:
            ps.push_b()

        else:
            ps.rot_a()


def bring_back(ps: PushSwap):
    while len(ps.stack_b):
        ps.push_a()
