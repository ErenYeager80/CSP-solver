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
n = 3
domain = list(range(1, 3 * n * (n - 1)))
a = Variable("a", domain)
b = Variable("b", domain)
c = Variable("c", domain)
print(a, b, c)

variables = [a, b, c]
constraint = MagicHexagonConstraint(variables, 38)
print(constraint.is_satisfied())
a.value = 10
b.value = 12
c.value = 16

print(constraint.is_satisfied())