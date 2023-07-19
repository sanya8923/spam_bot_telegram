from aiogram.utils.keyboard import InlineKeyboardMarkup
from aiogram.types import InlineKeyboardButton


def choice_groups_inline_keyboard(user_id, chat_data: list):
    print('choice_group_inline_keyboard')

    buttons = [
        [InlineKeyboardButton(text=f'{item["chat_name"]} (@{item["chat_username"]})',
                              callback_data=f'GrMan_{user_id}_{item["chat_id"]}')]
        for item in chat_data
    ]
    buttons.append([InlineKeyboardButton(text='Обновить список групп',
                                         callback_data=f'UpdGr_{user_id}')])

    return InlineKeyboardMarkup(inline_keyboard=buttons)


def button_update_groups_list(user_id):
    print('button_update_groups_list')
    button = [
        [InlineKeyboardButton(text='Обновить список групп', callback_data=f'UpdGr_{user_id}')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=button)


def group_management_inline_keyboard(chat_id: int, user_id: int):
    print('group_management_inline_keyboard')
    buttons = [
        [InlineKeyboardButton(text='Управление участниками', callback_data=f'MembManag_{user_id}_{chat_id}')],
        [InlineKeyboardButton(text='Управление администраторами', callback_data=f'Amanagement_{user_id}_{chat_id}')],
        [InlineKeyboardButton(text='Управление группой', callback_data=f'setting_{user_id}_{chat_id}')],
        [InlineKeyboardButton(text='Быстрая настройка группы', callback_data=f'Qsetting_{user_id}_{chat_id}')],
        [InlineKeyboardButton(text='Обратная связь', callback_data=f'feedback_{user_id}_{chat_id}')],
        [InlineKeyboardButton(text='Назад', callback_data=f'UpdGr_{user_id}')],
    ]

    return InlineKeyboardMarkup(inline_keyboard=buttons)


def management_admins_inline_keyboard(chat_id: int, user_id: int):
    print('management_admins_inline_keyboard')

    buttons = [
        [InlineKeyboardButton(text='Назначить администратора', callback_data=f'PromoteAdmin_{user_id}_{chat_id}')],
        [InlineKeyboardButton(text='Список администраторов', callback_data=f'AdminsList_{user_id}_{chat_id}')],
        [InlineKeyboardButton(text='Назад', callback_data=f'GrMan_{user_id}_{chat_id}')],
        [InlineKeyboardButton(text='К списку групп', callback_data=f'UpdGr_{user_id}')],
    ]

    return InlineKeyboardMarkup(inline_keyboard=buttons)


def members_management_inline_keyboard(chat_id: int, user_id: int):
    print('members_management_inline_keyboard')

    buttons = [
        [InlineKeyboardButton(text='Забанить участника', callback_data=f'BanUser_{user_id}_{chat_id}')],
        [InlineKeyboardButton(text='Разбанить участника', callback_data=f'UnbanUser_{user_id}_{chat_id}')],
        [InlineKeyboardButton(text='Замьютить участника', callback_data=f'MuteUser_{user_id}_{chat_id}')],
        [InlineKeyboardButton(text='Размьютить участника', callback_data=f'UnmuteUser_{user_id}_{chat_id}')],
        [InlineKeyboardButton(text='Назад', callback_data=f'GrMan_{user_id}_{chat_id}')],
        [InlineKeyboardButton(text='К списку групп', callback_data=f'UpdGr_{user_id}')],
    ]

    return InlineKeyboardMarkup(inline_keyboard=buttons)


def setting_group_inline_keyboard(chat_id: int, user_id: int):
    print('setting_group_inline_keyboard')

    buttons = [
        [InlineKeyboardButton(text='Управление бан-словами', callback_data=f'BanWords_{user_id}_{chat_id}')],
        [InlineKeyboardButton(text='Срок статуса "новый участник"', callback_data=f'NewMembTerm_{user_id}_{chat_id}')],
        [InlineKeyboardButton(text='Разрешить ссылки для новых участников', callback_data=f'NewMembLink_{user_id}_{chat_id}')],
        [InlineKeyboardButton(text='Разрешить ссылки', callback_data=f'Link_{user_id}_{chat_id}')],
        [InlineKeyboardButton(text='Разрешить пересылку сообщений из др. групп', callback_data=f'Forwarding_{user_id}_{chat_id}')],
        [InlineKeyboardButton(text='Слишком частый постинг', callback_data=f'TooOftenPost_{user_id}_{chat_id}')],
        [InlineKeyboardButton(text='Назад', callback_data=f'GrMan_{user_id}_{chat_id}')],
        [InlineKeyboardButton(text='К списку групп', callback_data=f'UpdGr_{user_id}')],
    ]

    return InlineKeyboardMarkup(inline_keyboard=buttons)


def button_return_to_member_management(chat_id: int, user_id: int):
    button = [
        [InlineKeyboardButton(text='Отмена', callback_data=f'MembManag_{user_id}_{chat_id}')]
    ]

    return InlineKeyboardMarkup(inline_keyboard=button)


def term_mute_inline_keyboard(chat_id: int, user_id_for_mute: int, user_id_who_mute: int):
    print('term_mute_inline_keyboard')
    buttons = [
        [
            InlineKeyboardButton(text='1 час',
                                 callback_data=f'term_hour_1_{user_id_for_mute}_{chat_id}_{user_id_who_mute}'),
            InlineKeyboardButton(text='2 часа',
                                 callback_data=f'term_hour_2_{user_id_for_mute}_{chat_id}_{user_id_who_mute}'),
            InlineKeyboardButton(text='3 час',
                                 callback_data=f'term_hour_3_{user_id_for_mute}_{chat_id}_{user_id_who_mute}')
        ],
        [
            InlineKeyboardButton(text='1 день',
                                 callback_data=f'term_day_1_{user_id_for_mute}_{chat_id}_{user_id_who_mute}'),
            InlineKeyboardButton(text='2 дня',
                                 callback_data=f'term_day_2_{user_id_for_mute}_{chat_id}_{user_id_who_mute}'),
            InlineKeyboardButton(text='3 дня',
                                 callback_data=f'term_day_3_{user_id_for_mute}_{chat_id}_{user_id_who_mute}')
        ],
        [
            InlineKeyboardButton(text='1 неделя',
                                 callback_data=f'term_week_1_{user_id_for_mute}_{chat_id}_{user_id_who_mute}'),
            InlineKeyboardButton(text='2 недели',
                                 callback_data=f'term_week_2_{user_id_for_mute}_{chat_id}_{user_id_who_mute}'),
            InlineKeyboardButton(text='3 недели',
                                 callback_data=f'term_week_3_{user_id_for_mute}_{chat_id}_{user_id_who_mute}'),
        ],
        [InlineKeyboardButton(text='Выбрать свой вариант',
                              callback_data=f'term_UserValue_{user_id_for_mute}_{chat_id}_{user_id_who_mute}')],
        [InlineKeyboardButton(text='Отмена', callback_data=f'MembManag_{user_id_who_mute}_{chat_id}')],
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)
