

class Problem(object):
    def __init__(self, initial=None, goal=None, **kwds):
        self.__dict__.update(initial=initial, goal=goal, **kwds)

    def actions(self, state):
        raise NotImplementedError

    def result(self, state, action):
        raise NotImplementedError

    def is_goal(self, state):
        return state == self.goal

    def action_cost(self, s, action, s1):
        return 1

    def h(self, node):
        return 0


class RouteProblem(Problem):
    def actions(self, state):
        return self.map.neighbours[state]

    def result(self, state, action):
        return action if action in self.map.neighbours[state] else state

    def action_cost(self, s, action, s1):
        return self.map.distance[s, s1]
