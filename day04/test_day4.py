import os

from day04 import solution


def test_sample_part1():
    assert solution.Solution(os.getcwd() + "/day04/sample.txt").part_one() == 2


def test_sample_part2_example1():
    assert solution.Solution(os.getcwd() + "/day04/valid_sample.txt").part_two() == 4


def test_sample_part2_example2():
    assert solution.Solution(os.getcwd() + "/day04/invalid_sample.txt").part_two() == 0


def test_part1():
    assert solution.Solution(os.getcwd() + "/day04/input.txt").part_one() == 170


def test_part2():
    assert solution.Solution(os.getcwd() + "/day04/input.txt").part_two() == 103
