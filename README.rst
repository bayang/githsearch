.. image:: https://img.shields.io/pypi/dm/githsearch.svg


githsearch
==========

Quick github search from the command line

Installation
------------

.. code-block:: python3

    pip install githsearch


Usage as a command line tool
----------------------------

.. code-block:: python3

    options :
        -h or --help : display instructions
        -r or --repo [args] : search for args in github repos
        -u or --user [args] : search for args in github users
        -l or --limit : know your rate limit
    example :
        githsearch -r python tetris

    sample output :
    --> https://github.com/davidcollins4481/tetris-clone
        -- Tetris Clone in Python (PyGame)
    --> https://github.com/zxmarcos/pytrix
        -- Tetris clone in Python + PyGame
    --> https://github.com/nickcrafford/python-pygame-tetris
        -- Quick and dirty Tetris clone written to learn Pygame.
    --> https://github.com/davepgreene/tetris-clone
        -- A Tetris clone written in Python with pygame

(Bonus : lines alternate in a purple color which is cute)


Using GithSearch programmatically
---------------------------------

You can search for repos or users.
First instantiate the main class, and to search for a repo call ``get_repo`` and pass the terms you want to search as arguments :

.. code-block:: python3

    >>> from githsearch import GithSearch
    >>> g=GithSearch()
    >>> g.get_repo('python tetris clone pygame')
    [('https://github.com/davidcollins4481/tetris-clone',
    'Tetris Clone in Python (PyGame)'),
    ('https://github.com/zxmarcos/pytrix', 'Tetris clone in Python + PyGame'),
    ('https://github.com/nickcrafford/python-pygame-tetris',
    'Quick and dirty Tetris clone written to learn Pygame.'),
    ('https://github.com/davepgreene/tetris-clone',
    'A Tetris clone written in Python with pygame'),
    ('https://github.com/AndreiMarks/BlindBlocks',
    'Tetris Clone written in Python 3.2 using Pygame 1.9.2'),
    ('https://github.com/dannyburrows/PoorMansTetris',
    'A Tetris clone, using python and pygame'), ...]


The search outputs the most relevant results.
To  search for a user is the same but call ``get_user`` instead

.. code-block:: python3

    >>> g.get_user('test')
    [('test', 'https://github.com/test'),
    ('prinnotamago', 'https://github.com/prinnotamago'),
    ('diannt', 'https://github.com/diannt'),
    ('73153', 'https://github.com/73153'),
    ('ssweetin', 'https://github.com/ssweetin'),
    ('deekoder', 'https://github.com/deekoder'),
    ('songkang666', 'https://github.com/songkang666'),
    ('ArdentZeal', 'https://github.com/ArdentZeal'),
    ('gitmobiletest', 'https://github.com/gitmobiletest'), ...]

But be aware that githsearch uses the free quotas from github search API so there is a rate limit. You can consult it by calling :

.. code-block:: python3

    >>> g.get_limit
    {'remaining': 10, 'reset': 1453497872, 'limit': 10}

As long as you don't hammer down the API you should be okay.

Changes :
---------
Feb 2016 : added Command line tool, refactoring, changed readme from markdown to restructuredtext so that it looks better on the Pypi.
