
from sqlite3 import connect
from fastapi import APIRouter

from app.articles_base import ArticlesDB, Art
from app.articles_base import SubscribesDB

from app.topic_model import TopicName

from app.utils import check_bd_free_space, check_originality

import app.databases_content as db_cont

import grpc
import app.grpc_files.basic_pb2 as basic_pb2
import app.grpc_files.basic_pb2_grpc as basic_pb2_grpc

import pika


pika_params = pika.ConnectionParameters(host='localhost', port=5672)

router = APIRouter()

articles_bd = ArticlesDB(db_cont.articles_data)
subscribes_bd = SubscribesDB(db_cont.subscribes_data)


@router.get('/')
async def read_root():
    content = [
        'Possible routes:',
        [
            '/articles',
            '/articles/<str art_topic> (Web, IT, NN)',
            '/articles/<str art_topic>?number=<int number>',
            '/articles/add in docs',
            '/check_topic/{topic_name} in docs',
            '/check_subscribe/{user_id}<int number>',
            '/extend_subscribe/{user_id}<int number>',
            '/check_grpc?n1=<int number>&n2=<int number>'
            ]
        ]
    return content


@router.get('/articles')
async def get_aricles():
    articles = [art['title'] for art in articles_bd.content]  # TODO: Исправить все места со сбором данных из БД (использовать find_by)
    return articles


@router.get('/articles/{art_topic}')
async def get_certain_aricles(art_topic: str, number: int | None = None):
    articles = [art['title'] for art in articles_bd.content if art['topic'] == art_topic]
    return articles[:number]


@router.post('/articles/add')
async def add_article(art: Art):
    article = art.dict()
    if art.published is not None:
        article['published'] = art.published
    if check_bd_free_space(articles_bd):
        dicision, rate = check_originality(articles_bd, article)
        if dicision:
            articles_bd.add_art(article)
            text = 'Article was successfully published!'
        else:
            text = f'Originality of the article is too low: {rate}..'
    else:
        text = 'There\'s no free space for new article..'
    return text


@router.get('/check_topic/{topic_name}')
async def check_topic(topic_name: TopicName):
    if topic_name is TopicName.web:
        n = len(list(filter(lambda art: art['topic'] == TopicName.web.value, articles_bd.content)))
        return {'info': f'There\'s {n} articles of {TopicName.web.value} topic!'}
    if topic_name.value == 'IT':
        return {'topic_name': topic_name, 'info': 'I love IT!'}
    return {'topic_name': topic_name, 'info': 'cNN\'s are cool!'}


@router.get('/check_subscribe/{user_id}')
async def get_certain_aricles(user_id: int):
    user_sub_status = subscribes_bd.check_user_subscribe_status(user_id)
    return user_sub_status


@router.get('/extend_subscribe/{user_id}')
async def get_certain_aricles(user_id: int):
    report = subscribes_bd.extend_subscribe(user_id)
    return report


@router.get('/check_grpc')
async def get_certain_aricles(n1: int, n2: int):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = basic_pb2_grpc.SimpleActionsStub(channel)
        message = basic_pb2.SumRequest(a=n1, b=n2)
        response = stub.AddNumbers(message)
    res = {'result': response.c}
    return res


@router.get('/publish_new_article')
async def publish_new_article():
    connection = pika.BlockingConnection(pika_params)
    channel = connection.channel()
    msg = 'New article has been published!'
    message = bytes(msg, encoding='utf8')
    channel.basic_publish(
        exchange='new_article', routing_key='new_art_key', body=message
        )
    channel.close()
    return msg

@router.get('/check_for_article/{user_id}')
async def check_for_article(user_id: int):
    user_sub_status = subscribes_bd.check_user_subscribe_status(user_id)
    if user_sub_status == 'Active':
        connection = pika.BlockingConnection(pika_params)
        channel = connection.channel()
        _, _, msg = next(channel.consume('new_article_queue'))
        channel.close()
    else:
        msg = 'To see notifications about recently published articles update your subscribe!'
    return msg
