from typing import List

def insert_at(original: List, value: int, target_index: int) -> List:
    #return original[:i] + [value] + original[i:] (python version)
    new_list = [0] * (len(original)+1) #(java version)
    index = -1
    for index in range(target_index):
        new_list[index] = original[index]

    new_list[index+1] = value 
    print(value)

    for index in range(index+2, len(new_list)):
        new_list[index] = original[index-1]

    return new_list


def insert(original: List, value: int) -> List:
    for i, num in enumerate(original):
        if num > value:
            break
        else:
            i += 1
        
    return insert_at(original, value, i)


def remove_at(original: List, i: int) -> List:
    return original[:i] + original[i+1:]