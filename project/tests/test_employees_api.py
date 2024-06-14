import unittest
import sys
import os

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the Connexion app and Flask app
from employees_api import app  # Ensure this path is correct
from admin_fr import app as admin_app  # Ensure this path is correct

class EmployeesApiTestCase(unittest.TestCase):
    def setUp(self):
        # Set up the test client for the Connexion app
        self.client = app.app.test_client()  # Access the Flask app within the Connexion app
        self.client.testing = True

    def test_read_employee(self):
        # Test reading an employee by ID
        response = self.client.get('/employees/1')
        # Check if the response status code is either 200 (OK) or 404 (Not Found)
        self.assertIn(response.status_code, [200, 404])  # Employee might or might not exist

    def test_update_employee(self):
        # Test updating an employee by ID
        response = self.client.put('/employees/1', json={
            'name': 'Updated Employee',
            'surname': 'Updated',
            'position': 'Senior Developer',
            'phone': '0987654321',
            'email': 'updated.employee@example.com'
        })
        # Check if the response status code is either 200 (OK) or 404 (Not Found)
        self.assertIn(response.status_code, [200, 404])  # Employee might or might not exist

    def test_delete_employee(self):
        # Test deleting an employee by ID
        response = self.client.delete('/employees/1')
        # Check if the response status code is either 204 (No Content) or 404 (Not Found)
        self.assertIn(response.status_code, [204, 404])  # Employee might or might not exist

class AdminFrontendTestCase(unittest.TestCase):
    def setUp(self):
        # Set up the test client for the Flask app
        self.client = admin_app.test_client()
        self.client.testing = True

    def test_root_endpoint(self):
        # Test accessing the root endpoint
        response = self.client.get('/')
        # Check if the response status code is 302 (Found), which indicates a redirect to the login page
        self.assertEqual(response.status_code, 302)  # Should redirect to login

    def test_login_page(self):
        # Test accessing the login page
        response = self.client.get('/login')
        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Check if the response contains the text 'Login'
        self.assertIn(b'Login', response.data)

    def test_login_and_index_page(self):
        # Log in to the application
        response = self.client.post('/login', data={'username': 'admin', 'password': '123456'})
        # Check if the response status code is 302 (Found), indicating a redirect to the index page
        self.assertEqual(response.status_code, 302)  # Should redirect to the index page

        # Check the index page after login
        response = self.client.get('/')
        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Check if the response contains the text 'Employees Information'
        self.assertIn(b'Employees Information', response.data)

    def test_logout(self):
        # Log in to the application
        self.client.post('/login', data={'username': 'admin', 'password': '123456'})

        # Log out of the application
        response = self.client.post('/logout')
        # Check if the response status code is 302 (Found), indicating a redirect to the login page
        self.assertEqual(response.status_code, 302)  # Should redirect to login

if __name__ == '__main__':
    unittest.main()
