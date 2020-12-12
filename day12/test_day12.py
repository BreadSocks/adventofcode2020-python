import os

from day12 import solution


def test_sample_part1():
    assert solution.Solution(os.getcwd() + "/day12/sample.txt").part_one() == 25


def test_sample_part2():
    assert solution.Solution(os.getcwd() + "/day12/sample.txt").part_two() == 286


def test_part1():
    assert solution.Solution(os.getcwd() + "/day12/input.txt").part_one() == 2297


def test_part2():
    assert solution.Solution(os.getcwd() + "/day12/input.txt").part_two() == 89984
