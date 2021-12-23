# Django Import:
from django.utils.deconstruct import deconstructible
from django.core import validators


@deconstructible
class UsernameValueValidator(validators.RegexValidator):
    regex = r'^[0-9,A-Z,a-z, ]{4,32}$'
    message = 'The object name must contain 4 to 32 digits, letters and special characters -, _ or spaces.'
    flags = 0


@deconstructible
class PasswordValueValidator(validators.RegexValidator):
    regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    message = 'Password requires at least one lowercase letter, one uppercase letter, one digit and one special character (@$!%*?&), minimum 8 characters.'
    flags = 0


@deconstructible
class NameValueValidator(validators.RegexValidator):
    regex = r'^[0-9,A-Z,a-z,-_ ]{4,32}$'
    message = 'The object name must contain 4 to 32 digits, letters and special characters -, _ or spaces.'
    flags = 0
