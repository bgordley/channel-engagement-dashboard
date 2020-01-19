from service.models.model_base import ModelBase


class Stream(ModelBase):
    id: str
    title: str
    game: str
    start_time: str
    viewer_count: int
