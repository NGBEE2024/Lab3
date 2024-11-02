# Lab3_test.py
import Lab3

def test_bubble_sort_empty():
    input_arr = []
    expected = []
    assert Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING) == expected

def test_bubble_sort_ascending():
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    expected = [11, 12, 22, 25, 34, 64, 90]
    assert Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING) == expected

def test_bubble_sort_descending():
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    expected = [90, 64, 34, 25, 22, 12, 11]
    assert Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING) == expected

def test_bubble_sort_invalid_order():
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    expected = []
    # Invalid sorting order, should return empty array
    assert Lab3.bubble_sort(input_arr, 3) == expected

def test_validate_and_sort_empty():
    input_list = [""]
    expected = 0
    assert Lab3.validate_and_sort(input_list) == expected

def test_validate_and_sort_invalid():
    input_list = ["64", "34", "notanumber", "90"]
    expected = 2
    assert Lab3.validate_and_sort(input_list) == expected

def test_validate_and_sort_more_than_10():
    input_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
    expected = 1
    assert Lab3.validate_and_sort(input_list) == expected

def test_validate_and_sort_valid():
    input_list = ["64", "34", "25", "12", "22", "11", "90"]
    expected = [64, 34, 25, 12, 22, 11, 90]
    assert Lab3.validate_and_sort(input_list) == expected
