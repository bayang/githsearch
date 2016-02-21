#!/usr/bin/env python3
# coding=utf-8

"""
Usage for githsearch :
options :
    -h or --help : display instructions
    -r or --repo [args] : search for args in github repos
    -u or --user [args] : search for args in github users
    -l or --limit : know your rate limit
example :
    githsearch -r python tetris
"""

from urllib.request import build_opener
from urllib.parse import urlencode
import json
import sys

__all__ = ['GithSearch', 'get_repo', 'get_user', 'get_limit']

PURPLE = "\033[1;35m"
NO_COLOUR = "\033[0m"


class GithSearch():
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
    def __init__(self):
        self.opener = build_opener()
        self.opener.addheaders.append(('User-agent', 'GithSearch - search Github from the CLI in Python, the quick and dirty way (github.com/bayang)'))

    def fetch_url(self, url, query):
        params = urlencode({'q': query})
        final = url.format(params)
        response = self.opener.open(final).read().decode('utf-8')
        dict_response = json.loads(response)
        return dict_response

    def get_repo(self, query):

        """Results are sorted by best match. Default sort order is desc
        """
        base_url = 'https://api.github.com/search/repositories?{}&per_page=50'
        res = self.fetch_url(base_url, query)
        resp = []
        for item in res['items']:
            resp.append((item['html_url'], item['description']))
        return resp

    def get_user(self, query):
        """Results are sorted by best match. Default sort order is desc
        """
        base_url = 'https://api.github.com/search/users?{}&per_page=50'
        res = self.fetch_url(base_url, query)
        respo = []
        for item in res['items']:
            respo.append((item['login'], item['html_url']))
        return respo

    @property
    def get_limit(self):
        """get your rate limit (e.g. the number of free requests remaining)
        """
        response = self.opener.open('https://api.github.com/rate_limit').read().decode('utf-8')
        txt = json.loads(response)
        return (txt['resources']['search'])

    @staticmethod
    def print_results(results):
        print("****** Query returned : ******")
        for item in results:
            print(PURPLE, '-->', item[0], NO_COLOUR)
            print('    --', item[1])

def main():
    g = GithSearch()
    rep = ['-r', '--repo', '--repository', ]
    usr_kw = ['-u', '--user', ]
    hlp = ['-h', '--help', '--please', '--what', ]
    lim = ['-l', '--limit', ]
    if len(sys.argv) == 1 or sys.argv[1].lower() in hlp:
        print(__doc__)

    elif sys.argv[1].lower() in rep:
        res = g.get_repo(sys.argv[2:])
        g.print_results(res)

    elif sys.argv[1].lower() in usr_kw:
        res = g.get_user(' '.join(sys.argv[2:]))
        g.print_results(res)

    elif sys.argv[1].lower() in lim:
        print(g.get_limit)
    else:
        print(__doc__)

if __name__ == '__main__':
    # g = GithSearch()
    # rep = ['-r', '--repo', '--repository', ]
    # usr_kw = ['-u', '--user', ]
    # hlp = ['-h', '--help', '--please', '--what', ]
    # lim = ['-l', '--limit', ]
    # if len(sys.argv) == 1 or sys.argv[1].lower() in hlp:
    #     print(__doc__)
    #
    # elif sys.argv[1].lower() in rep:
    #     res = g.get_repo(sys.argv[2:])
    #     g.print_results(res)
    #
    # elif sys.argv[1].lower() in usr_kw:
    #     res = g.get_user(' '.join(sys.argv[2:]))
    #     g.print_results(res)
    #
    # elif sys.argv[1].lower() in lim:
    #     print(g.get_limit)
    # else:
    #     print(__doc__)
    main()
