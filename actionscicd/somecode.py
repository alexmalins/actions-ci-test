"""Some basic Python code for adding two NumPy vectors and loading data from a
sub-packaged TSV file."""

from typing import List, Tuple
import numpy as np

try:
    from importlib import resources
except ImportError:
    import importlib_resources as resources  # type:ignore


def add_arrays(vec1: np.ndarray, vec2: np.ndarray) -> np.ndarray:
    """Adds two numpy arrays"""

    result: np.ndarray = vec1 + vec2
    return result


def load_datafile(filename: str) -> Tuple[List[str], List[int]]:
    """Loads people's names and ages from a TSV file"""

    names = []
    ages = []

    with resources.open_text(f"{__package__}.data", filename) as file:
        for idx, line in enumerate(file.readlines()):
            if idx == 0:
                continue
            lineentries = line.split()
            names.append(lineentries[0])
            ages.append(int(lineentries[1]))

    return (names, ages)


def unused_fn() -> None:
    """Unused dummy function to give an example of code not covered by tests"""

    return