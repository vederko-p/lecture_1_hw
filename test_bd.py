from app.utils import check_bd_free_space
from app.articles_base import ArticlesDB


def test_check_bd():
    articles_bd = ArticlesDB()
    assert isinstance(check_bd_free_space(articles_bd), bool)


def main():
    test_check_bd()


if __name__ == '__main__':
    main()
