from typing import Optional

from CSP.Problem import Problem
from CSP.Variable import Variable


class Solver:
    use_mrv = True
    use_lcv = True

    def __init__(self, problem: Problem):
        self.problem = problem

    def is_finished(self) -> bool:
        return all([x.is_satisfied() for x in self.problem.constraints]) and len(
            self.problem.get_unassigned_variables()) == 0

    def solve(self):
        result = self.backtracking()
        if result:
            print('Solved')
        else:
            print('Not solved')


    def backtracking(self):
        if len(self.problem.get_unassigned_variables()) == 0:
            return True

        var = self.select_unassigned_variable()
        for value in self.order_domain_values(var):

            var.value = value
            if self.is_consistent(var):
                result = self.backtracking()
                if result:
                    return True
            var.value = None

        return False

    def select_unassigned_variable(self) -> Optional[Variable]:
        if self.use_mrv:
            return self.mrv()
        unassigned_variables = self.problem.get_unassigned_variables()
        return unassigned_variables[0] if unassigned_variables else None

    def order_domain_values(self, var: Variable):
        if self.use_lcv:
            return self.lcv(var)
        return var.domain

    def mrv(self) -> Optional[Variable]:
        unassigned_variables = self.problem.get_unassigned_variables()
        if not unassigned_variables:
            return None

        min_var = min(unassigned_variables, key=lambda var: len(var.domain))
        return min_var

    def is_consistent(self, var: Variable):
        for constraint in self.problem.constraints:
            if var in constraint.variables and not constraint.is_satisfied():
                return False
        return True

    def lcv(self, var: Variable):
        return sorted(var.domain, key=lambda val: self.problem.count_conflicts(var, val))
