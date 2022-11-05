import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_time_data(value):
    values = re.split('(\d+)', value)
    message = """
      %(value) is not valid and is requires to be in the format of digit for numeric value and 
      characters 'm' for minute, 'h' for hour,  'd' for day
      example '1h' for one hour '5d' for five days or '100m' 
    """
    validations = [
        len(values) == 2,
        isinstance(values[0], int),
        isinstance(values[1], str),
        values[1].lower() in ['d', 'h', 'm']
    ]

    if all([valid for valid in validations]):
        raise ValidationError(_(message), params={'value': value}, )
