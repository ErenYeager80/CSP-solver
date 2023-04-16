from CSP.Constraint import Constraint
from CSP.Variable import Variable


class Problem:

    def __init__(self, constraints: list[Constraint], variables: list[Variable], name=""):
        self.constraints = constraints
        self.variables = variables
        self.name = name

    def get_unassigned_variables(self) -> list[Variable]:
        return [x for x in self.variables if not x.has_value]

    def print_assignments(self):
        for variable in self.variables:
            print(f"{variable.name} is set to {variable.value}")
