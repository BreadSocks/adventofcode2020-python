import os

from day05 import solution


def test_sample_part1():
    assert solution.Solution(os.getcwd() + "/day05/sample.txt").part_one() == 820


def test_part1():
    assert solution.Solution(os.getcwd() + "/day05/input.txt").part_one() == 959


def test_part2():
    assert solution.Solution(os.getcwd() + "/day05/input.txt").part_two() == 527
