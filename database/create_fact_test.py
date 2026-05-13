# Task P1.4

import pytest
from unittest.mock import Mock, patch
import sys
import os

# Add the project root to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from database.create_fact import create_fact
from fact import Fact


class TestCreateFact:
    """Test the create_fact function"""

    @patch.object(sys.modules['database.create_fact'], 'SQLiteConnectionProvider')
    def test_create_fact_success(self, mock_provider_class):
        """Test successful fact creation"""
        # ARRANGE
        mock_provider = Mock()
        mock_cursor = Mock()
        mock_provider_class.return_value = mock_provider
        mock_provider.cursor.return_value.__enter__ = Mock(return_value=mock_cursor)
        mock_provider.cursor.return_value.__exit__ = Mock(return_value=None)

        # Mock database return values
        mock_cursor.fetchone.return_value = (1, "Test fact", "science", 0, 0)

        # ACT
        # TODO: Call the create_fact function with some test data as arguments

        # ASSERT
        # TODO: Check if returned fact fields match what we expect 

        # Verify SQL execution
        mock_cursor.execute.assert_called_once()
        mock_provider.commit.assert_called_once()

    @patch.object(sys.modules['database.create_fact'], 'SQLiteConnectionProvider')
    def test_create_fact_with_null_likes_dislikes(self, mock_provider_class):
        """Test fact creation when likes/dislikes are NULL in database"""
        # ARRANGE
        mock_provider = Mock()
        mock_cursor = Mock()
        mock_provider_class.return_value = mock_provider
        mock_provider.cursor.return_value.__enter__ = Mock(return_value=mock_cursor)
        mock_provider.cursor.return_value.__exit__ = Mock(return_value=None)

        # TODO: Mock database return with NULL values for likes and dislikes

        # ACT
        # TODO: Call the create_fact function with some test data as arguments

        # ASSERT
        # TODO: Check if returned fact fields match what we expect 

    @patch.object(sys.modules['database.create_fact'], 'SQLiteConnectionProvider')
    def test_create_fact_empty_strings(self, mock_provider_class):
        """Test fact creation with empty strings"""
        # ARRANGE
        mock_provider = Mock()
        mock_cursor = Mock()
        mock_provider_class.return_value = mock_provider
        mock_provider.cursor.return_value.__enter__ = Mock(return_value=mock_cursor)
        mock_provider.cursor.return_value.__exit__ = Mock(return_value=None)

        mock_cursor.fetchone.return_value = (4, "", "", 0, 0)

        # ACT
        # TODO: Call the create_fact function with empty string test data as arguments

        # ASSERT
        # TODO: Check if returned fact fields match what we expect 


if __name__ == '__main__':
    pytest.main([__file__])