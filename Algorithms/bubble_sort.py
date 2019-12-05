from typing import List

def bubble_sort(numbers: List[int]) -> List[int]:
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i range(0, len(numbers)-1)
        current_num = numbers[i]
        next_num = numbers[i+1]
        if next_num < current_num:
            numbers[i+1] = current_num
            numbers[i] = next_num
            is_sorted = False
    if is_sorted == False:
        break
 
