def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.
    Args:
      boxes(list of list of int): A list where each element is a list of keys.

    Returns:
      bool: True if all boxes can be opened, False otherwise.
    """

    def dfs(index):
        """
        Depth-first search to visit boxes.

        Mark the current box as visited and recursively visit boxes
        for which the current box contains keys.

        Args:
          index (int): The index of the current box being visited.
        """

        visited.add(index)
        for key in boxes[index]:
            if key not in visited and key < len(boxes):
                dfs(key)

    visited = set()
    dfs(0)

    return len(visited) == len(boxes)
