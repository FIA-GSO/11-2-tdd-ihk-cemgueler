from my_functions import my_function, my_other_function

def test_my_function_too_short():
    assert my_function("hi") == "too short"

def test_my_function_too_long():
    assert my_function("CemSamyGüler") == "too long"

def test_my_function_just_right():
    assert my_function("abcdef") == "just right"

# Tests for my_other_function
def test_my_other_function_both_true():
    assert my_other_function(True, True) == "one is true, two is true"

def test_my_other_function_one_true_two_false():
    assert my_other_function(True, False) == "one is false, two is false"

def test_my_other_function_both_false():
    assert my_other_function(False, False) == ""

def test_my_other_function_one_false_two_true():
    assert my_other_function(False, True) == ""


