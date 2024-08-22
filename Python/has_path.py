def has_path(graph, src, dst):
    """
    Checks if a path exists between a source node and a destination node in a graph.

    Args:
        graph (dict): A dictionary representing the graph, wich is represented as an adjacency list.
        src (str): The source node.
        dst (str): The destination node.

    Returns:
        bool: True if a path exists from the source node to the destination node, False otherwise.
    """
    queue = [src]
    while (len(queue) > 0):
        current = queue[0]
        if current == dst:
            return True
        queue.pop(0)
        for neigbhor in graph[current]:
            if neigbhor == dst:
                return True
            queue.append(neigbhor)
    return False


def main():
    graph = {
        'f': ['g', 'i'],
        'g': ['h'],
        'h': [],
        'i': ['g', 'k'],
        'j': ['i'],
        'k': []
    }

    src = "f"
    dst = "j"
    hasPath = has_path(graph, src, dst)

    if hasPath:
        print(f"{graph} from '{src}' to '{dst}' has path")
    else:
        print(f"{graph} from '{src}' to '{dst}' has not path")


if __name__ == "__main__":
    main()
