# Uses python3
def get_fibonacci(num, fibonacci):
    if num < 2:
        return num
    else:
        for i in range(2,num+1):
            fibonacci[2] = fibonacci[1] + fibonacci[0]
            fibonacci[0] = fibonacci[1]
            fibonacci[1] = fibonacci[2]
    return fibonacci[2]

def main():
    n = int(input())
    starter_hash = {0:0,1:1,2:1}
    print(str(get_fibonacci(n, starter_hash))[-1])


if __name__ == '__main__':
    main()