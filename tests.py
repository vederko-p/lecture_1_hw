
import pytest

from app.utils import check_bd_free_space, check_originality, add_random_users
from app.articles_base import ArticlesDB, SubscribesDB

import app.databases_content as db_cont

import grpc
import app.grpc_files.basic_pb2 as basic_pb2
import app.grpc_files.basic_pb2_grpc as basic_pb2_grpc


def test_check_bd():
    articles_bd = ArticlesDB(db_cont.articles_data)
    res = check_bd_free_space(articles_bd)
    assert isinstance(res, bool)


def test_check_originality_type():
    res = check_originality(1, 1)
    assert isinstance(res, tuple)


@pytest.mark.parametrize("var, expectation", [(0.3, False),
                                              (0.49, False),
                                              (0.5, False),
                                              (0.51, True),
                                              (0.7, True),
                                              (0.95, True)])
def test_originality_reaction(var, expectation):
    decision, _ = check_originality(None, None, custom_rate=var)
    assert decision == expectation


def test_integration_1():
    articles_bd = ArticlesDB(db_cont.articles_data)
    article_new = {
        'title': 'New Title with Neural Network',
        'topic': 'NN',
        'published': 137
    }
    len_before = articles_bd.len
    articles_bd.add_art(article_new)
    len_after = articles_bd.len
    assert len_after - len_before == 1


def test_integration_2():
    subscribes_bd = SubscribesDB(db_cont.subscribes_data)
    expired_sub_user_id = 1
    subscribes_bd.extend_subscribe(expired_sub_user_id)
    assert subscribes_bd.check_user_subscribe_status(expired_sub_user_id) == 'Active'


@pytest.mark.parametrize("var, expectation", [(1, 1),
                                              (2, 2),
                                              (5, 5)])
def test_integration_3(var, expectation):
    subscribes_bd = SubscribesDB(db_cont.subscribes_data)
    len_before = len(subscribes_bd)
    add_random_users(var, subscribes_bd)
    len_after = len(subscribes_bd)
    assert len_after - len_before == expectation


@pytest.mark.parametrize(
    "var1, var2, expectation",
    [
        (1, 1, 2),
        (2, 2, 4),
        (2, 3, 5),
        (4, 3, 7),
        (6, 5, 11)
    ])
def test_integration_grpc(var1, var2, expectation):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = basic_pb2_grpc.SimpleActionsStub(channel)
        message = basic_pb2.SumRequest(a=var1, b=var2)
        response = stub.AddNumbers(message)
    assert response.c == expectation
