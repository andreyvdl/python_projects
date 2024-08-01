import sys
from push_swap import PushSwap
from sort_three import sort_three
from selection_sort import selection_sort
from merge_insertion_sort import merge_insertion_sort


if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.exit("Missing arguments")

    ps = PushSwap()

    for i in range(1, len(sys.argv)):
        try:
            num = int(sys.argv[i])
            if num < 0:
                sys.exit("Number cannot be negative")
            elif num in ps:
                sys.exit("Cannot have duplicates")
            elif num > 2147483647:
                sys.exit(f"{num} is bigger than 214783647")
            ps.add_number(num)

        except ValueError:
            sys.exit(f'Cannot convert "{sys.argv[i]}" to int')

    ps.ready()
    if len(ps.stack_a) < 2 or ps.is_sorted():
        pass

    elif len(ps.stack_a) == 2:
        ps.swap_a()

    elif len(ps.stack_a) == 3:
        sort_three(ps)

    # elif len(ps.stack_a) < 16:
    #     selection_sort(ps)

    else:
        merge_insertion_sort(ps)

    print(ps)
