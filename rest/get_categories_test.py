import pytest
from unittest.mock import patch
import sys
import os

# Add the project root to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from flask import Flask
from rest.get_categories import get_categories_route


class TestGetCategoriesRoute:
	"""Test the get_categories_route function"""

	@pytest.fixture
	def app(self):
		"""Create test Flask app"""
		app = Flask(__name__)
		app.config['TESTING'] = True
		return app

	@patch('rest.get_categories.get_categories')
	def test_get_categories_route_success(self, mock_get_categories, app):
		"""Test successful category retrieval"""
		mock_get_categories.return_value = ["animal", "food", "science"]

		with app.test_request_context('/api/categories'):
			response = get_categories_route()

		assert response.status_code == 200
		assert response.get_json() == {"categories": ["animal", "food", "science"]}
		mock_get_categories.assert_called_once_with()

	@patch('rest.get_categories.get_categories')
	def test_get_categories_route_empty_list(self, mock_get_categories, app):
		"""Test category retrieval when no categories exist"""
		mock_get_categories.return_value = []

		with app.test_request_context('/api/categories'):
			response = get_categories_route()

		assert response.status_code == 200
		assert response.get_json() == {"categories": []}
		mock_get_categories.assert_called_once_with()

	@patch('rest.get_categories.get_categories')
	def test_get_categories_route_database_error(self, mock_get_categories, app):
		"""Test propagation of database errors"""
		mock_get_categories.side_effect = Exception("Database connection failed")

		with app.test_request_context('/api/categories'):
			with pytest.raises(Exception) as exc_info:
				get_categories_route()

		assert "Database connection failed" in str(exc_info.value)
		mock_get_categories.assert_called_once_with()


if __name__ == '__main__':
	pytest.main([__file__])
