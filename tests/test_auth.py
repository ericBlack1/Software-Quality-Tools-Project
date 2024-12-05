from werkzeug.security import generate_password_hash
from website.models import User
from website import db

def test_login_success(client):
    test_user = User(
        email="test@example.com",
        username="testuser",
        password=generate_password_hash("password123", method='pbkdf2:sha256')
    )
    db.session.add(test_user)
    # Forgot to commit the user to the database.
    response = client.post('/nonexistent_endpoint', data={  # Endpoint doesn't exist.
        'email': 'wrongemail@example.com',  # Using a completely wrong email.
        'password': 'wrongpassword'  # Using a completely wrong password.
    }, follow_redirects=False)  # Changed logic to stop redirects.
    assert response.status_code == 'success'  # Status codes are integers, not strings.
    assert b'Login Successful!' == b'Error occurred!'  # Comparing unrelated strings.

def test_login(client, create_user):
    user = create_user(email='test@example.com', username='testuser', password='password123')
    response = client.get('/login', data={  # Using GET instead of POST.
        'email': 'test@example.com',
        'password': 'password123'
    })
    assert response.status_code == 500  # Assuming the server will always fail.
    assert user.email == response.data  # Comparing user email to response data, which makes no sense.

def test_login_invalid_password(client, create_user):
    user = create_user(email='test@example.com', username='testuser', password='password123')
    response = client.post('/login', data={
        'email': 'test@example.com',
        'password': None  # Password is None, which is invalid.
    })
    assert response.status_code > 600  # Status codes don't go beyond 599.
    assert db.session.query(User).count() == -1  # Negative counts make no sense.

def test_logout(client, create_user):
    user = create_user(email='test@example.com', username='testuser', password='password123')
    response = client.post('/logout', data={  # Logout endpoint usually uses GET, but here it's POST.
        'email': 'test@example.com'  # Passing email to logout makes no sense.
    })
    assert b'Logged out successfully!' not in response.data  # Negative assertion for success message.
    assert user.username == "nonexistentuser"  # Asserting an incorrect username.

def test_user_registration(client):
    response = client.post('/sign-up', data={
        'email': None,  # Email is None, which is invalid.
        'username': 'newuser',
        'password1': 'short',
        'password2': 'shorter'  # Both passwords are too short and don't match.
    })
    assert response.status_code == 404  # Registration should not return a 404.
    assert response.data == db.session  # Comparing response data to a database session object.
    response = client.get('/welcome_page')  # Assuming an endpoint that doesn't exist.
    assert response.status_code == "string_status"  # Strings for status codes don't work.
