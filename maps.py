from collections import defaultdict

def multimap(links):
    result = defaultdict(list)
    for v1, v2 in links:
        result[v1].append(v2)
    return result

class Map:
    def __init__(self, links, locations=None, directed=False):
        # Nếu đồ thị không có hướng
        if not directed:
            for v1, v2 in list(links):
                links[(v2, v1)] = links[(v1, v2)]
            self.distances = links
            self.neighbors = multimap(links)
            self.locations = locations or defaultdict(lambda : (0, 0))