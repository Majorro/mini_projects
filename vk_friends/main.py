import time
import vk_api
import argparse
from sys import argv


def argparse_():
    parser = argparse.ArgumentParser()
    parser.add_argument('--login')
    parser.add_argument('--password')
    args = parser.parse_args(argv[1:])
    return vars(args)


def get_friends(login, password):
    vk_session = vk_api.VkApi(login, password)
    vk_session.auth()
    friends = list(map(str, vk_session.method(method='friends.getOnline')))
    friends_string = ','.join(friends)
    users_objects = vk_session.method(method='users.get', values={'user_ids': friends_string})
    users = []
    for object in users_objects:
        users.append(object['first_name']+' '+object['last_name'])
    return users


if __name__ == '__main__':
    start = time.time()
    login_password = list(argparse_().values())
    online_friends = get_friends(login_password[0], login_password[1])
    print(online_friends)
    end = time.time()
    print('time =', end-start)