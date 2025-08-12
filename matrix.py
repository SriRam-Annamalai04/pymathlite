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
