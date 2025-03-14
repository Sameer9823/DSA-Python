
def swap_kth_element(arr, n, k):
    arr[k-1], arr[n-k] = arr[n-k], arr[k-1]
    return arr

n = int(input("Enter the size of array: "))
k = int(input("Enter the number: "))

arr = list(map(int, input("enter the number ").split()))

print(swap_kth_element(arr, n, k))