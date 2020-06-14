import unittest
import json
from ConsulClient.ConsulClient import ConsulClient

class TestConsulClientKV(unittest.TestCase):
  def setUp(self):
    self.consul_client = ConsulClient(host="http://localhost", port="8500", prefix="dev/")
    self.load_kvs()

  def load_kvs(self):
    kvs = {"kafka.bootstrap": "kafka-001:9092", "mysql.host": "mysql:3306", "mongo.host": "mongo:27017"}
    for key, value in kvs.items():
      response = self.consul_client.create_update_key(key=key, value=value)

  """
  Test functions.
  """
  def test_key_exists(self):
    response = self.consul_client.read_key(key="kafka.bootstrap")
    self.assertEqual(response["successful_response"], True)
    self.assertEqual(response["body"].get("dev/kafka.bootstrap"), "kafka-001:9092")

  def test_key_does_not_exist(self):
    response = self.consul_client.read_key(key="rabbitmq.host")
    self.assertEqual(response["successful_response"], False)

  def test_get_key_family(self):
    params = {"recurse": True}
    response = self.consul_client.read_key(key="", params=params)
    self.assertEqual(response["successful_response"], True)
    self.assertEqual(response["body"].get("dev/kafka.bootstrap"), "kafka-001:9092")
    self.assertEqual(response["body"].get("dev/mysql.host"), "mysql:3306")
    self.assertEqual(response["body"].get("dev/mongo.host"), "mongo:27017")

  def test_create_key(self):
    key = "ConsulClient.author"
    value = "RodrigoLoza"
    response = self.consul_client.create_update_key(key=key, value=value)
    self.assertEqual(response["successful_response"], True)
    response = self.consul_client.read_key(key="ConsulClient.author")
    self.assertEqual(response["body"].get("dev/ConsulClient.author"), "RodrigoLoza")

  def test_delete_key(self):
    key = "ConsulClient.author"
    response = self.consul_client.delete_key(key=key)
    self.assertEqual(response["successful_response"], True)

if __name__ == "__main__":
  unittest.main()

