import pytest

@pytest.fixture(scope="module") # The Scope Makes The Grades Test Simplier
def grades():
    # Fixture Docstring / Message On pytest --fixtures
    '''Gives the grades'''

    # Fixture Logic Implementatio
    print("\n\t=> Sending grades")
    yield (9.9, 10.0, 2.0, 5.0, 7.0)
    print("\n\t=> Grades used")

@pytest.fixture
def average_1(grades):
    '''
    Gives the average by dividing the sum of
    the grades and dividing it by the number
    of grades
    '''
    return sum(grades) / len(grades)

@pytest.fixture
def average_2(grades):
    '''
    Gives the average by the summing grades
    divided by the total number of grades
    '''

    avg = 0
    for g in grades:
        avg += g / len(grades)
    return avg


def test_has_grades(grades):
    assert len(grades) > 0

def test_grades_rage(grades):
    grades_inrange = tuple([i for i in grades if i >= 0 and i <= 10])
    assert grades_inrange == grades


def test_different_avarages(average_1, average_2):
    assert average_1 == average_2
