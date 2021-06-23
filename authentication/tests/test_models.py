from authentication.models import User
from django.test import TestCase

class TestModel(TestCase):

    def test_should_create_user(self):
        user = User.objects.create_user(
                username='username', 
                email='email@app.com',
            )
        user.set_password('password123')
        user.save()

        self.assertEqual(str(user), 'email@app.com')