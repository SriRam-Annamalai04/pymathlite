# pymathlite

[![tests](https://github.com/SriRam-Annamalai04/pymathlite/actions/workflows/tests.yml/badge.svg)](https://github.com/SriRam-Annamalai04/pymathlite/actions/workflows/tests.yml)

A tiny, dependency-free `Matrix` class for learning and demos. It validates shape on
construction and on arithmetic, so mistakes fail fast with a clear error.

```python
from pymathlite import Matrix

a = Matrix([[1, 2], [3, 4]])
b = Matrix([[5, 6], [7, 8]])
print(a + b)                 # Matrix([[6, 8], [10, 12]])
print(sum([a, b]))           # works with built-in sum()
print(Matrix.zeros(2, 3))    # Matrix([[0, 0, 0], [0, 0, 0]])

Matrix([[1, 2], [3]])        # ValueError: All rows must have the same length
a + Matrix([[1, 2, 3]])      # ValueError: shape mismatch: 2x2 vs 1x3
```

## Install

```bash
git clone https://github.com/SriRam-Annamalai04/pymathlite.git
cd pymathlite
pip install -e ".[test]"
```

## Test and build

```bash
pytest -q          # run the test suite
python -m build    # build the wheel and sdist into dist/
```

CI runs the tests and the build on Python 3.9, 3.11 and 3.13 for every push and pull request.

## License

MIT, see [LICENSE](LICENSE).
