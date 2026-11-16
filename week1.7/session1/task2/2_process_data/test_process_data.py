# Week 1.7, Session 1: Task 2 - unit test for process_data() 

# Write test functions for the values you have chosen in the equivalence classes
# for testing the functions

# Hint: you should test for empty list, list with a single value, list with multiple values
# and for positive and negative integers


from process_data import process_data


def test_empty_list():
    # complete the implementation for
    # testing an empty list
    assert process_data([]) == None
    
    
def test_one_int_list():
    # complete the implementation for 
    # testing a list with a single integer
    assert process_data([5]) == 5
    assert process_data([-9]) == -9


def test_multiple_int_list():
    # complete the implementation for
    # testing a list with multiple integers
    assert process_data([1, 2, 3]) == 6
    assert process_data([-1, -2, -9]) == -12
    assert process_data([5, -6, 9]) == 8
    
# | Empty list |[] |
# | Single integer list  |[5], [-9] |
# | Multiple integer list |[1, 2, 3], [-1, -2, -9], [5, -6, 9] |