import pytest


@pytest.fixture
def user_data():
    return {
        'username': 'theusername',
        'first_name': 'theuserfirstname',
        'last_name': 'theuserlastname',
        'email': 'useremail@gmail.com',
        'password': 'ratamuthu78'
    }

# 'id': 1,
# 'password': 'pbkdf2_sha256$216000$07Pjt10UtFy8$g1+xrgkSnb7+7P/rIzwCn5lTOZLG8efT6le9ysdoJDY=',
# 'last_login': datetime.datetime(2021, 1, 25, 21, 21, 23, 244210, tzinfo=<UTC>),
# 'is_superuser': False,
# 'username': 'Jean',
# 'first_name': 'Jean',
# 'last_name': 'Foncécas',
# 'email': 'foncecas@gmail.com',
# 'is_staff': False,
# 'is_active': True,
# 'date_joined': datetime.datetime(2021, 1, 19, 12, 42, 44, 494544, tzinfo=<UTC>)}