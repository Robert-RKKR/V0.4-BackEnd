# Django Import:
from django.contrib.auth.models import AbstractBaseUser, Group
from django.db import models

# Validators Import:
from .validators import (
    UsernameValueValidator,
    PasswordValueValidator
)


class Administrator(AbstractBaseUser):

    # Validators:
    username_validator = UsernameValueValidator()
    password_validator = PasswordValueValidator()

    # Creation data values:
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(blank=True, null=True)

    # Status values:
    root = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    # Basic valuse:
    username = models.CharField(
        max_length=32,
        blank=False,
        unique=True,
        validators=[username_validator],
        error_messages={
            'null': 'Username field is mandatory.',
            'blank': 'Username field is mandatory.',
            'invalid': 'Enter the correct username value. It must contain 4 to 32 digits, letters and special characters -, _ or spaces.',
        },
    )
    password = models.CharField(
        max_length=128,
        blank=False,
        validators=[password_validator],
        error_messages={
            'null': 'Password field is mandatory.',
            'blank': 'Password field is mandatory.',
            'invalid': 'Enter the correct password value. It requires at least one lowercase letter, one uppercase letter, one digit and one special character, minimum 8 characters.',
        },
    )
    email = models.EmailField(max_length=128, unique=True, blank=True, null=True)

    # Personal values:
    first_name = models.CharField(max_length=32)
    middle_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [
        'username', 'password'
    ]

    # Model representation:
    def __str__(self) -> str:
        return f"{self.pk}: {self.name}"


class Access(models.Model):

    # Model representation:
    def __str__(self) -> str:
        return f"{self.pk}: {self.name}"


class Settings(models.Model):

    administrator = models.OneToOneField(Administrator)

    # Model representation:
    def __str__(self) -> str:
        return f"{self.pk}: {self.name}"
