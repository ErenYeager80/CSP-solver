"""
Base solver class that implements the solve method and solves the problem using the backtracking, forward checking,
MRV, and LCV, and AC3 algorithms.
"""
from CSP.Problem import Problem
from CSP.Solver import Solver


class BaseSolver(Solver):
    def __init__(self, use_forward_checking: bool = True, use_mrv: bool = True,
                 use_lcv: bool = True, use_forward_check: bool = True):
        self.use_forward_checking = use_forward_checking
        self.use_mrv = use_mrv
        self.use_lcv = use_lcv
        self.use_ac3 = use_forward_check

    def solve(self, problem: Problem):
        if self.use_ac3:
            self.ac3(problem)
        return self.backtracking_search(problem)

    def backtracking_search(self, problem: Problem):
        return self.backtracking({}, problem)

    def backtracking(self, assignment, problem: Problem):
        if self.is_complete(assignment, problem):
            return assignment
        var = self.select_unassigned_variable(assignment, problem)
        for value in self.order_domain_values(var, assignment, problem):
            if self.is_consistent(var, value, assignment, problem):
                assignment[var] = value
                result = self.backtracking(assignment, problem)
                if result is not None:
                    return result
                del assignment[var]
        return None

    def is_complete(self, assignment, problem: Problem):
        return len(assignment) == len(problem.variables)

    def select_unassigned_variable(self, assignment, problem: Problem):
        if self.use_mrv:
            return self.mrv(assignment, problem)
        return self.first_unassigned_variable(assignment, problem)

    def first_unassigned_variable(self, assignment, problem: Problem):
        for var in problem.variables:
            if var not in assignment:
                return var
        return None

    def mrv(self, assignment, problem: Problem):
        min_var = None
        min_domain_size = float('inf')
        for var in problem.variables:
            if var not in assignment:
                if len(var.domain) < min_domain_size:
                    min_var = var
                    min_domain_size = len(var.domain)
        return min_var

    def order_domain_values(self, var, assignment, problem: Problem):
        if self.use_lcv:
            return self.lcv(var, assignment, problem)
        return var.domain

    def lcv(self, var, assignment, problem: Problem):
        return sorted(var.domain, key=lambda value: self.count_conflicts(var, value, assignment, problem))

    def count_conflicts(self, var, value, assignment, problem: Problem):
        count = 0
        for constraint in problem.constraints:
            if var in constraint.variables:
                for other_var in constraint.variables:
                    if other_var != var and other_var not in assignment:
                        if value in other_var.domain:
                            count += 1
        return count

    def is_consistent(self, var, value, assignment, problem: Problem):
        for constraint in problem.constraints:
            if var in constraint.variables:
                if not constraint.is_satisfied(assignment):
                    return False
        return True

    def ac3(self, problem: Problem):
        queue = []
        for constraint in problem.constraints:
            for var in constraint.variables:
                for other_var in constraint.variables:
                    if var != other_var:
                        queue.append((var, other_var))
        while queue:
            (var, other_var) = queue.pop(0)
            if self.revise(var, other_var, problem):
                if len(var.domain) == 0:
                    return False
                for constraint in problem.constraints:
                    if var in constraint.variables:
                        for other_var in constraint.variables:
                            if var != other_var:
                                queue.append((other_var, var))
        return True

    def revise(self, var, other_var, problem: Problem):
        revised = False
        for value in var.domain:
            if not self.has_support(value, other_var, problem):
                var.domain.remove(value)
                revised = True
        return revised

    def has_support(self, value, other_var, problem: Problem):

        for constraint in problem.constraints:
            if other_var in constraint.variables:
                if not constraint.is_satisfied({other_var: value}):
                    return False
        return True
