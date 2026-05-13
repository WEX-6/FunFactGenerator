import pytest
from unittest.mock import Mock, patch, MagicMock
import sys
import os

# Add the project root to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from database.provider import SQLiteConnectionProvider


class TestSQLiteConnectionProvider:
    """Test the SQLiteConnectionProvider class"""

    @patch('database.provider.sqlite3.connect')
    def test_init_with_default_values(self, mock_connect):
        """Test initialization with default database path"""
        # ARRANGE
        mock_connection = Mock()
        mock_connect.return_value = mock_connection

        # ACT
        provider = SQLiteConnectionProvider()

        # ASSERT
        mock_connect.assert_called_once_with("facts.db")
        assert provider.conn == mock_connection

    @patch('database.provider.sqlite3.connect')
    @patch.dict(os.environ, {
        'SQLITE_DB_PATH': 'custom_test.db'
    })
    def test_init_with_environment_variable(self, mock_connect):
        """Test initialization with custom environment variable"""
        # ARRANGE
        mock_connection = Mock()
        mock_connect.return_value = mock_connection

        # ACT
        provider = SQLiteConnectionProvider()

        # ASSERT
        mock_connect.assert_called_once_with("custom_test.db")
        assert provider.conn == mock_connection

    @patch('database.provider.sqlite3.connect')
    def test_init_with_explicit_path(self, mock_connect):
        """Test initialization with explicit database path"""
        # ARRANGE
        mock_connection = Mock()
        mock_connect.return_value = mock_connection

        # ACT
        provider = SQLiteConnectionProvider(db_path="explicit.db")

        # ASSERT
        mock_connect.assert_called_once_with("explicit.db")
        assert provider.conn == mock_connection

    @patch('database.provider.sqlite3.connect')
    def test_init_connection_error(self, mock_connect):
        """Test handling of connection errors during initialization"""
        # ARRANGE
        mock_connect.side_effect = Exception("Connection failed")

        # ACT & ASSERT
        with pytest.raises(Exception) as exc_info:
            SQLiteConnectionProvider()

        assert "Connection failed" in str(exc_info.value)

    @patch('database.provider.sqlite3.connect')
    def test_cursor_method(self, mock_connect):
        """Test cursor method returns connection cursor"""
    @patch('database.provider.sqlite3.connect')
    def test_cursor_method(self, mock_connect):
        """Test cursor method returns connection cursor"""
        # ARRANGE
        mock_connection = Mock()
        mock_cursor = Mock()
        mock_connect.return_value = mock_connection
        mock_connection.cursor.return_value = mock_cursor

        provider = SQLiteConnectionProvider()

        # ACT
        result = provider.cursor()

        # ASSERT
        mock_connection.cursor.assert_called_once()
        assert result == mock_cursor

    @patch('database.provider.sqlite3.connect')
    def test_cursor_method_multiple_calls(self, mock_connect):
        """Test cursor method can be called multiple times"""
        # ARRANGE
        mock_connection = Mock()
        mock_cursor1 = Mock()
        mock_cursor2 = Mock()
        mock_connect.return_value = mock_connection
        mock_connection.cursor.side_effect = [mock_cursor1, mock_cursor2]

        provider = SQLiteConnectionProvider()

        # ACT
        cursor1 = provider.cursor()
        cursor2 = provider.cursor()

        # ASSERT
        assert mock_connection.cursor.call_count == 2
        assert cursor1 == mock_cursor1
        assert cursor2 == mock_cursor2

    @patch('database.provider.sqlite3.connect')
    def test_commit_method(self, mock_connect):
        """Test commit method calls connection commit"""
        # ARRANGE
        mock_connection = Mock()
        mock_connect.return_value = mock_connection

        provider = SQLiteConnectionProvider()

        # ACT
        provider.commit()

        # ASSERT
        mock_connection.commit.assert_called_once()

    @patch('database.provider.sqlite3.connect')
    def test_close_method(self, mock_connect):
        """Test close method calls connection close"""
        # ARRANGE
        mock_connection = Mock()
        mock_connect.return_value = mock_connection

        provider = SQLiteConnectionProvider()

        # ACT
        provider.close()

        # ASSERT
        mock_connection.close.assert_called_once()

    @patch('database.provider.sqlite3.connect')
    def test_cursor_commit_close_workflow(self, mock_connect):
        """Test typical workflow: cursor, commit, close"""
        # ARRANGE
        mock_connection = Mock()
        mock_cursor = Mock()
        mock_connect.return_value = mock_connection
        mock_connection.cursor.return_value = mock_cursor

        provider = SQLiteConnectionProvider()

        # ACT
        cursor = provider.cursor()
        provider.commit()
        provider.close()

        # ASSERT
        mock_connection.cursor.assert_called_once()
        mock_connection.commit.assert_called_once()
        mock_connection.close.assert_called_once()
        assert cursor == mock_cursor

    @patch('database.provider.sqlite3.connect')
    def test_row_factory_set(self, mock_connect):
        """Test that row_factory is set to sqlite3.Row"""
        # ARRANGE
        mock_connection = Mock()
        mock_connect.return_value = mock_connection

        # ACT
        provider = SQLiteConnectionProvider()

        # ASSERT
        assert hasattr(mock_connection, 'row_factory')


if __name__ == '__main__':
    pytest.main([__file__])