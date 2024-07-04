def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.
    Args:
      boxes(list of list of int): A list where each element is a list of keys.

    Returns:
      bool: True if all boxes can be opened, False otherwise.
    """

    # Streamlined Validation
    if not all(isinstance(box, list) and all(isinstance(key, int) for key in box) for box in boxes if isinstance(boxes, list)):
        return False

    def dfs(index, visited):
        """
        Optimized Depth-first search to visit boxes.
        Includes cycle detection to prevent infinite recursion.

        Args:
          index (int): The index of the current box being visited.
          visited (set): A set of visited boxes to track progress and avoid revisits.
        """
        if index in visited or index >= len(boxes):
            return
        visited.add(index)
        for key in set(boxes[index]):  # Ensure key uniqueness and iterate efficiently
            if key not in visited:
                dfs(key, visited)

    visited = set()
    dfs(0, visited)

    return len(visited) == len(boxes)