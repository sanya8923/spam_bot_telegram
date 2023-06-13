# from typing import Union, Dict, Any
#
# from aiogram.filters import BaseFilter
# from aiogram.types import Message
# from aiogram.types.chat_join_request import ChatJoinRequest
#
#
# class NewMember(BaseFilter):
#     async def __call__(self, join: ChatJoinRequest):
#         new_user = join.user_chat_id()
#         print(f'new_user: {new_user}')
