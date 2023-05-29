import unittest
import requests
import threading
import time

from flask import Flask
from main import app

class TestApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Start the Flask app in a separate thread
        cls.server_thread = threading.Thread(target=app.run, kwargs={'host': '0.0.0.0', 'port': 8000})
        cls.server_thread.daemon = True
        cls.server_thread.start()
        # Allow some time for the server to start
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        # Stop the Flask app
        requests.get('http://localhost:8000/shutdown')
        cls.server_thread.join()

    def test_index(self):
        response = requests.get('http://localhost:8000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, 'Web App with Python Flask!')


if __name__ == '__main__':
    unittest.main()

