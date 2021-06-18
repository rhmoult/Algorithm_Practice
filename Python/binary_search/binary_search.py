# This is an implementation of binary search

def binary_search(data, target, low, high, iter):
    print("Iteration:", iter)
    iter += 1
    print("Midpoint is:", data[(low + high) // 2])
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            # Recur on next lower midpoint
            return binary_search(data, target, low, mid - 1, iter)
        else:
            # Recur on next higher midpoint
            return binary_search(data, target, mid + 1, high, iter)


def main():
    print(binary_search([1,2,3,4, 5, 6], 3, 1, 6, 0))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
