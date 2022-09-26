
from app.articles_base import ArticlesDB


def check_free_space(bd: ArticlesDB) -> bool:
    return bd.max_size > bd.len
