import random

from CSP.Problem import Problem
from CSP.Variable import Variable
from SecretSanta.SecretSantaConstraint import NotEqualConstraint


class SecretSantaProblem(Problem):
    def __init__(self, participants):
        super().__init__([], participants)
        self.participants = participants
        self.constraints = [NotEqualConstraint(p1, p2) for p1 in participants for p2 in participants if p1 != p2]

    def assign_givers_and_receivers(self):
        # Shuffle participants to avoid deterministic solutions
        random.shuffle(self.participants)

        # Assign givers and receivers
        for i in range(len(self.participants)):
            self.participants[i].value = i
            self.participants[i].receiver = self.participants[(i+1) % len(self.participants)]

    def print_assignments(self):
        for participant in self.participants:
            print(f"{participant.name} will give a gift to {participant.receiver.name}")


class Participant(Variable):
    def __init__(self, name):
        super().__init__(name, [])
        self.name = name
        self.receiver = None

    def __str__(self):
        return f"{self.name} ({self.value})"