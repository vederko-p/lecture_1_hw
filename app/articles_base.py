from pydantic import BaseModel


class Art(BaseModel):
    """Article model"""

    title: str
    topic: str
    published: int | None = None


class ArticlesDB:
    content = [
        {'id': 0, 'title': 'Web Applications', 'topic': 'Web'},
        {'id': 1, 'title': 'IT News', 'topic': 'IT'},
        {'id': 2, 'title': 'Neural Networks', 'topic': 'NN'},
        {'id': 3, 'title': 'Deep Learning', 'topic': 'NN'},
        {'id': 4, 'title': 'Self Driving Cars', 'topic': 'IT'},
        {'id': 5, 'title': 'Triplet Loss', 'topic': 'NN'},
        {'id': 6, 'title': 'YOLOv5', 'topic': 'NN'}]
    len = len(content)
    max_size = 9

    def add_art(self, new_art: Art):
        self.content.append(new_art)
        self.len += 1
