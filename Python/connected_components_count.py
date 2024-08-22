def connected_components_count(graph: dict) -> int:
    """
    This function calculates the number of connected components in a given graph.

    Args:
        graph (dict): A dictionary representing the graph, which is represented as an adjacency list.

    Returns:
        int: The number of connected components in the graph.
    """
    counter = 0
    visited = set()
    for i in graph:
        if not has_path(graph, i, visited):
            counter += 1
    return counter


def has_path(graph: dict, node: int, visited: set) -> bool:
    """
    Checks if a path exists between a source node and any other node in a graph.

    Args:
        graph (dict): A dictionary representing the graph, which is represented as an adjacency list.
        node (int): The source node.
        visited (set): A set of visited nodes.

    Returns:
        bool: True if a path exists from the source node to any other node, False otherwise.
    """
    if node in visited:
        return True

    if len(graph[node]) == 0:
        visited.add(node)
    else:
        queue = [node]
        while (len(queue) > 0):
            current = queue[0]
            queue.pop(0)
            visited.add(current)
            for neigbhor in graph[current]:
                if neigbhor not in visited:
                    queue.append(neigbhor)
    return False


def main():
    graph = {
        0: [4, 7],
        1: [],
        2: [],
        3: [6],
        4: [0],
        6: [3],
        7: [0],
        8: []
    }

    print(f"{graph} has {connected_components_count(graph)} connected components")


if __name__ == "__main__":
    main()
