## githsearch

For quick checking from the command line

## Installation
`pip install githsearch`


## Usage

You can search for repos or users.
First instantiate the main class,
and to search for a repo call `get_repo` and pass the terms you want to search as arguments :
```python
>>> from githsearch import GithSearch
>>> g=GithSearch()
>>> g.get_repo('python tetris clone pygame')
 --> https://github.com/davidcollins4481/tetris-clone
    -- Tetris Clone in Python (PyGame)
 --> https://github.com/zxmarcos/pytrix
    -- Tetris clone in Python + PyGame
 --> https://github.com/nickcrafford/python-pygame-tetris
    -- Quick and dirty Tetris clone written to learn Pygame.
 --> https://github.com/davepgreene/tetris-clone
    -- A Tetris clone written in Python with pygame
...
```

The search outputs the 30 most relevant results.
To  search for a user is the same but call `get_user` instead
```python
>>> g.get_user('test')
 --> test
    -- https://github.com/test
 --> prinnotamago
    -- https://github.com/prinnotamago
 --> diannt
    -- https://github.com/diannt
 --> 73153
    -- https://github.com/73153
 --> ssweetin
    -- https://github.com/ssweetin
 --> deekoder
    -- https://github.com/deekoder
...
```

But be aware that githsearch uses the free quotas from github search API so there is a rate limit. You can consult it by calling :
```python
>>> g.get_limit
{'remaining': 10, 'reset': 1453497872, 'limit': 10}
```
As long as you don't hammer down the API you should be okay.

Another thing : by default the results are just **displayed** on the terminal.
You can have the results in a variable by calling the functions with the flag `printed` set to `False` like so :
```python
>>> result=g.get_repo('python tetris', printed=False)
>>> len(result)
30
>>>
```

(Bonus : lines alternate in a purple color which is cute)
