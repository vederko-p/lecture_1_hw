from app.utils import check_bd_free_space, check_originality
from app.articles_base import ArticlesDB, Art


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
