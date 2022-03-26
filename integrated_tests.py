import unittest
import requests

HOST_LOGIN='http://0.0.0.0:80/'
HOST_OVERVIEW='http://0.0.0.0/overview/dsf'

class TestEndpoints(unittest.TestCase):

    def test_endpoints_user(self):

        for endpoint in ('/user', '/overview'):
            with self.subTest(path=endpoint):
                url = HOST_LOGIN + endpoint
                response = requests.get(url)
                print(url, response.status_code)
                self.assertEqual(response.status_code, requests.codes.ok, msg=f'expected status code {requests.codes.ok}')

    def test_endpoints_data(self):

        for endpoint in ('/temperature', '/humidity'):
            with self.subTest(path=endpoint):
                url = HOST_OVERVIEW + endpoint
                response = requests.get(url)
                print(url, response.status_code)
                self.assertEqual(response.status_code, requests.codes.ok, msg=f'expected status code {requests.codes.ok}')


if __name__ == '__main__':
    unittest.main()