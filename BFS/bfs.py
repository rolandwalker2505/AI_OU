
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