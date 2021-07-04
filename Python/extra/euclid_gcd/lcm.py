# Uses python3
import sys

def euclid_gcd(a, b):
    if b == 0:
        return a
    else:
        a_prime = a % b
        return euclid_gcd(b, a_prime)

def lcm(a, b):
    return abs(a*b) // euclid_gcd(a, b)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))

