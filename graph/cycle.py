def dfs(node, graph, this_visited):
    if node in this_visited:
        return True

    this_visited.add(node)

    # cycle if any node is seen again in this component
    return any(dfs(n, graph, this_visited) for n in graph[node])


def detect_cycle(graph):
    visited = set()

    for node in graph.keys():
        if node in visited:
            continue
        visited.add(node)

        # this will be executed once for each connected component
        this_visited = set()
        if dfs(node, graph, this_visited):
            return True

        visited.update(this_visited)

    return False


if __name__ == "__main__":
    test_cases = [
        # Test case 1: Simple Cycle
        ({0: [1], 1: [2], 2: [0]}, True),  # Expected: True (Cycle found)

        # Test case 2: Simple Tree (No Cycle)
        ({0: [1], 1: [2], 2: []}, False),  # Expected: False (No cycle)

        # Test case 3: Single Node (No Cycle)
        ({0: []}, False),  # Expected: False (No cycle)

        # Test case 4: Disconnected Graph (No Cycle)
        ({0: [1], 1: [], 2: [3], 3: []}, False),  # Expected: False (No cycle)

        # Test case 5: Self Loop (Cycle)
        ({0: [0]}, True),  # Expected: True (Cycle found)

        # Test case 6: Graph with Multiple Components (One Cycle)
        ({0: [1], 1: [2], 2: [0], 3: [4], 4: [5], 5: []}, True),  # Expected: True (Cycle found)

        # Test case 7: Complete Directed Graph (Cycle Exists)
        ({0: [1], 1: [2], 2: [0]}, True),  # Expected: True (Cycle found)

        # Test case 8: Single Edge Graph (No Cycle)
        ({0: [1], 1: []}, False),  # Expected: False (No cycle)

        # Test case 9: Two Cycles (One Independent, One Connecting)
        ({0: [1], 1: [2], 2: [0], 3: [4], 4: [5], 5: [3]}, True),  # Expected: True (Cycle found)

        # Test case 10: Bipartite Graph (No Cycle)
        ({0: [1], 1: [2], 2: [3], 3: []}, False),  # Expected: False (No cycle)

        # Test case 11: Large Graph with a Cycle
        ({0: [1], 1: [2], 2: [3], 3: [4], 4: [5], 5: [2]}, True), # Expected: True (Cycle found)

        # Test case 1: Simple Cycle (0 -> 1 -> 2 -> 0)
        ({0: [1], 1: [2], 2: [0]}, True),

        # Test case 2: No Cycle (Simple Tree)
        ({0: [1], 1: [2], 2: [3], 3: []}, False),

        # Test case 3: Multiple Components (Cycle in 0-1-2 and no cycle in 3-4-5)
        ({0: [1], 1: [2], 2: [0], 3: [4], 4: [5], 5: []}, True),

        # Test case 4: Large Graph with Multiple Cycles (0 -> 1 -> 2 -> 0 and 3 -> 4 -> 5 -> 3)
        ({0: [1], 1: [2], 2: [0], 3: [4], 4: [5], 5: [3]}, True),

        # Test case 5: Self-loop (Cycle: 0 -> 0)
        ({0: [0]}, True),

        # Test case 7: Disconnected Graph with No Cycle
        ({0: [1], 1: [], 2: [3], 3: []}, False),

        # Test case 9: Fully Connected Graph (Cycle exists)
        ({0: [1, 2, 3], 1: [0, 2, 3], 2: [0, 1, 3], 3: [0, 1, 2]}, True),

        # Test case 21: Directed graph with back edges creating multiple cycles
        ({0: [1], 1: [2], 2: [3], 3: [0], 4: [5], 5: [6], 6: [4]}, True),  # Expected: True (Cycle found)

        # Test case 22: Directed graph where cycle is in a subcomponent
        ({0: [1], 1: [2], 2: [3], 3: [0], 4: [5], 5: [6], 6: [7], 7: [4]}, True),  # Expected: True (Cycle in subcomponent)
    ]

    # Loop through test cases
    for idx, (graph, expected) in enumerate(test_cases):
        result = detect_cycle(graph)
        try:
            assert result == expected
            print(f"Test case {idx + 1}: Passed")
        except AssertionError:
            print(f"Test case {idx + 1}: Failed (Expected {expected}, Got {result})")
