

# def stringModified(s):
#     return s.replace(" ", "")
    
# s = input("enter string: ")
# # print(stringModified(s))

def join_string(arr):
    return " ".join(arr).replace(" ", "")

arr = input("enter string: ").split()
print(join_string(arr))