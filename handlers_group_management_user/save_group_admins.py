from bot import bot
from han


async def save_group_admins(chat_id):
    admins_data = await bot.get_chat_administrators(chat_id)

    for line in admins_data:
        if line.status == 'administrator':
            print(f'id: {line.user.id}')
            print(f'username: {line.user.username}')
            print(f'first_name: {line.user.first_name}')
            print(f'last_name: {line.user.last_name}')



