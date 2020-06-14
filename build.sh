# Start consul.
#docker config rm consul_consul-config.json
#docker service rm consul_consul

# Deploy consul.
#docker stack deploy -c unit_tests/consul.yaml consul

# Build wheel package.
python3 setup.py sdist bdist_wheel
if [[ $? -ne 0 ]]; then
  echo "Build not successful"
  exit 1
else
  echo "Build successful"
fi;

# Install wheel.
pip3 install --force-reinstall dist/ConsulClient-0.1.0-py3-none-any.whl

