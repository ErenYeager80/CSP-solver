from CSP.Constraint import Constraint
from CSP.Variable import Variable


class MyConstraint(Constraint):

    def is_satisfied(self) -> bool:
        return all([x.value < 5 for x in self.variables])


a = Variable[int]([1, 2, 3, 4])
b = Variable[int]([1, -2, 3, 4])
c = Variable[int]([1, 9, 3, 4])
d = Variable[int]([1, 9, -3, 4])

a.value = 2
b.value = 4

c1 = MyConstraint([a, b])
print(c1.is_satisfied())
