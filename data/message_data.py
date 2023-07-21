from data import Data
from entities import Entities


class MessageData(Data):
    id: int
    text: str
    entities: Entities  # TODO type not correct
    entities_type: str
