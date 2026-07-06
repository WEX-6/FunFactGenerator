# TASKS: P1.4, P4.7
# To Run: pytest rest/create_fact_test.py

import pytest
from unittest.mock import patch

from rest.create_fact import create_route
from fact import Fact


class TestCreateFactRoute:
    """Test the create_route function"""

    def test_create_route_get_request(self, app):
        """Test GET request returns create.html template"""
        with app.test_request_context('/', method='GET'):
            with patch('rest.create_fact.render_template') as mock_render:
                mock_render.return_value = "create template"

                result = create_route()

                assert result == "create template"
                mock_render.assert_called_once_with("create.html")

    @patch('rest.create_fact.create_fact')
    def test_create_route_post_success(self, mock_create_fact, app):
        """Test successful POST request with valid data"""
        # ARRANGE
        # TODO: (Task P4.7) Create a 'mock_fact' variable with fact and category test data
        mock_fact = None
        mock_create_fact.return_value = mock_fact

        with app.test_request_context('/', method='POST', data={
            'fact_text': 'Test fact',
            'category': 'science'
        }):
            with patch('rest.create_fact.render_template') as mock_render:
                mock_render.return_value = "success template"

                # ACT
                result = None # TODO: (Task P4.7) Call the create_route function

                # ASSERT
                assert result == "success template"
                mock_create_fact.assert_called_once_with('Test fact', 'science')
                mock_render.assert_called_once_with(
                    "create.html", 
                    random_fact="Test fact", 
                    category="science"
                )

    @patch('rest.create_fact.create_fact')
    def test_create_route_post_with_empty_category(self, mock_create_fact, app):
        """Test POST request with empty category"""
        # ARRANGE
        mock_fact = Fact(id=2, fact="Fact without category", category=None, likes=0, dislikes=0)
        mock_create_fact.return_value = mock_fact

        with app.test_request_context('/', method='POST', data={
            'fact_text': 'Fact without category',
            'category': ''
        }):
            with patch('rest.create_fact.render_template') as mock_render:
                mock_render.return_value = "template with empty category"

                # ACT
                # TODO: (Task P4.7) Call the create_route function

                # ASSERT
                # TODO: (Task P4.7) Verify the result, create_fact call, and render_template call

    @patch('rest.create_fact.create_fact')
    def test_create_route_post_with_missing_category(self, mock_create_fact, app):
        """Test POST request with missing category field"""
        # ARRANGE
        mock_fact = Fact(id=3, fact="Fact with no category field", category=None, likes=0, dislikes=0)
        mock_create_fact.return_value = mock_fact

        with app.test_request_context('/', method='POST', data={
            'fact_text': 'Fact with no category field'
            # No category field provided
        }):
            with patch('rest.create_fact.render_template') as mock_render:
                mock_render.return_value = "template with None category"

                # ACT
                # TODO: (Task P4.7) Call the create_route function

                # ASSERT
                # TODO: (Task P4.7) Verify the result, create_fact call, and render_template call

    def test_create_route_post_missing_fact_text(self, app):
        """Test POST request with missing fact_text returns 400 error"""
        with app.test_request_context('/', method='POST', data={
            'category': 'science'
            # No fact_text provided
        }):
            # ACT
            # TODO: (Task P1.4) Call the create_route function

            # ASSERT
            # TODO: (Task P1.4) Verify the result is a 400 error response
            pass

    @patch('rest.create_fact.create_fact')
    def test_create_route_database_error(self, mock_create_fact, app):
        """Test POST request when database function raises an error"""
        # ARRANGE
        mock_create_fact.side_effect = Exception("Database connection failed")

        with app.test_request_context('/', method='POST', data={
            'fact_text': 'Test fact',
            'category': 'science'
        }):
            # ACT & ASSERT
            # TODO: (Task P1.4) Call create_route and verify it raises an exception with the correct message
            pass

if __name__ == '__main__':
    pytest.main([__file__])