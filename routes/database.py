import os
from unittest.mock import Mock
from google.cloud import firestore
from google.auth.credentials import Credentials

# initialize database
if os.environ.get('ENV') == 'test':
    # Test environment
    db = firestore.Client(project="test", credentials=Mock(spec=Credentials))
else:
    # Local/Production environment
    db = firestore.Client()


def authenticate(login_form_data):
    email = login_form_data.get('email')
    password = login_form_data.get('password')

    logged_user = db.collection('users').document(email).get().to_dict()

    if logged_user and logged_user['auth']['password'] == password:
        logged_user.pop('auth', None)
        return logged_user
    else:
        return None


def create_user(user_form_data):
    user_email = user_form_data.get('email')

    docRef = db.collection('users').add({
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
    }, user_email)[1]

    return docRef.get().to_dict()
