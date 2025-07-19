import math

from trees import Node, expand, failure
from collections import deque


def breath_first_search(problem):
    node = Node(problem.initial)
    if node.is_goal(problem.initial):
        return node
    
    queue = deque([node])
    visited = {problem.initial}

    while queue:
        node = queue.pop()

        for child in expand(problem, node):
            s = child.state
            if problem.is_goal(s):
                return child
            
            if s not in visited:
                visited.add(s)
                queue.append(child)
    
    return failure


def depth_first_search(problem, initial):
    pass




# UCS: g(n)
# Greedy: h(n)
# A*: f(n) = g(n) + h(n)

def best_search(problem, f):
    node = Node(problem.initial)
    fringe = [node]   # PriorityQueue
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

