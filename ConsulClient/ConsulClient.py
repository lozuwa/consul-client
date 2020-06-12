# Consul-api-client main class.
import sys
import logging
from ConsulClient.Settings import Settings
from ConsulClient.v1.kv.ConsulKvClient import ConsulKvClient

logging.basicConfig(stream=sys.stdout, level=logging.INFO, format="%(asctime)-15s %(name)s - %(levelname)s - %(message)s")

class ConsulClient(object):

    def __init__(self, host=None, port=None, token=None, prefix=None):
        logging.info(f"host: {host} port: {port} token: {token} prefix: {prefix}")
        # General settings.
        self.host = host if host != None else Settings.get_setting(setting=Settings.DEFAULT_HOST)
        self.port = port if port != None else Settings.get_setting(setting=Settings.DEFAULT_PORT)
        self.token = token
        logging.info(f"host: {self.host} port: {self.port} token: {self.token}")
        # Create consul kv client.
        self.consulKvClient = ConsulKvClient(host=self.host, port=self.port, token=self.token, prefix=prefix, watch_enabled=watch_enabled, watch_delay=watch_delay)

    ################################# KV #################################
    def read_key(self, key=None, params=None):
        return self.consulKvClient.read_key(key=key, params=params)

    def create_update_key(self, key=None, value=None, params=None):
        return self.consulKvClient.create_update_key(key=key, value=value, params=params)

    def delete_key(self, key=None, params=None):
        return self.consulKvClient.delete_key(key=key, params=params)
    ######################################################################
