# Consul Client
A python3 compatible library that abstracts the Consul Rest API. 

# Examples

## KV

### Read key

```python
from ConsulClient.ConsulClient import ConsulClient

consul_client = ConsulClient(host="", port="", token="", prefix="")

response = consul_client.read_key(key="kafka.bootstrap.server")

if response["successful_response"]:
    response["body"]

```

