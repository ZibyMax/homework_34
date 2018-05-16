from pprint import pprint
import requests


class YAMetrica:
    request_url = 'https://api-metrika.yandex.ru/stat/v1/data'

    def __init__(self, access_token, counter_id):
        self.access_token = access_token
        self.counter_id = counter_id

    def get_visits(self):
        param = {'metrics': 'ym:s:visits',
                 'id': self.counter_id,
                 'oauth_token': self.access_token}
        return requests.get(self.request_url, param)

    def get_pageviews(self):
        param = {'metrics': 'ym:s:pageviews',
                 'id': self.counter_id,
                 'oauth_token': self.access_token}
        return requests.get(self.request_url, param)

    def get_users(self):
        param = {'metrics': 'ym:s:users',
                 'id': self.counter_id,
                 'oauth_token': self.access_token}
        return requests.get(self.request_url, param)


def main():
    access_token = 'AQAEA7qgxGPDAAT-0JwhPf4-2U3oi0xUjxTmtVc'
    counter_id = '48829715'
    my_counter = YAMetrica(access_token, counter_id)

    visits = my_counter.get_visits()
    pageviews = my_counter.get_pageviews()
    users = my_counter.get_users()

    pprint(visits.json())
    pprint(pageviews.json())
    pprint(users.json())


main()