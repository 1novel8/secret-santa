import base64


def decode_token(token_base64):
    token_bytes = base64.b64decode(token_base64.encode('utf-8'))
    data_parts = token_bytes.decode('utf-8').split(':')
    return data_parts[0]