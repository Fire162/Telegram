import telebot
from telebot import util

bot = telebot.TeleBot('7471178635:AAFtj4KEP-d9XE4AeNQfo9l57qfTEfXgYAw', parse_mode='HTML')

def get_admin(chat_id):
    try:
        admins = bot.get_chat_administrators(chat_id)
        admin_ids = [admin.user.id for admin in admins]
        return admin_ids
    except Exception as e:
        return []

@bot.chat_member_handler()
def chat_member_update_handler(message):
    status = message.new_chat_member.status
    if status == 'member':
        member(message)
    elif status == 'left':
        left(message)

def title(message):
    link = bot.create_chat_invite_link(message.chat.id).invite_link
    return f'<a href="{link}">{message.chat.title}</a>'

def member(message):
    admins = get_admin(message.chat.id)
    for admin in admins:
        try:
            bot.send_message(admin, f'{message.from_user.first_name} Has Joined {title(message)}')
        except:
            continue

def left(message):
    admins = get_admin(message.chat.id)
    for admin in admins:
        try:
            bot.send_message(admin, f'{message.from_user.first_name} Has Left {title(message)}')
        except:
            continue

allowed_updates = ['chat_member']

bot.infinity_polling(allowed_updates=allowed_updates)
