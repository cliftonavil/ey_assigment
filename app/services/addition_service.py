from multiprocessing import Pool
from typing import List


def add_pair(pair):
    return sum(pair)


def perform_addition(payload: List[List[int]]) -> List[int]:
    with Pool() as pool:
        result = pool.map(add_pair, payload)
    return result
