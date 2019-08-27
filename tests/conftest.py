import pytest
import sys

sys.path.append('.')
from server import creat_app # a changer des lignes

@pytest.fixture
def app():
    app = creat_app()       # rajouter des lignes 
    return app

@pytest.fixture
def client():
    app = create_app()     # rajouter des lignes
    client = app.test_client()
    yield client
