def find_smallest(array):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1,len(array)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(array):
    new_array = []
    for i in range(len(array)):
        smallest = find_smallest(array)
        new_array.append(array.pop(smallest))
    return new_array
