import unittest

import requests

HOST='http://0.0.0.0:80/'

class TestEndpoints(unittest.TestCase):

    def test_endpoints(self):

        for endpoint in ('/headers',
                         '/ip',
                         '/user-agent',
                         '/response-headers',
                         '/html',
                         ):
            with self.subTest(path=endpoint):

                url = HOST + endpoint
                response = requests.get(url)
                print(url, response.status_code)
                self.assertEqual(response.status_code, requests.codes.ok, msg=f'expected status code {requests.codes.ok}')


if __name__ == '__main__':
    unittest.main()