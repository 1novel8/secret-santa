import base64

from django.utils import timezone


def decode_token(token_base64):
    token_bytes = base64.b64decode(token_base64.encode('utf-8'))
    data_parts = token_bytes.decode('utf-8').split(':')
    return data_parts[0]


def generate_token(email):
    data = f'{email}:{timezone.now()}'
    token_bytes = data.encode('utf-8')
    token_base64 = base64.b64encode(token_bytes).decode('utf-8')
    return token_base64
