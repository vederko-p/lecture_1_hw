
from typing import Tuple

import random
from app.articles_base import ArticlesDB, Art


def check_bd_free_space(bd: ArticlesDB) -> bool:
    return bd.max_size > bd.len


def check_originality(bd: ArticlesDB, art: Art) -> Tuple[float, float]:
    r = random.random()
    return r > 0.5, round(r, 2)
