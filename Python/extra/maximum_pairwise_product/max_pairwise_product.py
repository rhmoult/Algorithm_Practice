# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

highest = 0
second_highest = 0
for i in range(0, n):
    if a[i] > highest:
        second_highest = highest
        highest = a[i]
    elif a[i] > second_highest:
        second_highest = a[i]

result = highest * second_highest

print(result)
