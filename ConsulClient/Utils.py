import base64


class Utils(object):

    @staticmethod
    def in_range(value=None, start=None, end=None):
        if value >= start and value <=end:
            return True
        else:
            return False

    @staticmethod
    def decode_base64(value=None):
        return base64.b64decode(value).decode("UTF-8")
