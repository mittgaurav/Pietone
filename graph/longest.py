edges = [
    (0, 1),
    (0, 2),
    (1, 3),
    (1, 4),
    (2, 4),
    (3, 5),
    (4, 5),
]

from collections import defaultdict
nodes = defaultdict(list)

for s, e in edges:
    nodes[s].append(e)

def sol(nodes):
    elders = set(nodes.keys())
    for s, e in edges:
        elders.discard(e)

    if not elders:
        return 0

    max_count = 0
    for n in elders:
        this_visited = set()
        count = dfs(n, nodes, this_visited)
        max_count = max(max_count, count)
    return max_count


def dfs(n, nodes, this_visited):
    if n in this_visited:
        return 0
    this_visited.add(n)

    max_count = 0
    # for each neighbour dfs to find the path from them.
    for neighbour in nodes[n]:
        count = dfs(neighbour, nodes, this_visited)
        max_count = max(count, max_count)
    # then add the current node to the len of the path.
    return 1 + max_count


test_cases = [
    {
        "edges": [(0, 1), (1, 2), (2, 3)],
        "expected": 4,
        "description": "Simple Directed Acyclic Graph (DAG)"
    },
    {
        "edges": [(0, 1), (0, 2), (1, 3), (2, 4), (3, 5), (4, 5)],
        "expected": 4,
        "description": "Graph with Multiple Elders and a Longer Path"
    },
    # {
    #     "edges": [(0, 1), (1, 2), (2, 0), (2, 3)],
    #     "expected": 3,
    #     "description": "Graph with a Cycle"
    # },
    {
        "edges": [(0, 1), (1, 2), (3, 4), (4, 5)],
        "expected": 3,
        "description": "Disconnected Graph (Multiple Components)"
    },
    # {
    #     "edges": [(0, 0)],
    #     "expected": 1,
    #     "description": "Graph with No Edges (Single Node)"
    # },
    {
        "edges": [(0, 1), (1, 2), (2, 3), (3, 4), (4, 2), (5, 6), (6, 7)],
        "expected": 5,
        "description": "Graph with Multiple Paths and Cycles"
    },
    {
        "edges": [(0, 1), (1, 2), (2, 3)],
        "expected": 4,
        "description": "Graph with No Elders (All Nodes Have Parents)"
    },
]

# Run the test cases
for i, test_case in enumerate(test_cases):
    edges = test_case["edges"]
    expected = test_case["expected"]
    description = test_case["description"]

    # Build the graph
    nodes = defaultdict(list)
    for s, e in edges:
        nodes[s].append(e)

    # Run the solution and print the result
    result = sol(nodes)

    # Check the result and print test outcome
    print(f"Test Case {i + 1}: {description}")
    print(f"Expected: {expected}, Got: {result}")
    print("Pass" if result == expected else "Fail")
    print("-" * 40)
