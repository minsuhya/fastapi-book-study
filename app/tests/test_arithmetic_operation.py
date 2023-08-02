#!/usr/bin/env python
# -*- coding: utf-8 -*-


def add(a: int, b: int) -> int:
    return a + b


def sub(a: int, b: int) -> int:
    return a - b


def mul(a: int, b: int) -> int:
    return a * b


def div(a: int, b: int) -> int:
    return a // b


def test_add() -> None:
    assert add(1, 2) == 3


def test_sub() -> None:
    assert sub(1, 2) == -1


def test_mul() -> None:
    assert mul(1, 2) == 2


def test_div() -> None:
    assert div(1, 2) == 0
