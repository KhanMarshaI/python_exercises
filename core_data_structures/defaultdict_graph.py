# Defaultdict Graph
# Implement an undirected graph of internal hosts where each node’s adjacency list is maintained by defaultdict(set). 
# Write add_edge(a, b) and has_path(a, b) using BFS.

from collections import defaultdict, deque

internalHostGraph = defaultdict(set)

def add_edge(a: str, b: str):
    internalHostGraph[a].add(b)
    internalHostGraph[b].add(a)

def has_path(a: str, b: str):
    if a == b:
        return True
    
    visited = []
    queue = deque()

    queue.append(a)

    while queue:
        curr = queue.popleft()
        if curr == b:
            return True
        if curr not in visited:
            visited.append(curr)
            for value in internalHostGraph[curr]:
                if value not in visited:
                    queue.append(value)
    return False


add_edge("10.0.0.1", "10.0.0.2")
add_edge("10.0.0.2", "10.0.0.3")
add_edge("10.0.0.3", "10.0.0.1")

print("Does path exist?",has_path("10.0.0.1", "10.0.0.3"))
