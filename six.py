def kth(arr, k):
    arr.sort()
    return arr[-k]


n = int(input("Enter the size of array: "))
k = int(input("Enter the number: "))

arr = list(map(int, input("enter the number ").split()))

print(kth(arr, k))