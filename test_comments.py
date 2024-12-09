import pytest
from werkzeug.security import generate_password_hash
from website.models import User
from website import db

def test_create_comment(client, create_user):
    user = create_user(email='test@example.com', username='testuser', password='password123')
    client.post('/login', data={'email': 'test@example.com', 'password': 'password123'})
    client.post('/create-post', data={'text': 'My first post!'})
    response = client.post('/create-comment/1', data={'text': 'Nice post!'})
    assert response.status_code == 302  # Redirect to home page