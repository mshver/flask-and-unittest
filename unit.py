import unittest
from app import app


class Test(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_sphere(self):
        with app.test_client() as client:
            data = {'shape': 'sphere', 'radius': '1', 'accuracy': '1'}
            response = self.app.post('/calculations', data=data)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'4.2', response.data)

    def test_cube(self):
        with app.test_client() as client:
            data = {'shape': 'cube', 'side': '1', 'accuracy': '1'}
            response = self.app.post('/calculations', data=data)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'1.0', response.data)

    def test_cylinder(self):
        with app.test_client() as client:
            data = {'shape': 'cylinder','height': '1', 'radius': '1', 'accuracy': '1'}
            response = self.app.post('/calculations', data=data)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'3.1', response.data)


if __name__ == '__main__':
    unittest.main()