from __future__ import annotations

from typing import Callable

from vector import Vector

ProfitFunction = Callable[[Vector], float]


def sphere(vec: Vector) -> float:
    total = 0.0

    for dimension in vec:
        total += dimension ** 2

    return total


def rosenbrock(vec: Vector) -> float:
    total = 0.0

    for dimension in range(0, len(vec) - 1):
        component = vec[dimension]
        total += 100 * (vec[dimension + 1] - component ** 2) ** 2 + (1 - component) ** 2

    return total


def loads(name: str) -> ProfitFunction | None:
    functions = {
        "sphere": sphere,
        "rosenbrock": rosenbrock,
    }
    return functions.get(name, None)
