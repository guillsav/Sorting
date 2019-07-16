# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i, len(arr)):
            if arr[j] < arr[smallest_index]:
                cur_index = j
                smallest_index = cur_index

        # TO-DO: swap
        temp = arr[i]
        arr[i] = arr[smallest_index]
        arr[smallest_index] = temp

    return arr


list_to_sort = [5, 8, 3, 10, 1]

selection_sort(list_to_sort)
print(list_to_sort)


# TO-DO:  implement the Bubble Sort function below

def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr


bubble_sort(list_to_sort)
print(list_to_sort)

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
