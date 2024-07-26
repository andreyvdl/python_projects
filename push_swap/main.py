import sys
from push_swap import PushSwap


if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.exit("Missing arguments")

    ps = PushSwap()

    for i in range(1, len(sys.argv)):
        try:
            num = int(sys.argv[i])
            if num < 0:
                sys.exit("Cannot be negative")
            elif num in ps:
                sys.exit("Cannot have duplicates")
            elif num > 2147483647:
                sys.exit(f"{num} is too large")
            ps.add_number(num)
        except ValueError:
            sys.exit(f"Cannot convert {num} to int")

    ps.ready()
    if len(ps.stack_a) < 2 or ps.is_sorted():
        pass
    elif len(ps.stack_a) == 2:
        ps.swap_a()
    elif len(ps.stack_a) == 3:
        ps.sort_three()
    elif len(ps.stack_a) < 10:
        ps.selection_sort()
    else:
        ps.merge_insertion_sort()

    print(ps)
