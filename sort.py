#Первый способ
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

data = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(data)) # [11, 12, 22, 25, 34, 64, 90]

#Второй способ
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

data = [12, 11, 13, 5, 6]
print(insertion_sort(data)) # [5, 6, 11, 12, 13]
