
import pytest

from app.utils import check_bd_free_space, check_originality
from app.articles_base import ArticlesDB


def test_check_bd():
    articles_bd = ArticlesDB()
    res = check_bd_free_space(articles_bd)
    assert isinstance(res, bool)


def test_check_originality_type():
    res = check_originality(1, 1)
    assert isinstance(res, tuple)


def test_integration():
    articles_bd = ArticlesDB()
    article_new = {
        'title': 'New Title with Neural Network',
        'topic': 'NN',
        'published': 137
    }
    len_before = articles_bd.len
    articles_bd.add_art(article_new)
    len_after = articles_bd.len
    assert len_after - len_before == 1


@pytest.mark.parametrize("var, expectation", [(0.3, False),
                                              (0.49, False),
                                              (0.5, False),
                                              (0.51, True),
                                              (0.7, True),
                                              (0.95, True)])
def test_originality_reaction(var, expectation):
    decision, _ = check_originality(None, None, custom_rate=var)
    assert decision == expectation
