import pytest
import calculator as calc

INVALID_INPUT_MESSAGE = "Input values must be numbers."
DIVIDE_BY_ZERO_MESSAGE = "Can\'t divide by zero."

def test_input_validation():
    with pytest.raises(ValueError) as e_info:
        calc.sum(3.9, 'abc') # pragma: no mutate
    e_message = str(e_info.value)
    assert INVALID_INPUT_MESSAGE == e_message
    
def test_calculator_sum():
    assert calc.sum(65, 355) == 420

def test_calculator_sum_float():
    assert calc.sum(3.9, 4.2) == pytest.approx(8.1)   

def test_calculator_sum_string_error():
    with pytest.raises(ValueError) as e_info:
        calc.sum(3.9, 'abc') # pragma: no mutate
    e_message = str(e_info.value)
    assert INVALID_INPUT_MESSAGE == e_message

def test_calculator_subtraction():
    assert calc.subtract(23, 40) == -17

def test_calculator_subtraction_float():
    assert calc.subtract(3.9, -4.2) == pytest.approx(8.1)   

def test_calculator_subtraction_string_error(): 
    with pytest.raises(ValueError) as e_info:
        calc.subtract(3.9, 'abc') # pragma: no mutate
    e_message = str(e_info.value)
    assert INVALID_INPUT_MESSAGE == e_message

def test_calculator_multiplication():
    assert calc.mult(3, 7) == 21

def test_calculator_multiplication_float():
    assert calc.mult(3, 7.4) == pytest.approx(22.2)

def test_calculator_multiplication_string_error():
    with pytest.raises(ValueError) as e_info:
        calc.mult(3.9, 'abc') # pragma: no mutate
    e_message = str(e_info.value)
    assert INVALID_INPUT_MESSAGE == e_message

def test_calculator_division():
    assert calc.div(10, 4) == pytest.approx(2.5)

def test_calculator_division_float():
    assert calc.div(26.25, 7.5) == pytest.approx(3.5)

def test_calculator_division_string_error():
    with pytest.raises(ValueError) as e_info:
        calc.div(3.9, 'abc') # pragma: no mutate
    e_message = str(e_info.value)
    assert INVALID_INPUT_MESSAGE == e_message

def test_calculator_division_by_zero():
    with pytest.raises(ValueError) as e_info:
        calc.div(3.9, 0) # pragma: no mutate
    e_message = str(e_info.value)
    assert DIVIDE_BY_ZERO_MESSAGE == e_message