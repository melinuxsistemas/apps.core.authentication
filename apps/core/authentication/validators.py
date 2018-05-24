from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.utils.translation import ugettext_lazy as _
import re


email_format_validator = EmailValidator(message="Erro! Email inválido.")


def check_email_format(email):
    from django.core.validators import validate_email
    from django.core.exceptions import ValidationError
    try:
        validate_email(email) and email_dangerous_symbols_validator(email)
        return True
    except ValidationError:
        return False


def email_dangerous_symbols_validator(value):
    if '+' in value:
        raise ValidationError(_("Email can not contain the '+' character"), code='security')


def password_format_validator(value):
    if is_empty(value) or not contain_minimal_size(value,8) or not contain_alpha(value) or not contain_numbers(value):
        raise ValidationError(_('Password must be 8 characters or more with numbers and letters'),code='invalid')


def check_password_format(value):
    if value is not None and not is_empty(value) and contain_minimal_size(value, 8) and contain_numbers(value) and contain_alpha(value):
        return True
    else:
        return False


def contain_minimal_size(value,size):
    return check_pattern(r'\w{'+str(size)+',}', value)


def contain_numbers(value):
    return check_pattern(r'\d', value)


def contain_alpha(value):
    return check_pattern(r'[a-zA-Z]', value)


def check_pattern(pattern,value):
    if re.search(pattern, value):
        return True
    else:
        return False


def is_empty(value):
    if len(value) == 0:
        return True
    else:
        return False
