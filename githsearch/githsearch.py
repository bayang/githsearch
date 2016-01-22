#!/usr/bin/env python3
# coding=utf-8

"""
Usage :
Instantiate the class
>>> g=GithSearch()
Search for a repo :
>>> g.get_repo('python tetris pygame')
Search for a user :
>>> g.get_user('toto')
Know the rate_limit :
>>> g.get_limit
"""

from urllib.request import build_opener
from urllib.parse import urlencode
import json

__all__ = ['GithSearch', 'get_repo', 'get_user', 'get_limit']

PURPLE = "\033[1;35m"
NO_COLOUR = "\033[0m"


class GithSearch():
    def __init__(self):
        self.opener = build_opener()
        self.opener.addheaders.append(('User-agent', 'GithSearch - search Github from the CLI in Python, the quick and dirty way (github.com/bayang)'))

    def get_repo(self, query, printed=True):
        """Results are sorted by best match. Default sort order is desc
        """
        base_url = 'https://api.github.com/search/repositories?{}'
        params = urlencode({'q': query})
        final = base_url.format(params)
        response = self.opener.open(final).read().decode('utf-8')
        dict_response = json.loads(response)
        if printed:
            for item in dict_response['items']:
                print(PURPLE, '-->', item['html_url'], NO_COLOUR)
                print('    --', item['description'])
        else:
            resp = []
            for item in dict_response['items']:
                resp.append((item['html_url'], item['description']))
            return resp

    def get_user(self, query, printed=True):
        """Results are sorted by best match. Default sort order is desc
        """
        base_url = 'https://api.github.com/search/users?{}'
        params = urlencode({'q': query})
        final = base_url.format(params)
        response = self.opener.open(final).read().decode('utf-8')
        dict_response = json.loads(response)
        if printed:
            for item in dict_response['items']:
                print(PURPLE, '-->', item['login'], NO_COLOUR)
                print('    --', item['html_url'])
        else:
            resp = []
            for item in dict_response['items']:
                resp.append((item['login'], item['html_url']))
            return resp

    @property
    def get_limit(self):
        """get your rate limit (e.g. the number of free requests remaining)
        """
        response = self.opener.open('https://api.github.com/rate_limit').read().decode('utf-8')
        txt = json.loads(response)
        return (txt['resources']['search'])
