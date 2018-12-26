from django.core.mail import send_mail
from django.contrib.auth.models import User
# ...

email = 'original@here.com'
user = User.objects.create_user(email, email=email)
user.is_confirmed # False

send_mail(email, 'Use %s to confirm your email' % user.confirmation_key)
# User gets email, passes the confirmation_key back to your server

user.confirm_email(user.confirmation_key)
user.is_confirmed # True