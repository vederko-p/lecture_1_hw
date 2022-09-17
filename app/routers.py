from fastapi import APIRouter

from app.articles_base import articles_bd, Art


router = APIRouter()


@router.get('/')
def read_root():
    content = [
        'Possible routes:',
        [
            '/articles',
            '/articles/<str art_topic> (Web, IT, NN)',
            '/articles/<str art_topic>?number=<int number>',
            '/articles/add in docs']
        ]
    return content


@router.get('/articles')
async def get_aricles():
    articles = [art['title'] for art in articles_bd]
    return articles


@router.get('/articles/{art_topic}')
async def get_certain_aricles(art_topic: str, number: int | None = None):
    articles = [art['title'] for art in articles_bd if art['topic'] == art_topic]
    return articles[:number]


@router.post('/articles/add')
async def add_article(art: Art):
    article = art.dict()
    if art.published is not None:
        article['published'] = art.published
    return article
