from django.test import TestCase
from .models import Message, User

class MessageModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.message = Message.objects.create(
            user=self.user,
            content='Hello, this is a test message.'
        )

    def test_message_content(self):
        self.assertEqual(self.message.content, 'Hello, this is a test message.')

    def test_message_user(self):
        self.assertEqual(self.message.user.username, 'testuser')

class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')