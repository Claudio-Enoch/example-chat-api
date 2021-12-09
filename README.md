<br>
<div align="center">
  <code>
    <img height="350" src="https://media.giphy.com/media/fL1EXX8pQs0dd9zqLR/giphy.gif" alt="img">
  </code>
  <h2>Example Chat API</h2>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
<a><img alt="" src="https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg"></a>
<a><img alt="" src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg"></a>

</div>

### About The Project

Example chat API for sending messages from one user to another

### Run App 🐳

- Run application   
  `docker-compose up --build`

- Seed database  
  `docker exec -it example-chat-api_api_1 bash`  
  `python manage.py seed_db`

- Navigate to **http://localhost:5000/** for documentation

### Run Tests ✓

- Install  
  `pip install -r requirements.txt`
- Run tests  
  `pytest`

### Tools 🛠

- [Python3.9+](https://www.python.org/downloads/) - Programming language
- [Flask](https://flask.palletsprojects.com/) - Web framework
- [Flask-RESTX](https://flask-restx.readthedocs.io/en/latest/) - Framework extension for building a REST API
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) - SQLAlchemy ORM for Flask
- [Docker](https://www.docker.com/) - Containerization: build, ship, run anywhere
- [Pytest](https://docs.pytest.org/) - 🐛 Testing framework
- [Pytest-Cov](https://pytest-cov.readthedocs.io/) - Coverage report plugin
- [Black](https://black.readthedocs.io/en/stable/) - Uncompromising code formatter
- [Isort](https://pycqa.github.io/isort/) - Import formatter

### Documentation - Swagger 🗺

- Run `docker-compose up --build`
- Swagger docs containing sample requests and responses will be served at `http://localhost:5000/`

### Enhancements

- **Document** expected payloads in Swagger docs
- Marshal request and response payloads
- Leverage UUIDs instead of passing around primary_key INT IDs
- Separate DB from API
- Expand tests
- Implement Auth
- Leverage production ready WSGI server
- Convert REST API to GraphQL for general requests
    - Leverage sockets for live updates on incoming messages