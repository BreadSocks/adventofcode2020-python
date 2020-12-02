import os

from day02 import solution


def test_sample_part1():
    assert solution.Solution(os.getcwd() + "/day02/sample.txt").part_one() == 2


def test_sample_part2():
    assert solution.Solution(os.getcwd() + "/day02/sample.txt").part_two() == 1


def test_part1():
    assert solution.Solution(os.getcwd() + "/day02/input.txt").part_one() == 636


def test_part2():
    assert solution.Solution(os.getcwd() + "/day02/input.txt").part_two() == 588
