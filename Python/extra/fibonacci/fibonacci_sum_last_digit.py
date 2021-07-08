# Uses python3
import sys

def fibonacci_sum_fast(num):
    # TODO: Make it take less time
    if num < 2:
        return num
    else:
        previous = 0
        current  = 1
        sum      = 1
        for i in range(2,num+1):
            previous, current = current, (current + previous) % 10
            sum += current

    return sum % 10

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_fast(n))
