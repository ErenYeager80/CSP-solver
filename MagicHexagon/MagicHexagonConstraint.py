from typing import List

from CSP.Constraint import Constraint
from CSP.Variable import Variable


class MagicHexagonConstraint(Constraint):
    def __init__(self, variables: List[Variable], magic_sum: int):
        super().__init__(variables)
        self.magic_sum = magic_sum

    def is_satisfied(self) -> bool:
        values = [v.value for v in self.variables if v.value is not None]
        if len(values) != len(set(values)):
            return False
        if None in values:
            return True
        return sum(values) == self.magic_sum
