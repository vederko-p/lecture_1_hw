
from typing import Tuple

import random
from app.articles_base import ArticlesDB, Art
from app.articles_base import SubscribesDB


def random_error(func):
    def _wrapper(*args, **kwargs):
        error_threshold = 1
        error_p = random.random()
        if error_p > error_threshold:
            return 'error'
        else:
            result = func(*args, **kwargs)
            return result
    return _wrapper


@random_error
def check_bd_free_space(bd: ArticlesDB) -> bool:
    return bd.max_size > bd.len


@random_error
def check_originality(
    bd: ArticlesDB, art: Art,
    custom_rate: float | None = None
) -> Tuple[float, float]:
    orig_threshold = 0.5
    if custom_rate is None:
        r = random.random()
    else:
        r = custom_rate
    return r > orig_threshold, round(r, 2)


def add_random_users(n: int, users_bd: SubscribesDB):
    for _ in range(n):
        users_bd.add_user('1', random.randint(100, 1000))
