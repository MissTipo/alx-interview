#!/usr/bin/python3
"""Rotate 2D Matrix."""


def transpose(matrix):
    """Transpose matrix."""
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def reverse_columns(matrix):
    """Reverse columns of a matrix"""
    for i in range(len(matrix)):
        matrix[i].reverse()


def rotate_2d_matrix(matrix):
    """Rotate an n x n 2D matrix by 90 degrees clockwise."""
    transpose(matrix)
    reverse_columns(matrix)
    # print_matrix(matrix)
