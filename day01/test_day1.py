from day01 import solution
import os


def test_sample_part1():
    assert solution.Logic(os.getcwd() + "/day01/sample.txt").program(2) == 514579


def test_sample_part2():
    assert solution.Logic(os.getcwd() + "/day01/sample.txt").program(3) == 241861950


def test_part1():
    assert solution.Logic(os.getcwd() + "/day01/input.txt").program(2) == 964875


def test_part2():
    assert solution.Logic(os.getcwd() + "/day01/input.txt").program(3) == 158661360
