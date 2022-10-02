
from fastapi import APIRouter

from app.articles_base import ArticlesDB, Art
from app.articles_base import SubscribesDB

from app.topic_model import TopicName

from app.utils import check_bd_free_space, check_originality

import app.databases_content as db_cont


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
            '/cgeck_topic/{topic_name} in docs']
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
