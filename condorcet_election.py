from collections import defaultdict, deque

def detect_cycle(n, graph):
    """Returns True if there's a cycle in the graph."""
    visited = [0] * (n + 1)  # 0 = unvisited, 1 = visiting, 2 = visited

    def dfs(node):
        if visited[node] == 1:  # Found cycle
            return True
        if visited[node] == 2:  # Already processed
            return False
        
        visited[node] = 1
        for neighbor in graph[node]:
            if dfs(neighbor):
                return True
        visited[node] = 2
        return False

    for i in range(1, n + 1):
        if visited[i] == 0 and dfs(i):
            return True
    return False

def topological_sort(n, edges):
    """Returns a valid topological order or None if cycle exists."""
    in_degree = {i: 0 for i in range(1, n + 1)}
    graph = defaultdict(list)

    for a, b in edges:
        graph[a].append(b)
        in_degree[b] += 1

    if detect_cycle(n, graph):
        return None  # Cycle detected

    queue = deque([node for node in in_degree if in_degree[node] == 0])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return order if len(order) == n else None

def construct_votes(n, m, constraints):
    order = topological_sort(n, constraints)
    if not order:
        return "NO"

    # Generate enough votes to satisfy the "more than half" rule
    votes = []
    num_votes = n * 2  # Ensure majority
    for _ in range(num_votes):
        votes.append(order[:])  # Duplicate the valid order

    output = ["YES", str(num_votes)]
    for vote in votes:
        output.append(" ".join(map(str, vote)))

    return "\n".join(output)

# Read input
def main():
    n, m = map(int, input().split())
    constraints = [tuple(map(int, input().split())) for _ in range(m)]
    print(construct_votes(n, m, constraints))

if __name__ == "__main__":
    main()
