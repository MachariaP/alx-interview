def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.
    Args:
      boxes (list of list of int): A list where each element is a list of keys.

    Returns:
      bool: True if all boxes can be opened, False otherwise.
    """

    # Input validation
    if not boxes or not all(isinstance(box, list) for box in boxes):
        return False

    unlocked = [False] * len(boxes)  # Track which boxes have been unlocked
    unlocked[0] = True  # The first box is always unlocked
    keys = set(boxes[0])  # Start with keys from the first box

    while keys:
        new_keys = set()
        for key in keys:
            if key < len(boxes) and not unlocked[key]:
                unlocked[key] = True  # Mark the box as unlocked
                new_keys.update(boxes[key])  # Add new keys from this box
        if not new_keys:
            break  # Exit if no new keys were found
        keys = new_keys

    return all(unlocked)