import random
graph = {
    'A': ['B','C','U'],
    'B': ['E','G'],
    'C': ['G','I','J'],
    'U': ['K','Y'],
    'E': ['G','M'],
    'G': ['M'],
    'I': ['M'],
    'J': ['K'],
    'K': ['J'],
    'Y': ['M'],
    'M': [],
}

h_values = {
    'A': 7,
    'B': 5,
    'C': 3,
    'U': 4,
    'E': 2,
    'G': 3,
    'I': 6,
    'J': 2,
    'K': 1,
    'Y': 2,
    'M': 0,
}


def hillclimb(graph, h_values,start,end):
    current = start
    visited = [start]


    while current != end:
        neighbor = graph[current]
        nextEval = float('inf')
        nextNode = None

        for x in neighbor:
            if h_values[x] < nextEval:
                nextNode = x
                nextEval = h_values[x]

        if neighbor == end:
            visited.append(nextNode)
            return "Reached goal",visited

        if h_values[nextNode] < h_values[current]:
            current = nextNode
            visited.append(current)
        else:
            return "Did not reach goal.", visited

    return "Reached goal", visited

print(hillclimb(graph, h_values, 'A', 'M'))



