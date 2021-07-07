# Uses python3
import sys


def is_pisano_period(prev, cur):
    if prev == 0 and cur == 1:
        return True
    else:
        return False


def pisano_period(m):
    previous, current = 0, 1
    for i in range(0, m*m):
        previous, current = current, (previous + current) % m

        if is_pisano_period(previous, current):
            return i + 1

def get_fibonacci_huge_mod(n, m):
    # n mod m is periodic
    # This is known as the pisano period
    period = pisano_period(m)

    # If we know where in the period n falls, we don't need to calc fib(n)
    # We can calculate fib(n mod period) faster
    n = n % period

    previous, current = 0, 1
    if n < 2:
        return n
    for i in range(n-1):
        previous, current = current, previous + current

    return current % m


def main():
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(get_fibonacci_huge_mod(n, m))


if __name__ == '__main__':
    main()
