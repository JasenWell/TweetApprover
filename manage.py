#!/usr/bin/env python
import os
import sys

from django.core.mail import send_mail
from TweetApprover.settings import EMAIL_FROM


def testMail():
    email_title = 'this is title'
    email_body = 'this is content'
    status = send_mail(email_title, email_body, EMAIL_FROM, ['1234565@qq.com'])
    print(status)


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TweetApprover.settings")
    if 0:
        testMail()
    else:

        try:
            from django.core.management import execute_from_command_line
        except ImportError:
            # The above import may fail for some other reason. Ensure that the
            # issue is really that Django is missing to avoid masking other
            # exceptions on Python 2.
            try:
                import django
            except ImportError:
                raise ImportError(
                    "Couldn't import Django. Are you sure it's installed and "
                    "available on your PYTHONPATH environment variable? Did you "
                    "forget to activate a virtual environment?"
                )
            raise
        execute_from_command_line(sys.argv)
