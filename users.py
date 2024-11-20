import os
from aiogram.types import Message

def create_dir():
    os.mkdir('users')
    with open('users/list_users.txt','w') as f:
        f.close()
    with open('users/list_admins.txt','w') as f:
        f.close()
    with open('users/list_ban.txt','w') as f:
        f.close()

def get_ids_users():
    with open('users/list_users.txt', 'r') as f:
        return list(map(lambda x: int(x.split(':')[0]), f.readlines()))

def add_user(message:Message):
    if message.from_user.id not in get_ids_users():
        with open('users/list_users.txt', 'a') as f:
            f.write(f'{message.from_user.id}:{message.from_user.username}\n')

def get_ids_admins():
    with open('users/list_admins.txt', 'r') as f:
        return list(map(lambda x: int(x.split(':')[0]), f.readlines()))

def check_in_admin(message:Message):
    return message.from_user.id in get_ids_admins()

def get_ids_ban():
    with open('users/list_ban.txt', 'r') as f:
        return list(map(lambda x: int(x.split(':')[0]), f.readlines()))

def check_in_ban(message:Message):
    return message.from_user.id in get_ids_ban()


