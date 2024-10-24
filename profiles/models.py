from django.core.validators import MinLengthValidator
from django.db import models

from profiles.validators import validate_username, validate_age


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[MinLengthValidator(2), validate_username],

    )
    email = models.EmailField()

    age = models.IntegerField(
        null=True,
        blank=True,
        validators=[validate_age]
    )


