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
        scope='friends',
    )
    api = vk.API(session)
    return api.friends.getOnline()


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
