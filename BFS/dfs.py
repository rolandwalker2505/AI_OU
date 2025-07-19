from trees import *

def depth_first_search(problem, node=None):
    node = Node(problem.initial)
    fringe = [node]
    visited = set()

    while fringe:
        node = fringe.pop()
        if problem.is_goal(node.state):
            return node

        visited.add(node.state)

        fringe.extend(child for child in expand(problem, node)
            if child.state not in visited and child not in fringe
        )

    return None