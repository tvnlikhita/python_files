import pytest

def sub(a, b):
    return a - b

@pytest.mark.parametrize("a, b, expected", [
    (30, 20, 10), (80, 50, 30),
    (160, 120, 40), (110, 87, 23),
    (172, 160, 12), (278, 91, 187),
    (40, 26, 14), (475, 348, 127)
])
def test_sub(a, b, expected):
    assert sub(a,b) == expected
