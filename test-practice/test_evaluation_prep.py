import evaluation_prep 
# from evaluation_prep import add (don't have to write 
# evaluation_prep before each function)

def test_add():
    assert evaluation_prep.add(1, 1) == 2

def test_add_list():
    assert evaluation_prep.add_list([]) == 0
    assert evaluation_prep.add_list([1, 2, 3]) == 6

def test_count_occurances():
    initial_list = []
    expected = {}
    result = evaluation_prep.count_occurances(initial_list)
    assert result == expected

    initial_list = ["hello", "hello", "hello", "bye"]
    expected = {"hello": 3, "bye": 1}
    result = evaluation_prep.count_occurances(initial_list)
    assert result == expected

    initial_list = ["hello", "bye", "bye", "hello"]
    expected = {"hello": 2, "bye": 2}
    result = evaluation_prep.count_occurances(initial_list)
    assert result == expected
