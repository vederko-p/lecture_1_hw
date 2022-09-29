
from typing import List
from pydantic import BaseModel


class Art(BaseModel):
    """Article model"""

    title: str
    topic: str
    published: int | None = None


class DataBaseClass:
    def __init__(self, content: List[dict]):
        self.content = content

    def find_by(self, field: str, value: int | str) -> List[dict]:
        collected = []
        for cell in self.content:
            if cell[field] == value:
                collected.append(cell)
        return collected


class ArticlesDB(DataBaseClass):
    def __init__(self, content: List[dict]):
        super(ArticlesDB, self).__init__(content)
        self.len = len(content)
        self.max_size = 8

    def add_art(self, new_art: Art):
        self.content.append(new_art)
        self.len += 1


class SubscribesDB(DataBaseClass):
    def __init__(self, content: List[dict]):
        super(SubscribesDB, self).__init__(content)
        
    def check_user_subscribe_status(self, user_id: int) -> dict:
        res = self.find_by('user_id', user_id)
        return res[0]['status']

    def extend_subscribe(self, user_id: int):
        res = self.find_by('user_id', user_id)
        res[0]['status'] = 'Active'
        return 'Subscribe has been extended successfully'

    def add_user(self, sub_status: str, user_id: int):
        new_id = self.get_last_id + 1
        new_user = {
            'id': new_id,
            'status': sub_status,
            'user_id': user_id
            }
        self.content.append(new_user)

    def get_last_id(self):
        max_id = -1
        for cell in self.content:
            max_id = max(max_id, cell['user_id'])
        return max_id
