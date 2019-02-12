from grades import average
from pytest import approx


def test_average():
    values = {'bob': 85.33, 'sara': 98.0, 'sue': 83.5}
    students = average()
    for name in students:
        assert students[name] == approx(values[name])
