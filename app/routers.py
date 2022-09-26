from fastapi import APIRouter

from app.articles_base import ArticlesDB, Art
from app.topic_model import TopicName

from utils import check_bd_free_space, check_originality


router = APIRouter()
articles_bd = ArticlesDB()


@router.get('/')
def read_root():
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
    articles = [art['title'] for art in articles_bd.content]
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
