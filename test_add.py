import pytest

def add(a, b):
    return a + b

@pytest.mark.parametrize("a, b, expected", [
    (10, 20, 30), (30, 50, 80),
    (40, 120, 160), (23, 87, 110),
    (12, 160, 172), (187, 91, 278),
    (14, 26, 40), (127, 348, 475),
    (56, 46, 102), (101, 87, 188)
])
def test_pysum1(a, b, expected):
    assert add(a,b) == expected
