import vk
import getpass


APP_ID = 6236179


def get_user_login():
    return input('Input VK login: ')


def get_user_password():
    return getpass.getpass('Input password: ')


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
    )
    api = vk.API(session)
    friends_ids = api.friends.get()
    friends_online = []
    for friend_id in friends_ids:
        friend = api.users.get(user_id=friend_id, fields='online')[0]
        if friend['online']:
            friends_online.append(friend)
    return friends_online


def output_friends_to_console(friends_online):
    if not friends_online:
        print('All friends are offline.')
        return
    print('Friends online: ')
    for friend in friends_online:
        print(friend['last_name'], friend['first_name'])


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
