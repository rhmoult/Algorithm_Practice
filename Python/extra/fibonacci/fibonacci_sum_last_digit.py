# Uses python3
import sys


def fibonacci_last_digit(n):
    current = 0
    next = 1
    for x in range(n):
        oldNext = next
        next = (current + next) % 10
        current = oldNext
    return current


if __name__ == '__main__':
    #input = sys.stdin.read()
    input = "832564823476"
    n = int(input) + 2
    n = n % 60
    print(str(((fibonacci_last_digit(n)) -1) % 10) )
