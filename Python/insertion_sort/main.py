def insertion_sort(A):
    for k in range(1, len(A)):
        cur = A[k]
        j = k
        while j > 0 and A[j-1] > cur:
            A[j] = A[j-1]
            j -= 1
        A[j] = cur
    return A

def main():
    list = [10,2,4,3,6,5,7,8,9,1]
    new_list = insertion_sort(list)
    print("New list", new_list)

if __name__ == '__main__':
    main()
