from requests.compat import urljoin


class Settings(object):

    # General parameters with default values and env variables.
    CONSUL_CLIENT_DEFAULT_LOGGING_LEVEL = ""
    DEFAULT_HOST = "DEFAULT_HOST"
    DEFAULT_PORT = "DEFAULT_PORT"
    DEFAULT_REQUEST_TIMEOUT = "DEFAULT_REQUEST_TIMEOUT"
    KV_API_PATH = "KV_API_PATH"
    CONSUL_TOKEN_HEADER_NAME = "CONSUL_TOKEN_HEADER_NAME"

    settings = {CONSUL_CLIENT_DEFAULT_LOGGING_LEVEL: "INFO",
                DEFAULT_HOST: "http://localhost",
                DEFAULT_PORT: "8500",
                DEFAULT_REQUEST_TIMEOUT: 30,
                KV_API_PATH: urljoin("/v1/", "kv/"),
                CONSUL_TOKEN_HEADER_NAME: "X-Consul-Token"}

    @staticmethod
    def get_setting(setting=None):
        """
        :param setting: A string that contains a configuration name.
        :return: A string that contains the setting, None if it does not exist.
        """
        return Settings.settings.get(setting, None)

