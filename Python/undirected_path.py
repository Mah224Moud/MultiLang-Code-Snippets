def undirected_path(edges, node_A, node_B):
    """
    This function checks if there is a path between two nodes in an undirected graph.

    Args:
        edges (list): A list of tuples representing the edges in the graph.
        node_A (str): The node to start the search from.
        node_B (str): The node to search for.

    Returns:
        bool: True if there is a path from node_A to node_B, False otherwise.
    """
    graph = generate_graph(edges)
    visited = set()
    queue = [node_A]
    while (len(queue) > 0):
        current = queue[0]
        queue.pop(0)
        if current == node_B:
            return True
        if current not in visited:
            visited.add(current)
            for i in graph[current]:
                queue.append(i)
    return False


def generate_graph(edges: list) -> dict:
    """
    This function generates the adjacency list from a list of edges reprensenting an undirected graph.

    Args:
        edges (list): A list of tuples representing the edges in the graph.

    Returns:
        dict: A dictionary representing the adjacency list of the graph.
    """
    graph = {}
    for (a, b) in edges:
        if a in graph:
            graph[a].append(b)
        else:
            graph[a] = [b]
        if b in graph:
            graph[b].append(a)
        else:
            graph[b] = [a]
    return graph


def main():

    edges = [
        ('i', 'j'),
        ('k', 'i'),
        ('m', 'k'),
        ('k', 'l'),
        ('o', 'n')
    ]
    src = "j"
    dst = 'm'
    has_path = undirected_path(edges, src, dst)
    if has_path:
        print(f"{edges} from {src} to {dst} has path")
    else:
        print(f"{edges} from {src} to {dst} has not path")


if __name__ == "__main__":
    main()
