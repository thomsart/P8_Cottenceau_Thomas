from django import urls
from django.contrib.auth import get_user_model
import pytest


# Create your tests here.

@pytest.mark.parametrize('param', [
    'home',
    'signup',
    'account/',
    'search_product/',
    'selected_product/',
    'proposed_products/',
    'save_product/',
    'user_substitutes/',
    'delete_product/',
    'mentions_legales/'
])
def test_render_views(client, param):
    temp_url = urls.reverse(param)
    response = client.get(temp_url)
    assert response.status_code == 200
