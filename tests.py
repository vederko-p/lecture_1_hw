from app.utils import check_bd_free_space, check_originality
from app.articles_base import ArticlesDB


def test_check_bd():
    articles_bd = ArticlesDB()
    assert isinstance(check_bd_free_space(articles_bd), bool)


def test_check_originality():
    assert isinstance(check_originality(1, 1), tuple)
