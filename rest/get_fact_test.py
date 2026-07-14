 #P4.7, P5.9
# To Run: pytest rest/get_fact_test.py

import pytest
from unittest.mock import patch

from rest.get_fact import get_route
from fact import Fact


class TestGetFactRoute:
    """Test the get_route function"""
# Tasks P0.4
    # Patch the get_fact function to mock database interactions
    @patch('rest.get_fact.get_fact')
    def test_get_route_html_response(self, mock_get_fact, app):
        """Test GET request returns HTML template by default with category data"""
        # ARRANGE
        mock_fact = Fact(id=1, fact="Test fact", category="science", likes=5, dislikes=2)
        mock_get_fact.return_value = mock_fact

        with app.test_request_context('/'): # default to HTML response
            with patch('rest.get_fact.render_template') as mock_render:
                mock_render.return_value = "generate template"

                # ACT
                result = get_route()

                # ASSERT
                assert result == "generate template" # Check that the rendered template is returned
                mock_get_fact.assert_called_once()
                mock_render.assert_called_once_with(
                    "generate.html",
                    random_fact="Test fact",
                    category="science",
                    random_fact_id=1,
                    random_fact_likes=5,
                    random_fact_dislikes=2
                )

    # Patch the get_fact function to mock database interactions
    @patch('rest.get_fact.get_fact')
    def test_get_route_with_null_fact_attributes(self, mock_get_fact, app):
        """Test handling fact with NULL/None attributes"""
        # ARRANGE
        mock_fact = Fact(id=None, fact="Fact with null attributes", category=None, likes=None, dislikes=None)
        mock_get_fact.return_value = mock_fact

        with app.test_request_context('/?json=1'):
            with patch('rest.get_fact.jsonify') as mock_jsonify:
                mock_jsonify.return_value = "null attributes json"

                # ACT
                # TODO: Call the get_route function

                # ASSERT
                # TODO: Check that the JSON response is returned
                mock_jsonify.assert_called_with({}) # TODO: Verify that the JSON response contains default values for null attributes

    # Patch the get_fact function to mock database interactions
    @patch('rest.get_fact.get_fact')
    def test_get_route_database_error(self, mock_get_fact, app):
        """Test handling database errors"""
        # ARRANGE
        mock_get_fact.side_effect = Exception("Database connection failed")

        with app.test_request_context('/'):
            # ACT
            with pytest.raises(Exception) as exc_info:
             # TODO: Call the get_route function
                get_route()

            # ASSERT
            # TODO: (Task P0.4) Verify the exception message contains the correct error message
            # TODO: (Task P0.4) Verify that get_fact was called

    # Patch the get_fact function to mock database interactions
    @patch('rest.get_fact.get_fact')
    def test_get_route_render_template_error(self, mock_get_fact, app):
        """Test handling template rendering errors"""
        # ARRANGE
        mock_fact = Fact(id=8, fact="Template error fact", category="error", likes=1, dislikes=1)
        mock_get_fact.return_value = mock_fact

        with app.test_request_context('/'):
            with patch('rest.get_fact.render_template') as mock_render:
                mock_render.side_effect = Exception("Template not found")

                # ACT
                with pytest.raises(Exception) as exc_info:
                    pass  # TODO: Call the get_route function

                # ASSERT
                # TODO: (Task P0.4) Verify the exception message contains the correct error message
                # TODO: (Task P0.4) Verify that get_fact was called

if __name__ == '__main__':
    pytest.main([__file__])