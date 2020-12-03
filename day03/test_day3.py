import os

from day03 import solution


def test_sample_part1():
    assert solution.Solution(os.getcwd() + "/day03/sample.txt").part_one() == 7


def test_sample_part2():
    assert solution.Solution(os.getcwd() + "/day03/sample.txt").part_two() == 336


def test_part1():
    assert solution.Solution(os.getcwd() + "/day03/input.txt").part_one() == 254


def test_part2():
    assert solution.Solution(os.getcwd() + "/day03/input.txt").part_two() == 1666768320
