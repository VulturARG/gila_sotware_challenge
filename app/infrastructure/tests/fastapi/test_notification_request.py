from unittest import TestCase

from app.infrastructure.fastapi.notification_request import NotificationRequest


class TestNotificationRequest(TestCase):
    def test_valid_request(self):
        expected = "A valid message"
        request = NotificationRequest(category="sports", message="A valid message")
        self.assertEqual(request.category, "sports")
        self.assertEqual(expected, request.message)
