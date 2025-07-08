import math
from collections import deque
from problems import RouteProblem
from trees import Node

# def breadth_first_search(problem: RouteProblem):
#     q = deque()
#     result = []
#     q.append(problem.initial)

#     while q:
#         if problem.goal in result:
#             return result
#         v = q.popleft()
#         if v not in result:
#             result.append(v)
#         for x in problem.actions(v):
#             if x not in result:
#                 q.append(x)

#     return result


def breadth_first_search(problem: RouteProblem):
    node = Node(problem.initial)
    # if problem
