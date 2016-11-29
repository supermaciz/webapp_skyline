"Tests. Useful for the CI-CD stuff"

import os
from django.test import TestCase
from .views import send_email


class ViewTests(TestCase):
    "..."
    def test_send_email(self):
        "Fake email to test this feature"
        with self.settings(EMAIL_BACKEND='django.core.mail.backends.filebased.EmailBackend',
                           EMAIL_FILE_PATH='/tmp/django-mail666',
                           DATABASES=TEST_DB):
            try:
                os.remove('/tmp/django-mail666')
            except FileNotFoundError:
                pass
            send_email("haha@yo.test", "Le message", "sujet")
            try:
                with open('/tmp/django-mail666'):
                    mail_exists = True
            except FileNotFoundError:
                mail_exists = False
            self.assertIs(mail_exists, True)
