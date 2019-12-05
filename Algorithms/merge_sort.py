from typing import List
# Merge Sort

# recursive
def merge_sort(numbers: List[int]) -> List[int]:
    # base case
    if len(numbers) == 1:
        return numbers

    midpoint = len(numbers)//2
    # mergesort left
    left_side = merge_sort(numbers[:midpoint])

    # mergesort right
    right_side = merge_sort(numbers[midpoint:])

    # merge the two together
    sorted_list = []

    # loop through both lists with two markers
    left_marker = 0
    right_marker = 0
    while left_marker < len(left_side) and right_marker < len(right_side):
        if left_side[left_marker] < right_side[right_marker]:
            sorted_list.append(left_side[left_marker])
            left_marker += 1
        else:
            sorted_list.append(right_side[right_marker])
            right_marker += 1
    
    while right_marker < len(right_side):
        sorted_list.append(right_side[right_marker])
        right_marker += 1

    while left_marker < len(left_side):
        sorted_list.append(left_side[left_marker])
        left_marker += 1

    return sorted_list

print(merge_sort([1, 2, 3, 4, 5]))

print(merge_sort([5, 4, 3, 2, 1]))

    # if 1 marker is smaller, append that first, move marker over

    # if marker 2 is smaller, append that, move marker over

    # if one marker goes off the list, add the rest of the other list