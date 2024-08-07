import sys

if __name__ == "__main__":
    if len(sys.argv) < 5 or len(sys.argv) > 6:
        print("Usage: n_philos life_span lunch_span sleep_span [n_meals]")
        sys.exit(1)

    for arg in sys.argv[1:]:
        if not arg.isdigit():
            print("Arguments must be integers.")
            sys.exit(2)

    n_philos, life_span, lunch_span, sleep_span = map(int, sys.argv[1:5])
    n_meals = int(sys.argv[5]) if len(sys.argv) == 6 else None

