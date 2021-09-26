# Requirements:

-Python 3.8

# Install :

- git clone git@github.com:programgames/pokepedia-middleware.git
- cd pokepedia-middleware
- git submodule init
- git submodule update
- pip install -r /path/to/requirements.txt
- cd veekun 
- sudo python setup.py develop
- cd ..
- pip install -e veekun
- pokedex load -e sqlite:///local/db.sqlite
- cp .env.dist .env
- setup your env variables
- python main.py init