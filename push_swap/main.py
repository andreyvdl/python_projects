import sys
from push_swap import PushSwap


if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.exit("Missing arguments")

    ps = PushSwap()

    for i in range(1, len(sys.argv)):
        try:
            num = int(sys.argv[i])
            ps.stack_a.numbers.append(num)
        except Exception:
            sys.exit("Cannot convert to int")

    print(ps)
