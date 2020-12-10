import os

from day08 import solution


def test_sample_part1():
    assert solution.Solution(os.getcwd() + "/day08/sample.txt").part_one() == 5


def test_sample_part2_example1():
    assert solution.Solution(os.getcwd() + "/day08/sample.txt").part_two() == 8


def test_part1():
    assert solution.Solution(os.getcwd() + "/day08/input.txt").part_one() == 1553


def test_part2():
    assert solution.Solution(os.getcwd() + "/day08/input.txt").part_two() == 1877
