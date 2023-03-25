from CSP.Variable import Variable
from MagicHexagon.MagicHexagonConstraint import MagicHexagonConstraint

# class MyConstraint(Constraint):
#     def is_satisfied(self) -> bool:
#         return all([x.value < 5 for x in self.variables])
#
#
# a = Variable[int]([1, 2, 3, 4])
# b = Variable[int]([1, -2, 3, 4])
# c = Variable[int]([1, 9, 3, 4])
# d = Variable[int]([1, 9, -3, 4])
#
# a.value = 2
# b.value = 4
#
# c1 = MyConstraint([a, b])
# print(c1.is_satisfied())
from SecretSanta.SecretSantaProblem import SecretSantaProblem, Participant
from Solver.BaseSolver import BaseSolver
from Sudoku.SudokuProblem import SudokuProblem

# Example usage
participants = [Participant("Alice"), Participant("Bob"), Participant("Charlie"), Participant("David")]
problem = SecretSantaProblem(participants)
problem.assign_givers_and_receivers()
problem.print_assignments()

grid = [
    [0, 0, 3, 0, 2, 0, 6, 0, 0],
    [9, 0, 0, 3, 0, 5, 0, 0, 1],
    [0, 0, 1, 8, 0, 6, 4, 0, 0],
    [0, 0, 8, 1, 0, 2, 9, 0, 0],
    [7, 0, 0, 0, 0, 0, 0, 0, 8],
    [0, 0, 6, 7, 0, 8, 2, 0, 0],
    [0, 0, 2, 6, 0, 9, 5, 0, 0],
    [8, 0, 0, 2, 0, 3, 0, 0, 9],
    [0, 0, 5, 0, 1, 0, 3, 0, 0]
]

problem = SudokuProblem(grid)

solver = BaseSolver(use_ac3=False, use_forward_checking=False, use_mrv=False, use_lcv=False)

solver.solve(problem)

print(problem)
