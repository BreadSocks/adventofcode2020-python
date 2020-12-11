import os

from day09 import solution


def test_sample_part1():
    assert solution.Solution(os.getcwd() + "/day09/sample.txt").part_one() == 127


def test_sample_part2_example1():
    assert solution.Solution(os.getcwd() + "/day09/sample.txt").part_two() == 62


def test_part1():
    assert solution.Solution(os.getcwd() + "/day09/input.txt").part_one() == 167829540


def test_part2():
    assert solution.Solution(os.getcwd() + "/day09/input.txt").part_two() == 28045630
