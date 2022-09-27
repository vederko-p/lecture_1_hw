
from typing import Tuple

import random
from app.articles_base import ArticlesDB, Art


def random_error(func):
    def _wrapper(*args, **kwargs):
        error_p = random.random()
        if error_p > 0.5:
            return 'error'
        else:
            result = func(*args, **kwargs)
            return result
    return _wrapper


@random_error
def check_bd_free_space(bd: ArticlesDB) -> bool:
    return bd.max_size > bd.len


@random_error
def check_originality(bd: ArticlesDB, art: Art) -> Tuple[float, float]:
    r = random.random()
    return r > 0.5, round(r, 2)
