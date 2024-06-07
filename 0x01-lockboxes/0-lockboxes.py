#!/usr/bin/python3
"""This modoule is about lockboxes dsa in python"""


def canUnlockAll(boxes):
    """Determine if all boxes can be unlocked"""
    unlocked_boxes = set([0])
    keys = [0]  # Start with the first box, which is always unlocked

    while keys:
        # Get the last key from the keys list
        current_key = keys.pop()
        for key in boxes[current_key]:
            if key not in unlocked_boxes and key < len(boxes):
                unlocked_boxes.add(key)
                keys.append(key)

    return len(unlocked_boxes) == len(boxes)
