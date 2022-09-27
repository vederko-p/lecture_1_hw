from app.utils import check_bd_free_space, check_originality
from app.articles_base import ArticlesDB


def test_check_bd():
    articles_bd = ArticlesDB()
    res = check_bd_free_space(articles_bd)
    assert isinstance(res, bool)


def test_check_originality_type():
    res = check_originality(1, 1)
    assert isinstance(res, tuple)

