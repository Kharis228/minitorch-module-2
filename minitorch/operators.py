"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# TODO: Implement for Task 0.1.
def mul(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b


def id(a: float) -> float:
    """Return the input unchanged."""
    return a


def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b


def neg(a: float) -> float:
    """Negate a number."""
    return -a


def lt(a: float, b: float) -> float:
    """Return 1.0 if a is less than b, else 0.0."""
    return 1.0 if a < b else 0.0


def eq(a: float, b: float) -> float:
    """Return 1.0 if a is equal to b, else 0.0."""
    return 1.0 if a == b else 0.0


def max(a: float, b: float) -> float:
    """Return the larger of two numbers."""
    return a if a > b else b


def is_close(a: float, b: float) -> bool:
    """Check whether two numbers are within 1e-2 of each other."""
    return abs(a - b) < 1e-2


def sigmoid(a: float) -> float:
    """Compute the sigmoid function."""
    return 1.0 / (1.0 + math.exp(-a))


def relu(a: float) -> float:
    """Return a if a is positive, else 0.0."""
    return a if a > 0 else 0.0


def log(a: float) -> float:
    """Compute the natural logarithm."""
    return math.log(a)


def exp(a: float) -> float:
    """Compute the exponential function."""
    return math.exp(a)


def inv(a: float) -> float:
    """Compute the reciprocal 1 / a."""
    return 1.0 / a


def log_back(a: float, d: float) -> float:
    """Compute the derivative of log at a, multiplied by d."""
    return d / a


def inv_back(a: float, d: float) -> float:
    """Compute the derivative of 1 / a at a, multiplied by d."""
    return -d / (a * a)


def relu_back(a: float, d: float) -> float:
    """Compute the derivative of relu at a, multiplied by d."""
    return d if a > 0 else 0.0


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


# TODO: Implement for Task 0.3.
def map(iterable: Iterable[float], func: Callable[[float], float]) -> Iterable[float]:
    """Apply func to each element of a list."""
    return [func(i) for i in iterable]


def zipWith(
    ls1: Iterable[float], ls2: Iterable[float], func: Callable[[float, float], float]
) -> Iterable[float]:
    """Combine elements of two lists pairwise using func."""
    return [func(x, y) for x, y in zip(ls1, ls2)]


def reduce(
    ls: Iterable[float], func: Callable[[float, float], float], start: float
) -> float:
    """Combine the elements of a list into one value using func, starting from start."""
    res = start
    for i in ls:
        res = func(res, i)
    return res


def negList(ls: Iterable[float]) -> Iterable[float]:
    """Negate each element of a list."""
    return map(ls, neg)


def addLists(ls1: Iterable[float], ls2: Iterable[float]) -> Iterable[float]:
    """Add two lists element-wise."""
    return zipWith(ls1, ls2, add)


def sum(ls: Iterable[float]) -> float:
    """Sum a list."""
    return reduce(ls, add, 0)


def prod(ls: Iterable[float]) -> float:
    """Take the product of a list."""
    return reduce(ls, mul, 1)
