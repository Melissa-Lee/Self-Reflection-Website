import pytest

from project import app, db  #Import app object from project.py

@pytest.fixture # client is the fixture that provides a testing client
def client():  # Set up a Flask test client
    app.config['TESTING'] = True

    with app.test_client() as client:
        with app.app_context():
            db.execute("CREATE TABLE IF NOT EXISTS reflections (id INTEGER PRIMARY KEY, date TEXT, category TEXT, content TEXT)")
        yield client
        with app.app_context():
            db.execute("DROP TABLE reflections")

def test_main(client): # Test the main function
    response = client.get("/")
    assert response.status_code == 200 #200 is successful request in response status code
    assert b"reflections" in response.data

def test_records(client):
    response = client.get("/records")
    assert response.status_code == 200
    assert b"reflections" in response.data


def test_add_reflection(client): #Test the add_reflection function
    test_data = {
        "date": "2023-12-21",
        "category": "Work",
        "content": "Testing for adding a reflection."
    }
    response = client.post("/add_reflection", data=test_data, follow_redirects=True)
    assert response.status_code == 200 #200 is successful request in response status code
    assert b"Testing for adding a reflection." in response.data

def test_remove(client):
    client.post("/add_reflection", data = {
        "date": "2023-12-21",
        "category": "Work",
        "content": "Testing for adding a reflection."
    })
    response = client.post("/remove", data={"id": 1}, follow_redirects=True)
    assert response.status_code == 200 #200 is successful request in response status code
    assert b"Testing for adding a reflection." not in response.data


