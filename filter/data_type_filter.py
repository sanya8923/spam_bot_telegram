from typing import Any, Union, List


class MyRouter:
    pass

class DataTypeRouter(MyRouter):
    def __init__(self, *args: str, **kwargs):
        self.data_type = args[0]  # TODO: don't working. Add right

    async def __call__(self, data: Union[Any, List[Any]]):
        type_data = data.type  # TODO: don't working. Add right
        try:
            if isinstance(type_data, list):
                return self.data_type in type_data
            else:
                return self.data_type == type_data
        except TypeError as e:
            raise f'{e} in DataTypeRouter'