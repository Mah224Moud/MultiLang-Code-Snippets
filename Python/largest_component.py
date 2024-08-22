def largest_component(graph: dict) -> int:
    """
    This function finds the size of the largest connected component in a graph.

    Args:
        graph (dict): A dictionary representing the graph, which is represented as an adjacency list.

    Returns:
        int: The size of the largest connected component in the graph.
    """
    visited = set()
    largest = 0
    for node in graph:
        size = get_size(graph, node, visited)
        if size > largest:
            largest = size
    return largest


def get_size(graph: dict, node: int, visited: set) -> int:
    """
    This function calculates the size of a connected component in a graph.

    Args:
        graph (dict): A dictionary representing the graph, which is represented as an adjacency list.
        node (int): The node from which to start the search.
        visited (set): A set of nodes that have already been visited.
        size (list): A list to store the size of the connected component.

    Returns:
        int: The size of the connected component.
    """
    largest = 0
    if node in visited:
        return 0
    if not graph[node]:
        visited.add(node)
    else:
        queue = [node]
        while len(queue) > 0:
            current = queue[0]
            queue.pop(0)
            visited.add(current)
            largest += 1
            for neigbhor in graph[current]:
                if neigbhor not in visited and neigbhor not in queue:
                    queue.append(neigbhor)
    return largest


def main():
    graph = {
        0: [8, 1, 5],
        1: [0],
        5: [0, 8],
        8: [0, 5],
        2: [3, 4],
        3: [2, 4],
        4: [3, 2]
    }
    print(f"The largest component in {graph} is {largest_component(graph)}")


if __name__ == "__main__":
    main()
