import pytest
import sys

sys.path.append('.')
<<<<<<< HEAD
from __init__ import create_app

@pytest.fixture
def app():
    app = create_app()
=======
from app import create_app # a changer des lignes

@pytest.fixture
def app():
    app = create_app()       # rajouter des lignes 
>>>>>>> 71a4520b7fc522fbed88f21f00771b87a2a39b58
    return app

@pytest.fixture
def client():
<<<<<<< HEAD
    app = create_app()
    client = app.test_client()
    yield client


=======
    app = create_app()     # rajouter des lignes
    client = app.test_client()
    yield client
>>>>>>> 71a4520b7fc522fbed88f21f00771b87a2a39b58
