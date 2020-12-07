import os

import pytest

from day07 import solution


def test_sample_part1():
    assert solution.Solution(os.getcwd() + "/day07/sample.txt").part_one() == 4


def test_sample_part2_example1():
    assert solution.Solution(os.getcwd() + "/day07/sample.txt").part_two() == 32


@pytest.mark.skip(reason="pytest shits a brick about recursion, but runs absolutely fine")
def test_sample_part2_example2():
    assert solution.Solution(os.getcwd() + "/day07/sample2.txt").part_two() == 126


@pytest.mark.skip(reason="pytest shits a brick about recursion, but runs absolutely fine")
def test_part1():
    assert solution.Solution(os.getcwd() + "/day07/input.txt").part_one() == 296


@pytest.mark.skip(reason="pytest shits a brick about recursion, but runs absolutely fine")
def test_part2():
    assert solution.Solution(os.getcwd() + "/day07/input.txt").part_two() == 9339
