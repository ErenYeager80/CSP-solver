from typing import List

from CSP.Constraint import Constraint
from CSP.Variable import Variable
from MagicHexagon.MagicHexagonConstraint import MagicHexagonConstraint


class MagicHexagonProblem:
    def __init__(self, n: int):
        self.variables = self.get_variables(n)
        self.constraints = self.get_constraints(n)
        # super().__init__(self.get_constraints(n), self.get_variables(n))
        self.n = n

    def get_variables(self, n: int) -> List[Variable]:
        variables = [Variable(i, list(range(1, 3 * n * (n - 1) + 2))) for i in range(1, 3 * n * (n - 1) + 2)]
        return variables

    def get_constraints(self, n: int) -> List[Constraint]:
        constraints = []
        magic_sum = n * (3 * n * n + 3 * n + 1) // 2
        for i in range(1, n + 1):
            # Row constraints
            row = [j for j in range(3 * n * (i - 1) + 2, 3 * n * i + 1)]
            constraints.append(MagicHexagonConstraint([self.variables[j - 1] for j in row], magic_sum))
            # Column constraints
            col = [j for j in range(i, 3 * n * (n - 1) + i + 1, 3)]
            constraints.append(MagicHexagonConstraint([self.variables[j - 1] for j in col], magic_sum))
            # Diagonal constraints
            if i < n:
                diag_left = [j for j in [3 * n * (i - 1) + 1 + i, 3 * n * i + i]]
                diag_right = [j for j in [3 * n * (i - 1) + 1 + 2 * n - i, 3 * n * i + 2 * n - i + 1]]
                constraints.append(MagicHexagonConstraint([self.variables[j - 1] for j in diag_left], magic_sum))
                constraints.append(MagicHexagonConstraint([self.variables[j - 1] for j in diag_right], magic_sum))
        return constraints

    def draw(self):
        for i in range(1, self.n + 1):
            row = [f"v{j}" for j in range(3 * self.n * (i - 1) + 2, 3 * self.n * i + 1)]
            spaces = " " * (2 * (self.n - i))
            print(spaces + "  ".join(
                [str(self.variables[j - 1].value) if self.variables[j - 1].value is not None else "*" for j in row]))
        for i in range(self.n + 1, 2 * self.n + 1):
            row = [f"v{j}" for j in range(3 * self.n * (i - 1) + 2, 3 * self.n * i + 1)]
            spaces = " " * (2 * (i - self.n - 1))
            print(spaces + "  ".join(
                [str(self.variables[j - 1].value) if self.variables[j - 1].value is not None else "*" for j in row]))
