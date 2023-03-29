#!/usr/bin/python3
"""Lockboxes"""
def canUnlockAll(boxes):
    """Determines if all the boxes can be opened"""
    n = len(boxes)
    unlocked_boxes = [0]
    for box_num, box in enumerate(boxes):
        for key in box:
            if key < n and key not in unlocked_boxes and key != box_num:
                unlocked_boxes.append(key)
    return len(unlocked_boxes) == n
