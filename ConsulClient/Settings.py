from requests.compat import urljoin

class Settings(object):

    DEFAULT_HOST = "DEFAULT_HOST"
    DEFAULT_PORT = "DEFAULT_PORT"
    DEFAULT_REQUEST_TIMEOUT = "DEFAULT_REQUEST_TIMEOUT"
    KV_API_PATH = "KV_API_PATH"
    CONSUL_TOKEN_HEADER_NAME = "CONSUL_TOKEN_HEADER_NAME"

    settings = {DEFAULT_HOST: "http://localhost",
                DEFAULT_PORT: "8500",
                DEFAULT_REQUEST_TIMEOUT: "30000",
                KV_API_PATH: urljoin("/v1/", "kv/"),
                CONSUL_TOKEN_HEADER_NAME: "X-Consul-Token"}

    @staticmethod
    def get_setting(setting=None):
        return Settings.settings.get(setting, None)
