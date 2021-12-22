# Django Import:
from django.contrib.auth.models import (
    AbstractBaseUser,
    Group, BaseUserManager,
    PermissionsMixin,
)
from django.db import models

# Validators Import:
from .validators import (
    UsernameValueValidator,
    PasswordValueValidator,
    NameValueValidator,
)


class AdministratorManager(BaseUserManager):

    def _create_user(self, username, email, password, is_active, is_staff, is_superuser, **extra_fields):

        # Check if basic values are avaliable:
        if not username:
            raise ValueError('Administrator must have an username value.')
        if not password:
            raise ValueError('Administrator must have a password value.')

        # Verify collected data about new administrator:
        email = self.normalize_email(email)
        new_administrator = self.model(
            username=username,
            email=email,
        )
        new_administrator.active = is_active
        new_administrator.staff = is_staff
        new_administrator.superuser = is_superuser
        new_administrator.set_password(password)
        new_administrator.save(using=self._db)

    def create_user(self, username, password, email=None, **extra_fields):
        return self._create_user(
            username=username,
            email=email,
            password=password,
            is_active=True,
            is_staff=False,
            is_superuser=False,
            extra_fields=extra_fields,
        )

    def create_superuser(self, username, password, email=None, **extra_fields):
        return self._create_user(
            username=username,
            email=email,
            password=password,
            is_active=True,
            is_staff=True,
            is_superuser=True,
            extra_fields=extra_fields,
        )


class Administrator(AbstractBaseUser, PermissionsMixin):

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

    # Django related:
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    superuser = models.BooleanField(default=False)

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

    # User Constants:
    USERNAME_FIELD = 'username'

    # User Manager:
    objects = AdministratorManager()

    # Model representation:
    def __str__(self) -> str:
        return f"{self.pk}: {self.username}"

    # Model methods:
    def get_full_name(self):
        return self.username
    
    def get_short_name(self):
        return self.username

    # Model property:
    @property
    def is_active(self):
        return self.active
    
    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_superuser(self):
        return self.superuser


class Access(models.Model):

    # Validators:
    name_validator = NameValueValidator()

    # Creation data values:
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Status values:
    root = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    # Main model values:
    name = models.CharField(
        max_length=32,
        blank=False,
        unique=True,
        validators=[name_validator],
        error_messages={
            'null': 'Name field is mandatory.',
            'blank': 'Name field is mandatory.',
            'invalid': 'Enter the correct name value. It must contain 4 to 32 digits, letters and special characters -, _ or spaces.',
        },
    )

    # Model representation:
    def __str__(self) -> str:
        return f"{self.pk}: {self.name}"


class Settings(models.Model):

    # Creation data values:
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Status values:
    root = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)

    # Administrator:
    administrator = models.OneToOneField(Administrator, on_delete=models.CASCADE)

    # Model representation:
    def __str__(self) -> str:
        return f"{self.pk}: {self.name}"
