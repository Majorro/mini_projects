import datetime
import time
import requests


def shifted_date(days):
    date_now = datetime.datetime.now()
    delta = datetime.timedelta(days=days)
    return date_now-delta

def get_trending_repositories(date):
    formated_date = date.strftime('%Y-%m-%d')
    params = {
        'q': formated_date,
        'sort': 'stars',
        'order': 'desc'
    }
    r = requests.get('https://api.github.com/search/repositories', params=params)
    repositories = r.json()['items']
    users = []
    max = 0
    for repo in repositories:
        users.append(repo['full_name'])
        max += 1
        if max == 20:
            break
    return users

def get_issues(users):
    params = {
        'state': 'open',
        'sort': 'created',
        'token': 'your_token'
    }
    for user in users:
        url = 'https://api.github.com/repos/{0}/issues'.format(user)
        r = requests.get(url, params=params)
        issues = r.json()
        if len(issues) != 0:
            print('\n', user.split('/')[1]+'\'s', 'issues = {0}'.format(len(issues)))
            for issue in issues:
                print('\t\tIssue: {0}'.format(issue['title']))
        else:
            print('\n', user.split('/')[1]+'\'s', 'issues = 0')


if __name__ == '__main__':
    start = time.time()
    
    result = get_trending_repositories(shifted_date(7))
    get_issues(result)

    end = time.time()
    print(end-start)
