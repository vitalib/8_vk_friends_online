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
    friends_online_ids = api.friends.getOnline()
    if friends_online_ids:
        return api.users.get(user_ids=friends_online_ids)
    else:
        return None


def output_friends_to_console(friends_online):
    if friends_online:
        print('Friends online: ')
        for friend in friends_online:
            print(friend['last_name'], friend['first_name'])
    else:
        print('All friends are offline.')


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
