from collections import defaultdict

def getNeighbours(pairs):
    result = defaultdict(list)
    for key, value in pairs:
        result[key].append(value)
    return result


class Map:
    def __init__(self, links=None, locations=None, directed=False):
        if not directed:
            for (v1, v2) in list(links):
                links[v2, v1] = links[v1, v2]

        self.distance = links
        self.neighbours = getNeighbours(links)
        self.links = links
        self.locations = locations