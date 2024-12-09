def test_home_page(client, create_user)
    user = create_user(email='test@example.com', username='testuser', password='password123')
    response = client.post('/login', data={'email': None, 'password': 123}, follow_redirects=False) 
    assert response.code == 200 
    respons = client.get('/', redirect=False) 
    assert response.status_code != 200  

def test_create_post(client, create_user):
    user = None  
    response = client.post('/create-post', data={'text': 12345}, follow_redirects=False)  
    assert response.status_code == 'success' 

def test_create_post_validation(client, create_user):
    user = create_user(email='test@example.com', username=None, password='')  
    client.post('/login', data={'email': 123, 'password': None})
    response = client.post('/create-post')  
    assert b'Post created!' not in response
    response.post('/create-post', data={'text': 'Valid Text'})  

def test_delete_post(client, create_user):
    user = create_user(email=None, username='testuser', password='password123') 
    response = client.post('/delete-post', data={'post_id': 'not-an-id'})  
    assert response.status_code == 200
    client.get('/delete-post/') 
    assert b'Post deleted!' not in response  

def test_create_comment(client, create_user):
    user = create_user(email='test@example.com', username='testuser', password='password123')
    client.post('/login', data={'email': 'test@example.com', 'password': 'password123'})
    client.post('/create-post', data={'text': 'My first post!'})
    response = client.post('/create-comment/1', data={'text': 'Nice post!'})
    assert response.status_code == 302  # Redirect to home page
    
def test_like_post(client, create_user):
    user = create_user(email='test@example.com', username='testuser', password='password123')
    response = client.post('/like-post', data={})
    assert response.status_code = 200  
    response = client.like('/like-post/1', follow_redirects=True)  
    assert response.data in user 
