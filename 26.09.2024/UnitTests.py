import pytest
import unittest

from Functions import calculateReachedPercentage, getGradeFromPercentage

@pytest.mark.parametrize(
    "reached_points, possible_points, expected",
    [
        (50, 100, 50.0),
        (75, 100, 75.0),
        (90, 90, 100.0),
        (0, 100, 0.0),
        (25, 50, 50.0),
    ]
)
def test_calculateReachedPercentage(reached_points, possible_points, expected):
    result = calculateReachedPercentage(reached_points, possible_points)

    assert result == expected


@pytest.mark.parametrize(
    "reached_points, possible_points, expected_exception",
    [
        (-1, 100, ValueError),
        (50, -1, ValueError),
        ("fifty", 100, TypeError),
        (50, "one hundred", TypeError),
        (50, 0, ValueError),
        (50, 101, ValueError),
        (101, 100, ValueError)
    ]
)
def test_calculateReachedPercentage_exceptions(reached_points, possible_points, expected_exception):
    with pytest.raises(expected_exception):
        calculateReachedPercentage(reached_points, possible_points)

@pytest.mark.parametrize("percentage, expected_grade", [
    (100, 'sehr gut'),
    (92, 'sehr gut'),
    (91, 'gut'),
    (81, 'gut'),
    (80, 'befriedigend'),
    (67, 'befriedigend'),
    (66, 'ausreichend'),
    (50, 'ausreichend'),
    (49, 'mangelhaft'),
    (30, 'mangelhaft'),
    (29, 'ungenügend'),
    (0, 'ungenügend'),
])
def test_valid_percentage(percentage, expected_grade):
    assert getGradeFromPercentage(percentage) == expected_grade

@pytest.mark.parametrize("invalid_percentage", [-1, 101])
def test_invalid_percentage(invalid_percentage):
    with pytest.raises(ValueError):
        getGradeFromPercentage(invalid_percentage)

@pytest.mark.parametrize("invalid_type", ['text'])
def test_invalid_type(invalid_type):
    with pytest.raises(TypeError):
        getGradeFromPercentage(invalid_type)

if __name__ == '__main__':
    pytest.main()

