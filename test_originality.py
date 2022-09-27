from app.utils import check_originality


def test_check_originality():
    assert isinstance(check_originality(1, 1), tuple)


def main():
    test_check_originality()


if __name__ == '__main__':
    main()
