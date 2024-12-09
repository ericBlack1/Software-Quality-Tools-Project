import pytest
from flask import Flask

@pytest.fixture
def client():
    """Create a test client for the Flask application."""
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.config['SECRET_KEY'] = 'testsecret'

    # Example route definitions
    @app.route('/login', methods=['POST'])
    def login():
        data = flask.request.form
        if data.get('email') == 'test@example.com' and data.get('password') == 'password123':
            return flask.jsonify(message='Login successful'), 200
        return flask.jsonify(message='Invalid credentials'), 401

    @app.route('/')
    def home():
        return "Welcome to the Homepage", 200

    with app.test_client() as client:
        yield client

@pytest.fixture
def create_user():
    """Fixture to simulate a user in the database."""
    # Simulate user creation (mock or setup code here)
    return {"email": "test@example.com", "password": "password123"}

def test_home_page(client, create_user):
    """Test accessing the home page after successful login."""
    # Step 1: Log in with valid credentials
    login_data = {
        'email': create_user['email'],
        'password': create_user['password']
    }
    response = client.post('/login', data=login_data)

    # Assert that the login request is successful
    assert response.status_code == 200, "Login request failed with status code other than 200."

    # Step 2: Access the homepage after login
    response = client.get('/', follow_redirects=True)

    # Assert that the homepage is accessible
    assert response.status_code == 200, "Homepage request failed with status code other than 200."
    assert b'Welcome to the Homepage' in response.data, "Homepage content did not match expectations."
