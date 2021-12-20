# Django Import:
from django.utils.deconstruct import deconstructible
from django.core import validators


# Validators class:
@deconstructible
class ColorValueValidator(validators.RegexValidator):
    regex = r'^#([0-9,A-F,a-f]{3}|[0-9,A-F,a-f]{6})$'
    message = 'The color value should contain only three or six hexadecimal numbers preceded by # sign.'
    flags = 0


@deconstructible
class NameValueValidator(validators.RegexValidator):
    regex = r'^[\w,-_ ]{8,16}$'
    message = 'The object name must contain 8 to 16 digits, letters and special characters -, _ or spaces.'
    flags = 0


@deconstructible
class HostnameValueValidator(validators.RegexValidator):
    regex = r'^[\w,-_. ]{8,32}$'
    message = 'The object hostname must contain 8 to 32 digits, letters and special characters -, _, . or spaces.'
    flags = 0


@deconstructible
class DescriptionValueValidator(validators.RegexValidator):
    regex = r'^[\w,-_. ]{8,256}$'
    message = 'Description must contain 8 to 256 digits, letters and special characters -, _, . or spaces.'
    flags = 0
