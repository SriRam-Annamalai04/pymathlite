from pymathlite import Matrix
import pytest


def test_column_mismatch_raises():
    with pytest.raises(ValueError):
        Matrix([[1, 2], [1, 2, 3]])


def test_type_error_raises():
    with pytest.raises(TypeError):
        Matrix([1, [1, 2, 3]])
    with pytest.raises(TypeError):
        Matrix(1)


def test_addition():
    a = Matrix([[1, 2], [3, 4]])
    b = Matrix([[5, 6], [7, 8]])
    c = a + b
    assert c.__repr__() == "Matrix([[6, 8], [10, 12]])"


def test_sum_works_with_radd():
    a = Matrix([[1, 1]])
    b = Matrix([[2, 2]])
    c = Matrix([[3, 3]])
    s = sum([a, b, c])
    assert s.__repr__() == "Matrix([[6, 6]])"


def test_shape_mismatch_raises():
    a = Matrix([[1, 2]])
    b = Matrix([[1, 2, 3]])
    with pytest.raises(ValueError):
        _ = a + b
