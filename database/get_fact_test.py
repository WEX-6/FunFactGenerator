# Task P0.4

import pytest
from unittest.mock import Mock, patch
import sys
import os

# Add the project root to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from database.get_fact import get_fact
from fact import Fact


class TestGetFact:
    """Test the get_fact function"""

    # Patch the SQLiteConnectionProvider to mock database interactions
    @patch.object(sys.modules['database.get_fact'], 'SQLiteConnectionProvider')
    def test_get_fact_success(self, mock_provider_class):
        """Test successful fact retrieval"""
        # ARRANGE
        mock_provider = Mock()
        mock_cursor = Mock()
        mock_provider_class.return_value = mock_provider
        mock_provider.cursor.return_value.__enter__ = Mock(return_value=mock_cursor)
        mock_provider.cursor.return_value.__exit__ = Mock(return_value=None)

        # Mock database return values
        mock_cursor.fetchone.return_value = (1, "Random test fact", "science", 5, 2)

        # ACT
        result = get_fact()

        # ASSERT
        assert isinstance(result, Fact)
        assert result.id == 1
        assert result.fact == "Random test fact"
        assert result.category == "science"
        assert result.likes == 5
        assert result.dislikes == 2

        # Verify SQL execution
        mock_cursor.execute.assert_called_once_with(
            "SELECT id, fact, category, likes, dislikes FROM facts ORDER BY RANDOM() LIMIT 1;"
        )

    # Patch the SQLiteConnectionProvider to mock database interactions
    @patch.object(sys.modules['database.get_fact'], 'SQLiteConnectionProvider')
    def test_get_fact_with_null_likes_dislikes(self, mock_provider_class):
        """Test fact retrieval when likes/dislikes are NULL in database"""
        # ARRANGE
        mock_provider = Mock()
        mock_cursor = Mock()
        mock_provider_class.return_value = mock_provider
        mock_provider.cursor.return_value.__enter__ = Mock(return_value=mock_cursor)
        mock_provider.cursor.return_value.__exit__ = Mock(return_value=None)

        # Mock database return with NULL values
        mock_cursor.fetchone.return_value = (2, "Another random fact", "history", None, None)

        # ACT
        # TODO: Call the get_fact function

        # ASSERT
        # TODO: Verify that the Fact object is created with default values for likes/dislikes

    @patch.object(sys.modules['database.get_fact'], 'SQLiteConnectionProvider')
    def test_get_fact_no_results_found(self, mock_provider_class):
        """Test behavior when no facts are found in database"""
        # ARRANGE
        mock_provider = Mock()
        mock_cursor = Mock()
        mock_provider_class.return_value = mock_provider
        mock_provider.cursor.return_value.__enter__ = Mock(return_value=mock_cursor)
        mock_provider.cursor.return_value.__exit__ = Mock(return_value=None)

        # Mock no result returned
        mock_cursor.fetchone.return_value = None

        # ACT
       # TODO: Call the get_fact function

        # ASSERT
        # TODO: Verify that the Fact object is created with default values for likes/dislikes

        # Verify SQL execution
        mock_cursor.execute.assert_called_once()

    @patch.object(sys.modules['database.get_fact'], 'SQLiteConnectionProvider')
    def test_get_fact_database_error(self, mock_provider_class):
        """Test handling of database errors during fact retrieval"""
        # ARRANGE
        mock_provider = Mock()
        mock_cursor = Mock()
        mock_provider_class.return_value = mock_provider
        mock_provider.cursor.return_value.__enter__ = Mock(return_value=mock_cursor)
        mock_provider.cursor.return_value.__exit__ = Mock(return_value=None)

        # Mock database error
        mock_cursor.execute.side_effect = Exception("Database connection failed")

        # ACT & ASSERT
        with pytest.raises(Exception) as exc_info:
            get_fact()

        assert "Database connection failed" in str(exc_info.value)

if __name__ == '__main__':
    pytest.main([__file__])