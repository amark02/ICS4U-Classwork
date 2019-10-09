from typing import Dict, List


def average(a: float, b: float, c:float) -> float:
    """Returns the average of 3 numbers.

    Args:
        a: A decimal number
        b: A decimal number
        c: A decimal number
    Returns:
        The average of the 3 numbers as a float
    """
    return (a + b + c)/3


def count_length_of_wood(wood: List[int], wood_length: int) -> int:
    """Finds how many pieces of wood have a specific
        board length.

    Args:
        wood: A list of integers indicating length of 
        a piece of wood
        
        wood_length: An integer that specifices what length 
        of wood a person is looking for
    Returns:
        How many pieces of wood there are for a specific 
        board length

        e.g.,
        wood = [10, 5, 10]
        wood_length = 10
        return 2
    """
    total = 0
    for piece in wood:
        if piece == wood_length:
            total += 1
        else:
            None 
    return total


def occurance_of_board_length(board_length: List[int]) -> Dict:
    """Returns a diciontary of the occurances of the length of a board. 

    Args:
        board_length: A list of integers indicating the length
        of a piece of wood
    Returns:
        Dictionary with the key being the length, and the value
        being the number of times the length appeares in the list

        e.g.,
        board_length = [10, 15, 20, 20, 10]
        return {10: 2, 15: 1, 20: 2}
    """
    occurances = {}
    for wood_length in board_length:
        if wood_length in occurances.keys():
            occurances[wood_length] += 1
        else:
            occurances[wood_length] = 1
    return occurances


def get_board_length(board_length: Dict, wood_length: int) -> int:
    """Finds out how many pieces of wood have a specific 
        board length.

    Args:
        board_length: A dictionary with the keys being the board
        length and the values being the number of boards with that
        specific length

        wood_length: An integer that specfies what length of wood
        a person is looking for
    Returns:
        How many pieces of wood there are for a specific board length
    """
    list_of_wood = []
    for key in board_length.keys():
        list_of_wood.append(key)
    
    total = 0
    for piece in list_of_wood:
        if piece == wood_length:
            total += 1
        else:
            None
    return total

""" correct answer
    for key in board_length.keys():
        if key == str(wood_length)
            return board_length[key]
    
    else: 
        return 0
"""

    

