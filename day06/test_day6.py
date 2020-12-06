import os

from day06 import solution


def test_sample_part1():
    assert solution.Solution(os.getcwd() + "/day06/sample.txt").part_one() == 11


def test_sample_part2():
    assert solution.Solution(os.getcwd() + "/day06/sample.txt").part_two() == 6


def test_part1():
    assert solution.Solution(os.getcwd() + "/day06/input.txt").part_one() == 7120


def test_part2():
    assert solution.Solution(os.getcwd() + "/day06/input.txt").part_two() == 3570
