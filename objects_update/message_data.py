from update_data import UpdateData


class MessageData(UpdateData):
    id: int
    text: str
    entities: str  # TODO type not correct
    entities_type: str
