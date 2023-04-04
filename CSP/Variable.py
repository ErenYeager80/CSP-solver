from typing import Generic, TypeVar, List

T = TypeVar('T')


class Variable(Generic[T]):
    _value: T = None
    _has_value: bool = False

    def __init__(self, domain: List[T],name:str=None):
        self._domain = domain
        self.name = name

    @property
    def value(self) -> T:
        return self._value

    @value.setter
    def value(self, x: T):
        if x in self._domain:
            self._value = x
            # self._domain.remove(x)
            self._has_value = True
        if x is None:
            self._has_value = False

    @property
    def domain(self) -> List[T]:
        return self._domain

    @property
    def has_value(self) -> bool:
        return self._has_value


