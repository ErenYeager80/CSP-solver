from collections import deque
from typing import Optional

from CSP.Problem import Problem
from CSP.Variable import Variable


class Solver:

    def __init__(self, problem: Problem, use_mrv=False, use_lcv=False, use_ac3=False):
        self.problem = problem
        self.use_lcv = use_lcv
        self.use_mrv = use_mrv
        self.use_ac3 = use_ac3

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
                # if self.forward_check():
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

    def forward_check(self, var):
        constraints_involved = [x for x in self.problem.constraints if var in x.variables]
        for constraint in constraints_involved:
            for other_var in constraint.variables:
                if other_var is not var:
                    for other_var_candidate in other_var.domain:
                        other_var.value = other_var_candidate
                        if not self.is_consistent(other_var):
                            other_var.domain.remove(other_var_candidate)
                            if len(other_var.domain) <= 0:
                                return False
                        other_var.value = None

        var.value = None
        return True

    def is_consistent(self, var: Variable):
        for constraint in self.problem.constraints:
            if var in constraint.variables and not constraint.is_satisfied():
                return False
        return True

    """
    Least-constraining value heuristic: choose a value that rules
    out the smallest number of values in variables connected to the
    current variable by constraints.
    """

    def lcv(self, var: Variable):
        domain_len = len(var.domain)
        if var.has_value:
            raise Exception("Variable should be unassigned for LCV")
        sorted_domain = sorted(var.domain, key=lambda val: self.count_conflicts(var, val))
        if len(sorted_domain) != domain_len:
            raise Exception("Domain member is missing")
        return sorted_domain

    def count_conflicts(self, var, val):
        constraints_involved = [x for x in self.problem.constraints if var in x.variables]
        conflicts = 0
        var.value = val
        for constraint in constraints_involved:
            for other_var in constraint.variables:
                if other_var is not var and not other_var.has_value:
                    for other_var_candidate in other_var.domain:
                        other_var.value = other_var_candidate
                        if not self.is_consistent(var):
                            conflicts += 1
                        other_var.value = None

        var.value = None
        return conflicts
