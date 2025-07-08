from problems import RouteProblem
from queue import PriorityQueue

def ucs_search(problem: RouteProblem):
    result = []
    q = PriorityQueue()
    q.put((0, problem.initial))
    while q:
        v = q.get()[1]
        result.append(v)
        for x in problem.action_cost(v):
            if x not in result:
                q.put((problem.action_cost(v, '', x)))
    return result
