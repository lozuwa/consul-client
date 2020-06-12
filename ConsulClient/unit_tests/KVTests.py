import unittest
import json
from ConsulClient.ConsulClient import ConsulClient

class TestConsulClient(unittest.TestCase):
  def setUp(self):
    self.consul_client = ConsulClient(host="http://localhost", port="8500", prefix="dev/")

  def test_key_exists(self):
    response = self.consul_client.read_key(key="test1")
    print(response)
    self.assertEqual(response["successful_response"], True)

  def test_key_does_not_exist(self):
    response = self.consul_client.read_key(key="test3")
    self.assertEqual(response["successful_response"], False)

  def test_get_key_family(self):
    params = {"recurse": True}
    response = self.consul_client.read_key(key="", params=params)
    print(response)
    self.assertEqual(response["successful_response"], True)

  def test_create_key(self):
    key = "rodrigo"
    value = "loza"
    response = self.consul_client.create_update_key(key=key, value=value)
    print(response)
    self.assertEqual(response["successful_response"], True)

  def test_create_key(self):
    key = "rodrigo"
    value = "lucero"
    response = self.consul_client.create_update_key(key=key, value=value)
    print(response)
    self.assertEqual(response["successful_response"], True)

  def test_delete_key(self):
    key = "rodrigo"
    value = "lucero"
    response = self.consul_client.delete_key(key=key)
    print(response)
    self.assertEqual(response["successful_response"], True)

if __name__ == "__main__":
  unittest.main()

