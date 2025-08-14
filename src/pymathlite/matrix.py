class Matrix:
    def __init__(self, value: list[list[any]]):
        self.value = value
        self._row: int = len(self.value)
        self._column: int = len(self.value[0])

    @property
    def value(self) -> list[list[any]]:
        return self._value

    @value.setter
    def value(self, v: list[list[any]]):
        column = 0
        for i, column_value in enumerate(v):
            if not isinstance(column_value, list):
                raise TypeError(f'{column_value} is not a list')
            if i == 1:
                column = len(column_value)
            elif column != len(column_value):
                raise ValueError("Each Column should have the same length")
        self._value = v

    @property
    def row(self):
        return self._row

    @property
    def column(self):
        return self._column

    def _check_same_shape(self, other: "Matrix"):
        if not isinstance(other, Matrix):
            raise TypeError(f"{other!r} is not a Matrix")
        if self.row != other.row or self.column != other.column:
            raise ValueError(
                f"shape mismatch: {self.row}x{self.column} vs {other.row}x{other.column}"
            )

    def __add__(self, other: "Matrix") -> "Matrix":
        self._check_same_shape(other)
        result = [
            [a + b for a, b in zip(r1, r2)]
            for r1, r2 in zip(self._value, other._value)
        ]
        return Matrix(result)

    def __radd__(self, other):
        if other == 0:
            return self
        return NotImplemented

    @classmethod
    def zeros(cls, row: int, column: int) -> "Matrix":
        return cls([[0 for _ in range(column)] for _ in range(row)])

    def __repr__(self):
        return f"Matrix({self._value!r})"
