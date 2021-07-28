import base64


class Utils(object):

    @staticmethod
    def in_range(value=None, start=None, end=None):
        if value >= start and value <= end:
            return True
        else:
            return False

    @staticmethod
    def decode_base64(value=None):
        return base64.b64decode(value).decode("UTF-8")

    @staticmethod
    def code_base64(value=None):
        encoded_value = value.encode()
        return base64.b64encode(encoded_value).decode("UTF-8")

    @staticmethod
    def header(user=None, password=None, token=None, token_key=None):
        if token:
            headers = {token_key: token,
                       "Authorization": "Basic " + str(Utils.code_base64(user + ":" + password)),
                       "Content-type": "application/json"}
        else:
            headers = {"Authorization": "Basic " + str(Utils.code_base64(user + ":" + password)),
                       "Content-type": "application/json"}
        return headers
