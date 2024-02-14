import unittest
from app import app 

class TestHome(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True
        self.ctx = app.app_context()
        self.ctx.push()

    def tearDown(self):
        self.ctx.pop()

    def test_home_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    def test_home_data(self):
        response = self.client.get('/')
        self.assertEqual(response.data, b"Hello, World!")

if __name__ == '__main__':
    unittest.main()