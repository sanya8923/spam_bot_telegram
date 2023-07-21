from data import Data


class MessageData(Data):
    id: int
    text: str
    entities: str  # TODO type not correct
    entities_type: str
