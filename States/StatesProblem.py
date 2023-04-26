import random
from typing import List

from CSP.Problem import Problem
from CSP.Variable import Variable
from States.StatesConstraint import StatesNotSameConstraint


class StatesProblem(Problem):

    def __init__(self):
        super().__init__([], [], "States Problem")

        wa = Variable[str](['R', 'G', 'B'], 'WA')
        nt = Variable[str](['R', 'G', 'B'], 'NT')
        sa = Variable[str](['R', 'G', 'B'], 'SA')
        q = Variable[str](['R', 'G', 'B'], 'Q')
        nsw = Variable[str](['R', 'G', 'B'], 'NSW')
        v = Variable[str](['R', 'G', 'B'], 'V')
        t = Variable[str](['R', 'G', 'B'], 'T')

        c1 = StatesNotSameConstraint([wa, nt])
        c2 = StatesNotSameConstraint([wa, sa, nt])
        c3 = StatesNotSameConstraint([sa, nt, q])
        c4 = StatesNotSameConstraint([v, nsw, sa])

        self.constraints = [c1, c2, c3, c4]
        self.variables = [wa, nt, sa, q, nsw, v, t]



