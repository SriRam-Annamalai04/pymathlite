# pymathlite

A tiny `Matrix` class for learning and demos.

```python
from pymathlite import Matrix

a = Matrix([[1,2],[3,4]])
b = Matrix([[5,6],[7,8]])
print(a + b)  # Matrix([[6, 8], [10, 12]])
```

# 8) Build & install locally
```bash
# from the project root (where pyproject.toml is)
python -m pip install --upgrade pip build
python -m build  # creates dist/*.whl and dist/*.tar.gz

# install locally
pip install -e .
# or install the built wheel:
pip install dist/pymathlite-0.1.0-py3-none-any.whl
```