import heapq
from trees import *
from utils import PriorityQueue


def g(n):
    return n.path_cost

def best_search(problem, f):
    node = Node(problem.initial)
    fringe = PriorityQueue([node], key=f)
    visited = {problem.initial: node}

    while fringe:
        node = fringe.pop()
        if problem.is_goal(node.state):
            return node

        for child in expand(problem, node):
            s = child.state
            if s not in visited:
                visited[s] = child
                fringe.add(child)

    return failure

def uniform_cost_search(problem):
    return best_search(problem, f=g)

def greedy(problem, h = None):
    h = h or problem.h
    return best_search(problem, f=h)

def a_star(problem, h = None):
    h = h or problem.h
    return best_search(problem, f=lambda n: g(n) + h(n))