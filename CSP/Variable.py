from typing import Generic, TypeVar, List

T = TypeVar('T')


class Variable(Generic[T]):
    _value: T = None

    def __init__(self, domain: List[T]):
        self._domain = domain

    @property
    def value(self) -> T:
        return self._value

    @value.setter
    def value(self, x: T):
        if x in self._domain:
            self._value = x
            self._domain.remove(x)

    @property
    def domain(self) -> List[T]:
        return self._domain
