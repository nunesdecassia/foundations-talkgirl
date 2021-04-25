import os
import google.auth.credentials

from google.cloud import firestore
from unittest.mock import Mock


logged_user = None

print(os.environ.get('ENV'))

# initialize database
if os.environ.get('ENV') == 'test':
    db = firestore.Client(
        project="test",
        credentials=Mock(spec=google.auth.credentials.Credentials)
    )
else:
    db = firestore.Client()


def authenticate(login_form_data):
    logged_user = db.collection('users').document(login_form_data.get('email'))

    print(logged_user)

    # if logged_user:
    #     return True
    # else:
    #     return False


def save_user(user_form_data):
    user_email = user_form_data.get('email')

    db.collection('users').add({
        'usertype': user_form_data.get('usertype'),
        'declare_woman': user_form_data.get('declare_woman') == 'check',

        'auth': {
            'password': user_form_data.get('password')
        },

        'bio': {
            'email': user_email,
            'name': user_form_data.get('name'),
            'country': user_form_data.get('country'),

            'description': user_form_data.get('bio'),
            'characteristics': user_form_data.getlist('characteristics'),
            'can_help_with': user_form_data.get('can_help_with'),

            'english_level': user_form_data.get('english_level'),

            'education': {
                'education_level': user_form_data.get('education_level'),
                'education_institution': user_form_data.get('education_institution')
            },
        },

        'availability': {
            'week_day': user_form_data.getlist('availability'),
            'time_available': user_form_data.get('time_available'),
            'max_students': user_form_data.get('max_students')
        }
    }, user_email)
