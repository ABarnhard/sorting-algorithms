def selection_sort(list_to_sort):
    for i in range(len(list_to_sort)):
        min_index = i
        for j in range(i + 1, len(list_to_sort)):
            if list_to_sort[j] < list_to_sort[min_index]:
                min_index = j
        list_to_sort[i], list_to_sort[min_index] = list_to_sort[min_index], list_to_sort[i]

nums = [20, 3, 7, 56, 2, 77, 100, 43, 698, 1]
selection_sort(nums)

print(nums)

pass
