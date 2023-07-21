class Data:
    id: int
    text: str


class UserData(Data):
    id: int
    username: str
    first_name: str
    last_name: str


class GroupData(Data):
    id: int
    chat_username: str
    chat_name: str


class Entities(Data):
    type: str
    data: str   # TODO type not correct


class MessageData(Data):
    id: int
    text: str
    entities: Entities  # TODO type not correct
    entities_type: str
