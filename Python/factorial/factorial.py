# This is an implementation of the factorial function

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def main():
    print(factorial(5))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()