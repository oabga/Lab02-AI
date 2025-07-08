from problems import RouteProblem

result = []
def dfs_search(problem: RouteProblem, stack=[], s=None):
    if problem.goal in result:
        return result
    if problem.initial not in result:
        s = problem.initial
        stack.append(s)
    elif s not in result:
        stack.append(s)

    v = stack.pop()
    result.append(v)

    for x in problem.actions(v):
        if x not in result:
            dfs_search(problem, stack,x)

    return result
    