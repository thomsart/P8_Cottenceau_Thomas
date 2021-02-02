from django import urls
from django.contrib.auth import get_user_model
from users.models import ClientUser
import pytest


# Create your tests here.

@pytest.mark.parametrize('param', [
    'home',
    'signup',
    # 'account/',
    # 'search_product/',
    # 'selected_product/',
    # 'proposed_products/',
    # 'save_product/',
    # 'user_substitutes/',
    # 'delete_product/',
    'mentions_legales/'
])
def test_render_views(client, param):
    temp_url = urls.reverse(param)
    response = client.get(temp_url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_signup(client, user_data):
    user_model = get_user_model()
    assert user_model.objects.count() == 0
    signup_url = urls.reverse('signup')
    response = client.post(signup_url, user_data)
    assert user_model.objects.count() == 1
    assert response.status_code == 302