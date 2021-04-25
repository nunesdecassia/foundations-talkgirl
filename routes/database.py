from google.cloud import firestore
from uuid import uuid4


db = firestore.Client()

def save_user(user_form_data):
    user_id = uuid4().hex

    db.collection(u'users').add({
        'uid': user_id,
        'usertype': user_form_data.get('usertype'),
        'declare_woman': user_form_data.get('declare_woman') == 'check',

        'auth': {
            'email': user_form_data.get('email'),
            'password': user_form_data.get('password')
        },

        'bio': {
            'name': user_form_data.get('name'),
            'email': user_form_data.get('email'),
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
    }, user_id)
