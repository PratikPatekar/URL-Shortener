# URL-Shortener using Flask
Just a Sample project created while learning Flask.

## Installation
Clone/Create project repository
```bash
git clone https://github.com/PratikPatekar/URL-Shortener/
cd URL-shortener
```

Use the packet manager [pip](https://pip.pypa.io/en/stable/) to install [pipenv](https://pypi.org/project/pipenv/)
```bash
pip install pipenv
pipenv install
```

Activate Pipenv shell using 
```bash
pipenv shell
```

Use pipenv to install the required packages using the requirements.txt file.
```bash
pipenv install -r requirements.txt
```

## Usage
Run the app using flask
```bash
flask run
```
or
Run the app using Gunicorn
```bash
gunicorn "urlshort:create_app()" -b 0.0.0.0
```

## Contribution
Pull Requests are Welcome :bowtie: 

#### Author [Pratik Patekar](https://github.com/PratikPatekar/) :octocat:
