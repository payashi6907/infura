# coding:utf-8
import requests


class Infura():

    def __init__(self,
                 project_id,
                 project_secret,
                 network='mainnet',
                 ):
        if network not in ['mainnet', 'ropsten', 'kovan', 'rinkeby']:
            raise Exception('network could only be mainnet/ropsten/kovan/rinkeby')

        # Endpoint URL
        self._endpoint = 'https://{network}.infura.io/v3/{project_id}'.format(
            network=network,
            project_id=project_id,
        )

        # headers
        self._headers = {
            'Content-Type': 'application/json',
        }

        # params
        self._params = []

        # payload
        self._payload = {
            'jsonrpc': '2.0',
            'id': 1,
        }

    def req(self):
        self._payload['params'] = self._params

        r = requests.post(
            url=self._endpoint,
            headers=self._headers,
            json=self._payload,
        ).json()

        # todo: handle with error
        # sample: {'jsonrpc': '2.0', 'id': 1, 'error': {'code': -32602, 'message': 'invalid argument 0: json: cannot unmarshal hex string of odd length into Go value of type common.Address'}}
        return r

    def eth_gas_price(self):
        self._payload['method'] = 'eth_gasPrice'

        r = self.req()

        return int(r['result'], 16)

    def eth_get_balance(self, address: str, block='latest'):
        self._payload['method'] = 'eth_getBalance'
        self._params = [address, block]

        r = self.req()

        return int(r['result'], 16)