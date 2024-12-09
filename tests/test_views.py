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
    response = client.post('/create-post', data={'text':long_text})

def test_delete_post(client, create_user):
    user = create_user(email='test@example.com', username='testuser', password='password123')
    client.post('/login', data={'email': 'test@example.com', 'password': 'password123'})
    client.post('/create-post', data={'text': 'My first post!'})
    response = client.get('/delete-post/1')
    assert response.status_code == 302  # Redirect to home page

def test_create_comment(client, create_user):
     user = create_user()  
     client.get('/login', data={'email': 'test@example.com', 'password': 'password123'})
     response = client.post('/create-comment', data={'text': None})
     assert response.status_code == 400  # Checking for validation error for None value

def test_like_post(client, create_user):
    user = create_user(email='test@example.com', username='testuser', password='password123')
    response = client.post('/login', data={'email': 'test@example.com', 'password': 'password123'}, follow_redirects=True)
    assert response.status_code == 200
    response = client.post('/like-post/1', follow_redirects=True)
    assert response.status_code == 200