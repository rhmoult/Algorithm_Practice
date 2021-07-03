def get_fibonacci(num):
    if num < 2:
        return num
    else:
        fibonacci = {0:0,1:1}
        for i in range(2,num+1):
            fibonacci[i] = fibonacci[i-1] + fibonacci[i-2]
    return fibonacci[num]

def main():
    print(get_fibonacci(10000))


if __name__ == '__main__':
    main()