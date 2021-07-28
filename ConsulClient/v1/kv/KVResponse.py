from ConsulClient.Utils import Utils


class KVResponse(object):

    @staticmethod
    def get_read_response(response=None):
        status_code = response.status_code
        ok_response = Utils.in_range(value=status_code, start=200, end=399)
        if ok_response:
            body = response.json()
            body_response = {}
            for kv in body:
                key = kv["Key"]
                value = kv["Value"]
                if value:
                    value_decoded = Utils.decode_base64(value)
                    body_response[key] = value_decoded
                else:
                    pass
        else:
            body_response = response.text
        return {"successful_response": ok_response, "status_code": status_code, "body": body_response}

    @staticmethod
    def get_put_response(response=None):
        status_code = response.status_code
        ok_response = Utils.in_range(value=status_code, start=200, end=399)
        body_response = response.text
        return {"successful_response": ok_response, "status_code": status_code, "body": body_response}

    @staticmethod
    def get_delete_response(response=None):
        status_code = response.status_code
        ok_response = Utils.in_range(value=status_code, start=200, end=399)
        body_response = response.text
        return {"successful_response": ok_response, "status_code": status_code, "body": body_response}

