import evaluation

def test_average():
    assert evaluation.average(1, 1, 1) == 1.0
    assert evaluation.average(1, 2, 3) == 2.0
    assert evaluation.average(3, 0, 0) == 1.0

def test_pieces_of_wood():
    assert evaluation.count_length_of_wood([10, 12, 13, 10, 15], 10) == 2
    assert evaluation.count_length_of_wood([5, 3, 10, 2], 4) == 0
    assert evaluation.count_length_of_wood([2, 2, 2, 2], 2) == 4

def test_occurance_of_board_length():
    initial_list = []
    expected = {}
    result = evaluation.occurance_of_board_length(initial_list)
    assert result == expected

    intial_list = [10, 10, 3]
    expected = {10: 2, 3: 1}
    result = evaluation.occurance_of_board_length(intial_list)
    assert result == expected

    intial_list = [5, 5, 5, 5, 5]
    expected = {5: 5}
    result = evaluation.occurance_of_board_length(intial_list)
    assert result == expected

def test_get_board_length():
    intial_dict = {10: 2, 5: 1}
    expected = 2
    result = evaluation.get_board_length(intial_dict, 10)
    assert result == expected

    intial_dict = {15: 5, 3: 1, 0: 2}
    expected = 5
    result = evaluation.get_board_length(intial_dict, 15)
    assert result == expected

    intial_dict = {}
    expected = 0
    result = evaluation.get_board_length(intial_dict, 5)
    assert result == expected