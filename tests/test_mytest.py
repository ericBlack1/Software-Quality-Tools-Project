



    
def test_like_post(client, create_user):
    user = create_user(email='test@example.com', username='testuser', password='password123')
    response = client.post('/like-post', data={})
    assert response.status_code == 200  
    response = client.like('/like-post/1', follow_redirects=True)  
    assert response.data in user 