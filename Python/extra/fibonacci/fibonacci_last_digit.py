# Uses python3
def get_fibonacci(num, fibonacci):
    if num < 2:
        return num
    else:
        for i in range(2,num+1):
            fibonacci[i] = (fibonacci[i-1] + fibonacci[i-2]) % 10
    return fibonacci[num]

def main():
    n = int(input())
    starter_array = list(range(0,n+1))
    print(str(get_fibonacci(n, starter_array))[-1])


if __name__ == '__main__':
    main()