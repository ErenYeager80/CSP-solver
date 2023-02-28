from typing import List

from CSP.Constraint import Constraint
from CSP.Variable import Variable


class Problem:
    def __int__(self, constraints: list[Constraint], variables: List[Variable]):
        self.constraints = constraints
        self.variables = variables
