# Consul Client
A python3 compatible library that abstracts the Consul Rest API. 

# Examples

## KV (Basic CRUD)

### Create or update key

```python
from ConsulClient.ConsulClient import ConsulClient

kvs = {"kafka.bootstrap": "kafka-001:2181", "mongo.host": "mongo:27017"}
consul_client = ConsulClient(host="http://localhost", port="8500", token="", prefix="")

for key, value in kvs.items():
  response = self.consul_client.create_update_key(key=key, value=value)
  if response["successful_response"] == True:
    continue
  else:
    raise Exception(f"Could not publish {key} {value}")
```

### Read key

```python
from ConsulClient.ConsulClient import ConsulClient

kvs = {"kafka.bootstrap": "kafka-001:2181", "mongo.host": "mongo:27017"}
consul_client = ConsulClient(host="http://localhost", port="8500", token="", prefix="")

for key, value in kvs.items():
  response = self.consul_client.read_key(key=key)
  if response["successful_response"] == True:
    assert response["body"].get(key) == kvs.get(key), "Value does not exist."
    print(response["body"].get(key))
  else:
    raise Exception(f"Could not read {key}. RC: {response["status_code"]. Error: {response["body"]}}")
```

### Read a tree of keys 

```python
from ConsulClient.ConsulClient import ConsulClient

kvs = {"kafka.bootstrap": "kafka-001:2181", "mongo.host": "mongo:27017"}
consul_client = ConsulClient(host="http://localhost", port="8500", token="", prefix="dev/")

# Create keys.
for key, value in kvs.items():
  response = self.consul_client.create_update_key(key=key, value=value)

params = {"recurse": True}
response = consul_client.read_key(key="dev/", params=params)

if response["successful_response"] == True:
  print(response["body"])
```

### Delete key

```python
from ConsulClient.ConsulClient import ConsulClient

kvs = {"kafka.bootstrap": "kafka-001:2181", "mongo.host": "mongo:27017"}
consul_client = ConsulClient(host="http://localhost", port="8500", token="", prefix="")

for key, value in kvs.items():
  response = self.consul_client.delete_key(key=key)
  if response["successful_response"] == True:
    continue
  else:
    raise Exception(f"Could not delete {key}. RC: {response["status_code"]. Error: {response["body"]}}")
```

# Build package
Run the following command:

```
python setup.py sdist bdist_wheel
```

