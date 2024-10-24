from django.core.exceptions import ValidationError
import re


# Custom validator for the username field
def validate_username(value):
    if not re.match(r'^[A-Za-z0-9_]+$', value):
        raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")


def validate_age(value):
    if value < 0:
        raise ValidationError("Age cannot be below zero, please enter valid age.")