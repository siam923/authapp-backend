from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # Add custom fields here, e.g., profile picture, bio, etc.
    pass
