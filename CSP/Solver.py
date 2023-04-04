from CSP.Problem import Problem
from CSP.Variable import Variable


class Solver:
    use_mrv = True
    use_lcv = False

    def __init__(self, problem: Problem):
        self.problem = problem

    def is_finished(self) -> bool:
        return all([x.is_satisfied() for x in self.problem.constraints]) and \
            len(self.problem.get_unassigned_variables()) == 0

    def solve(self):
        self.backtracking()
        if self.is_finished():
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
                    return result
                var.value = None

        return False

    def select_unassigned_variable(self) -> Variable:
        if self.use_mrv:
            return self.mrv()
        return self.problem.get_unassigned_variables()[0] if self.problem.get_unassigned_variables() else None

    def order_domain_values(self, var):
        if self.use_lcv:
            return self.lcv(var)
        return var.domain

    def mrv(self):
        min_var = None
        min_domain_size = float('inf')
        for var in self.problem.get_unassigned_variables():
            if len(var.domain) < min_domain_size:
                min_var = var
                min_domain_size = len(var.domain)
        return min_var

    def is_consistent(self, var):
        list_of_values = [x.is_satisfied() for x in self.problem.constraints if var in x.variables]
        return all(list_of_values)
