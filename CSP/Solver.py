from abc import ABC, abstractmethod

from CSP.Problem import Problem


class CPSSolver(ABC):
    """
    An abstract class representing a CPS problem solver.
    """

    @abstractmethod
    def solve(self, problem: Problem):
        """
        Solves the given CPS problem and returns the solution.

        Args:
        problem: A CPS problem object.

        Returns:
        The solution to the problem.
        """
        pass
