def binary_search(arr, x):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]

        if mid_value == x:
            return mid  
        elif mid_value < x:
            low = mid + 1  
        else:
            high = mid - 1  

    return -1 

sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
search_value = 7

result = binary_search(sorted_array, search_value)

if  result != -1:
    print(f"Число {search_value} найдено в массиве под индексом {result}.")
else:
    print(f"Число {search_value} не найдено в массиве.")
