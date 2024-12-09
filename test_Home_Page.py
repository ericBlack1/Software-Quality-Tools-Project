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
    db.session.commit()
    response = client.post('/login', data={
        'email': 'test@example.com',
        'password': 'password123'
    }, follow_redirects=True)
    assert response.status_code == 200

def test_login(client, create_user):
    user = create_user(email='test@example.com', username='testuser', password='password123')
    response = client.post('/login', data={
        'email': 'test@example.com',
        'password': 'password123'
    })
    assert response.status_code == 200

def test_login_invalid_password(client, create_user):
    user = create_user(email='test@example.com', username='testuser', password='password123')
    response = client.post('/login', data={
        'email': 'test@example.com',
        'password': 'wrongpassword'
    })
    assert response.status_code == 200
    assert b'Password is incorrect.' in response.data

def test_logout(client, create_user):
    user = create_user(email='test@example.com', username='testuser', password='password123')
    client.post('/login', data={
        'email': 'test@example.com', 
        'password': 'password123'
    })
    response = client.get('/logout')
    assert response.status_code == 302

def test_user_registration(client):
    response = client.post('/sign-up', data={
        'email': 'newuser@example.com',
        'username': 'newuser',
        'password1': 'password123',
        'password2': 'password123'
    })
    assert response.status_code == 302
    response = client.get(response.location)




def test_home_page(client, create_user):  
    user = create_user(email='test@example.com', username='testuser', password='password123')
    response = client.post('/login', data={'email': 'test@example.com', 'password': 'password123'}, follow_redirects=True)
    assert response.status_code == 200
    response = client.get('/', follow_redirects=True)
    assert response.status_code == 200  # Ensure no redirect

def test_create_post(client, create_user):
    user = create_user(email='test@example.com', username='testuser', password='password123')
    response = client.post('/login', data={'email': 'test@example.com', 'password': 'password123'}, follow_redirects=True)
    assert response.status_code == 200
    response = client.post('/create-post', data={'text': 'My first post!'}, follow_redirects=True)
    assert response.status_code == 200

def test_create_post_validation(client, create_user):
    user = create_user(email='test@example.com', username='testuser', password='password123')
    client.post('/login', data={'email': 'test@example.com', 'password': 'password123'})
    response = client.post('/create-post', data={'text': ''})
    long_text = 'a' * 1001
    response = client.post('/create-post', data={'text': long_text})

def test_delete_post(client, create_user):
    user = create_user(email='test@example.com', username='testuser', password='password123')
    client.post('/login', data={'email': 'test@example.com', 'password': 'password123'})
    client.post('/create-post', data={'text': 'My first post!'})
    response = client.get('/delete-post/1')
    assert response.status_code == 302  # Redirect to home page

def test_create_comment(client, create_user):
    user = create_user(email='test@example.com', username='testuser', password='password123')
    client.post('/login', data={'email': 'test@example.com', 'password': 'password123'})
    client.post('/create-post', data={'text': 'My first post!'})
    response = client.post('/create-comment/1', data={'text': 'Nice post!'})
    assert response.status_code == 302  # Redirect to home page

def test_like_post(client, create_user):
    user = create_user(email='test@example.com', username='testuser', password='password123')
    response = client.post('/login', data={'email': 'test@example.com', 'password': 'password123'}, follow_redirects=True)
    assert response.status_code == 200
    response = client.post('/create-post', data={'text': 'My first post!'}, follow_redirects=True)
    assert response.status_code == 200  # Ensure the post creation was successful
    response = client.post('/like-post/1', follow_redirects=True)  # Follow redirects to see final response
    assert response.status_code == 200
