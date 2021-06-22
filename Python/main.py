def kGoodnessString(s, k):
    n = len(s)
    minOperations = 0
    x = 0
    for index in range(0, (n // 2)):
        if not s[index] == s[(n - index - 1)]:
            x += 1
    if x == k:
        minOperations = 0
    elif x > k:
        minOperations = x - k
    else:
        minOperations = k - x
    return minOperations


def main():
    # Number of test cases
    numberOfTestCases = int(input(""))
    for case in range(0, numberOfTestCases):
        # String length and goodness score desired:
        n, K = map(int, (input("")).split())
        # The string
        string = input("")
        minimumNumberOfOperations = kGoodnessString(string, K)
        print("Case #" + str(case + 1) + ":", minimumNumberOfOperations)


if __name__ == '__main__':
    main()
