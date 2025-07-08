import math
from BFS.problems import RouteProblem
from maps import Map
from collections import deque

def breadth_first_search(problem):
    queue = deque()
    visited = {}
    queue.append(problem.initial)
    visited[problem.initial] = None
    while queue is not None:
        temp = queue.popleft()

        if problem.is_goal(temp):
            path = []
            while temp is not None:
                path.append(temp)
                temp = visited[temp]
            return path[::-1]


        for action in problem.actions(temp):
            if action not in visited:
                visited[action] = temp
                queue.append(action)

    return


# if __name__ == "__main__":
#     romania = Map(links={('O', 'Z'): 71, ('O', 'S'): 151, ('A', 'Z'): 75, ('A', 'S'): 140, ('A', 'T'): 118},
#                   locations={'A': (76, 497), 'O': (117, 580), 'S': (187, 463), 'T': (83, 414), 'Z': (92, 539)})
#     my_route = RouteProblem('O', 'T', map=romania)
#     print(breadth_first_search(my_route))
