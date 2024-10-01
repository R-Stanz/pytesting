from uri1973 import star_trek
import pytest

def test_case_1():
    visits = 8
    sheeps_left = 68

    family_size = 8
    sheeps_by_farm = [1, 3, 5, 7, 11, 13, 17, 19]

    assert (visits, sheeps_left) == star_trek(family_size, sheeps_by_farm)

def test_case_2():
    visits = 7
    sheeps_left = 63

    family_size = 8
    sheeps_by_farm = [1, 3, 5, 7, 11, 13, 16, 19]

    assert (visits, sheeps_left) == star_trek(family_size, sheeps_by_farm)

@pytest.mark.xfail
def test_case_3():
    visits = 1
    sheeps_left = 1

    family_size = 1
    sheeps_by_farm = [1]

    assert (visits, sheeps_left) == star_trek(family_size, sheeps_by_farm)
