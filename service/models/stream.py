from service.models.game import Game
from service.models.model_base import ModelBase


class Stream(ModelBase):
    id: str
    title: str
    game: Game
    start_time: str
    viewer_count: int
