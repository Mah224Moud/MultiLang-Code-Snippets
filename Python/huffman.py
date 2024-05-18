
class Node:
    def __init__(self, frequency, character=None, left=None, right=None):
        """
        Initializes a new instance of the `Node` class.

        Args:
            frequency (int): The frequency of the node.
            character (Optional[str]): The character associated with the node. Defaults to None.
            left (Optional[Node]): The left child node. Defaults to None.
            right (Optional[Node]): The right child node. Defaults to None.
        """
        self.character = character
        self.frequency = frequency
        self.left = left
        self.right = right

    def __repr__(self):
        """
        Return a string representation of the Node object.

        Returns:
            str: A string representation of the Node object in the format "Node(character, frequency)".
        """
        return f"Node({self.character}, {self.frequency})"


def determines_frequencies(data: str) -> dict:
    """
    Determines the frequencies of each character in a given string.

    Parameters:
        data (str): The input string.

    Returns:
        dict: A dictionary where the keys are the characters in the string and the values are the frequencies of each character.
    """
    frequency = {}
    for i in data:
        frequency[i] = data.count(i)
    return frequency


def sort_by_frequency_asc(nodes: dict) -> None:
    """
    Sorts the nodes dictionary by frequency in ascending order.

    Parameters:
        nodes (dict): A dictionary containing nodes and their frequencies.

    Returns:
        None
    """
    return dict(sorted(nodes.items(), key=lambda i: i[1], reverse=False))


def build_tree(frequencies: dict) -> Node:
    """
    Builds a binary tree from a dictionary of character frequencies.

    Args:
        frequencies (dict): A dictionary where the keys are characters and the values are their corresponding frequencies.

    Returns:
        Node: The root node of the binary tree.

    Description:
        This function builds a binary tree from a dictionary of character frequencies. It creates a list of nodes, where each node represents a character and its frequency. The nodes are then sorted by frequency in ascending order and paired up to form parent nodes. This process continues until there is only one node left, which is the root node of the binary tree.

        The function uses the following steps:
        1. Iterate over the characters and frequencies in the input dictionary.
        2. Create a node for each character and add it to the list of nodes.
        3. While there are more than one node in the list, sort the nodes by frequency in ascending order.
        4. Pop the two nodes with the lowest frequencies from the list.
        5. Create a parent node with the sum of the frequencies of the two child nodes and the child nodes as left and right children.
        6. Add the parent node to the list of nodes.
        7. Repeat steps 3-6 until there is only one node left, which is the root node.
        """
    nodes = []
    for character, frequency in frequencies.items():
        nodes.append(Node(frequency, character))
    while len(nodes) > 1:
        nodes.sort(key=lambda node: node.frequency)
        left = nodes.pop(0)
        right = nodes.pop(0)
        parent = Node(frequency=left.frequency +
                      right.frequency, left=left, right=right)
        nodes.append(parent)
    return nodes[0]


def generate_code(node: Node, prefix: str = "") -> dict:
    """
    A recursive function that generates a dictionary of binary codes for characters based on a given binary tree node. 
    It traverses the binary tree starting from the given node and recursively generates the binary codes for each character. 
    If the node represents a character, it returns a dictionary with the character as the key and the binary code as the value. 
    If the node does not represent a character, it recursively calls itself on the left and right child nodes, adding "0" to the prefix when moving left and "1" when moving right, and combines the generated dictionaries. 
    Returns a dictionary where the keys are characters and the values are their corresponding binary codes.
    Args:
        node (Node): The current node in the binary tree.
        prefix (str): The binary code prefix for the current node. Defaults to an empty string.
    Returns:
        dict: A dictionary where the keys are characters and the values are their corresponding binary codes.
    """
    if node.character:
        return {node.character: prefix}
    else:
        return {**generate_code(node.left, prefix + "0"), **generate_code(node.right, prefix + "1")}


def huffman_compression(data: str, codes: dict):
    """
    Compresses the given data using Huffman coding.

    Args:
        data (str): The input string to be compressed.
        codes (dict): A dictionary mapping each character in the input string to its corresponding Huffman code.

    Returns:
        str: The compressed string obtained by concatenating the Huffman codes of each character in the input string.
    """
    result = ""
    for i in data:
        result += codes[i] + " "
    return result


def calculate_bits(original_text: str, frequencies: dict, codes: dict) -> dict:
    """
    Calculates the total number of bits required to encode the original text using the provided frequencies and codes.

    Parameters:
        original_text (str): The original text to be encoded.
        frequencies (dict): A dictionary containing the frequencies of each character in the text.
        codes (dict): A dictionary of binary codes for characters.

    Returns:
        dict: A dictionary containing the original number of bits, the total number of bits after encoding, and the percentage reduction in bits.
    """
    total = 0
    original = len(original_text) * 8
    for i in frequencies:
        total += frequencies.get(i) * len(codes.get(i))
    percentage = round(((original - total)/original) * 100, 2)
    return {
        "original": original,
        "after": total,
        "percentage": percentage
    }


def reverse_dict(original_codes: dict) -> dict:
    """
    Reverses a dictionary by swapping the keys and values.

    Parameters:
        original_codes (dict): The original dictionary to be reversed.

    Returns:
        dict: A new dictionary with the keys and values swapped.

    Raises:
        ValueError: If the values in the original dictionary are not unique.

    Example:
        >>> original_codes = {"a": 1, "b": 2, "c": 3}
        >>> reverse_dict(original_codes)
        {1: "a", 2: "b", 3: "c"}
    """
    if len(set(original_codes.values())) != len(original_codes):
        raise ValueError(
            "Les valeurs doivent être uniques pour inverser le dictionnaire sans perte de données.")
    return {value: key for key, value in original_codes.items()}


def huffman_decompression(compression_binaries: str, codes: dict):
    """
    Decompresses a compressed string using Huffman coding.

    Args:
        compression_binaries (str): The compressed string to be decompressed.
        codes (dict): A dictionary mapping each Huffman code to its corresponding character.

    Returns:
        str: The decompressed string obtained by concatenating the characters corresponding to the Huffman codes in the compressed string.
    """
    compression = compression_binaries.split(" ")
    codes = reverse_dict(codes)
    result = ""
    for i in compression:
        if i in codes:
            result += codes[i]
    return result


def main():
    text = "wikipedia"
    print(f"original: {text}\n")
    freq = determines_frequencies(text)
    print(f"Frequence of each character :\n {sort_by_frequency_asc(freq)}\n")
    root = build_tree(freq)
    print(f"Huffman Tree : {root}\n")
    code = generate_code(root)
    print(f"Code of each character :\n {code}\n")
    compressed = huffman_compression(text, code)
    print(f"Compressed : {compressed}\n")

    result = calculate_bits(text, freq, code)
    print(
        f"After compression, we gets {result.get('after')} bits which is {result.get('original')} bits ({len(text)} characters x 8 bits per character).\n")
    decompression = huffman_decompression(compressed, code)

    print("Decompressed :", decompression)


if __name__ == "__main__":
    main()
