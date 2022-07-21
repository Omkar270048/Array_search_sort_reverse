import array as a
import sys

arr = a.array('i', [32,2,31, 34, 36,1])

# sort algorithm
def sort(arr):
    for x in range(len(arr)):
        for i in range(x):
            if arr[x]>arr[i]:
                temp = arr[i]
                arr[i] = arr[x]
                arr[x] = temp

    return arr

# search algorithm
def search(num, arr):
    if num in arr:
        return num, "is present at index", arr.index(num)
    else:
        return num, "not found"


#reversing algorithm
def reverse(arr):
    start = 0
    end = len(arr)-1
    while start < end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1
    return arr

def menu():
    print()
    print("array being used is", arr)
    print("Menu is:")
    print("1. search")
    print("2. sort")
    print("3. reverse")
    print("0. exit")
    option = input("Enter option :")

    while True:
        if option == "1":
            num = int(input("Enter number to search :"))
            print(search(num, arr))
            menu()
        elif option == "2":
            print(sort(arr))
            menu()
        elif option == "3":
            print(reverse(arr))
            menu()
        elif option == "0":
            print("Exiting.....")
            sys.exit()
        else:
            print("Invalid input.....")
            print("Select valid input")
            menu()

menu()
