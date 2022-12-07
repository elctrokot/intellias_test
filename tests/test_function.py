import pytest
from func.get_customers import get_customers

@pytest.mark.parametrize("input_data, expected_result", [
    ((1, 12), ['Byron Fields', 'Charles Morris', 'Emma Wong', 'Eve Holt', 'George Bluth',
                                    'George Edwards', 'Janet Weaver', 'Lindsay Ferguson', 'Michael Lawson',
                                    'Rachel Howell', 'Tobias Funke', 'Tracey Ramos']),
    ((3, 6), ['Charles Morris', 'Emma Wong', 'Eve Holt', 'Tracey Ramos']),
    ((6, 3), ['Charles Morris', 'Emma Wong', 'Eve Holt', 'Tracey Ramos']),
    ((3, 3), ['Emma Wong']),
    (('str', 5), []),
    ((5, 'str'), []),
    (((5, 7, 6), 'str'), []),
    ((5, [5, 7, 6]), []),
    ((-5, 7), []),
    ((5, -7), []),

])
def test_get_customers_function(input_data, expected_result):
    assert get_customers(input_data[0],input_data[1]) == expected_result

def test_get_customers_function_no_arguments():
    assert get_customers() == []