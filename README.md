# Requirements:

-Python 3.8

# Install :

- git clone git@github.com:programgames/pokepedia-middleware.git
- cd pokepedia-middleware
- git submodule init
- git submodule update
- pip install -r requirements.txt
- cd pokedex 
- sudo python setup.py develop
- cd ..
- sudo pip install -e pokedex
- pokedex load -e sqlite:///run/db.sqlite 
- cp .env.dist .env
- setup your env variables
- python middleware.py init