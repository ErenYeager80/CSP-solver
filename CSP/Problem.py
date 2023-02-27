from CSP.Constraint import Constraint


class Problem:

    def __int__(self, constraints: list[Constraint]):
        self.constraints = constraints
