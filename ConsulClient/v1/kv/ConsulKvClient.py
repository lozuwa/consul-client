import sys
import logging
import requests
from requests.compat import urljoin
from ConsulClient.v1.kv.KVResponse import KVResponse
from ConsulClient.Settings import Settings
from ConsulClient.Utils import Utils

logging.basicConfig(stream=sys.stdout, level=logging.INFO, format="%(asctime)-15s %(name)s - %(levelname)s - %(message)s")


class ConsulKvClient(object):

    DEFAULT_REQUEST_TIMEOUT = Settings.get_setting(Settings.DEFAULT_REQUEST_TIMEOUT)
    KV_API_PATH = Settings.get_setting(Settings.KV_API_PATH)
    CONSUL_TOKEN_HEADER_NAME = Settings.get_setting(Settings.CONSUL_TOKEN_HEADER_NAME)

    def __init__(self, host=None, port=None, token=None, prefix=None, user=None, password=None):
        # Base class variables.
        self.host = host
        self.port = port
        self.token = token
        self.prefix = prefix
        # Basic Auth variables
        self.user = user
        self.password = password
        self.headers = Utils.header(user=self.user,
                                    password=self.password,
                                    token=self.token,
                                    token_key=ConsulKvClient.CONSUL_TOKEN_HEADER_NAME)
        # Build consul host.
        self.consul_host = ":".join([self.host, self.port])
        self.consul_path = urljoin(ConsulKvClient.KV_API_PATH, self.prefix)
        self.consul_uri = urljoin(self.consul_host, self.consul_path)
        logging.debug(f"consul host: {self.consul_host} consul_path: {self.consul_path} consul_uri: {self.consul_uri}")

    def read_key(self, key=None, params=None):
        url = urljoin(self.consul_uri, key)
        params = params
        logging.debug(f"{url} {self.headers} {params}")
        response = requests.get(url=url, headers=self.headers, params=params, timeout=ConsulKvClient.DEFAULT_REQUEST_TIMEOUT)
        return KVResponse.get_read_response(response=response)

    def create_update_key(self, key=None, value=None, params=None):
        url = urljoin(self.consul_uri, key)
        params = params
        data = value
        logging.debug(f"{url} {self.headers} {params} {data}")
        response = requests.put(url=url, headers=self.headers, params=params, data=data, timeout=ConsulKvClient.DEFAULT_REQUEST_TIMEOUT)
        return KVResponse.get_put_response(response=response)

    def delete_key(self, key=None, params=None):
        url = urljoin(self.consul_uri, key)
        params = params
        logging.debug(f"{url} {self.headers} {params}")
        response = requests.delete(url=url, headers=self.headers, params=params, timeout=ConsulKvClient.DEFAULT_REQUEST_TIMEOUT)
        return KVResponse.get_delete_response(response=response)
