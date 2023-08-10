"""
You are keeping the score of a baseball game where past rounds might affect future rounds' scores.
given a list of strings:
'ops' where ops[i] is the ith operation you must apply to the record.
an int x that records new score of x
'+' that records a new score that is the sum of previous 2 scores, there will always be 2 previous scores
'D' that records a new score that is double the previous score
'c' invalidates the previous score, removing it from the record
Return sum of all scores on the record

"""


def calPoints(ops) -> int:
    """Return Sum of all scores on the record"""
    result = None

    return result


# Example usage:
ops = ["5", "2", "C", "D", "+"]
print(calPoints(ops))  # Output: 30
