class Data:
    type = 'data'
    id: int
    text: str


class UserData(Data):
    type = 'user_data'
    id: int
    username: str
    first_name: str
    last_name: str


class GroupData(Data):
    type = 'group_data'
    id: int
    chat_username: str
    chat_name: str


class Entities(Data):
    type = 'entities'
    type: str
    data: str   # TODO type not correct


class MessageData(Data):
    type = 'message'
    id: int
    text: str
    entities: Entities  # TODO type not correct
    entities_type: str
