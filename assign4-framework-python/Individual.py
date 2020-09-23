import random


# Author Fan Zhang
class Individual:
    # Updates the fitness value based on the genom and the map.
    def updateFitness(self):
        # TODO implement fitness function
        self.fitness = 0
        for i in range(17):
            if self.color[self.map.borders[i].index1] != self.color[self.map.borders[i].index2]:
                self.fitness += 1

    def __init__(self, map):
        self.map = map  # the map
        self.fitness = 0  # fitness is cached and only updated on request whenever necessary
        # TODO some representation of the genom of the individual
        # TODO implement random generation of an individual
        self.color = [None] * 10
        for i in range(10):
            self.color[i] = random.randint(1, 3)
        self.updateFitness()

    # Reproduces a child randomly from two individuals (see textbook).
    # x The first parent.
    # y The second parent.
    # return The child created from the two individuals.
    def reproduce(self, x, y):
        child = Individual(x.map)
        # TODO reproduce child from individuals x and y
        for i in range(len(x.color)):
            if random.random() < 0.5:
                child.color[i] = x.color[i]
            else:
                child.color[i] = y.color[i]
        child.updateFitness()
        return child

    # Randomly mutates the individual.
    def mutate(self):
        # TODO implement random mutation of the individual
        self.color[random.randint(0, 9)] = random.randint(1, 3)
        self.updateFitness()

    # Checks whether the individual represents a valid goal state.
    # return Whether the individual represents a valid goal state.
    def isGoal(self):
        return self.fitness == len(self.map.borders)

    def printresult(self):
        print("Your result:")
        # TODO implement printing the individual in the following format:
        # fitness: 15
        # North
        # Carolina: 0
        # South Carolina: 2
        # ...
        for i in range(10):
            print(self.map.states[i], ':', self.color[i])
