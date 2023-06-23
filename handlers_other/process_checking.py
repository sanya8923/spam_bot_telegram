def check_members_data(m_data: list):
    for line in m_data:
        print(f'user_id: {line.user_id}'
              f'\tchat_id: {line.chat_id}'
              f'\tmessage_id: {line.message_id}'
              f'\tdate_message: {line.date_message}')
