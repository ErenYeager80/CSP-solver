from CSP.Constraint import Constraint
from CSP.Problem import Problem
from CSP.Solver import Solver
from CSP.Variable import Variable


class NotSameConstraint(Constraint):

    def is_satisfied(self) -> bool:
        list_of_values = [x.value for x in self.variables if x.value is not None]
        return len(list_of_values) == len(set(list_of_values))


WA = Variable[str](['R', 'G', 'B'], 'WA')
NT = Variable[str](['R', 'G', 'B'], 'NT')
SA = Variable[str](['R', 'G', 'B'], 'SA')
Q = Variable[str](['R', 'G', 'B'], 'Q')
NSW = Variable[str](['R', 'G', 'B'], 'NSW')
V = Variable[str](['R', 'G', 'B'], 'V')
T = Variable[str](['R', 'G', 'B'], 'T')

c1 = NotSameConstraint([WA, NT])
c2 = NotSameConstraint([WA, SA, NT])
c3 = NotSameConstraint([SA, NT, Q])
c4 = NotSameConstraint([V, NSW, SA])

p = Problem([c1, c2, c3, c4], [WA, NT, SA, Q, NSW, V, T])
s = Solver(p)
s.solve()

print('WA: ', WA.value)
print('NT: ', NT.value)
print('SA: ', SA.value)
print('Q: ', Q.value)
print('NSW: ', NSW.value)
print('V: ', V.value)
print('T: ', T.value)
