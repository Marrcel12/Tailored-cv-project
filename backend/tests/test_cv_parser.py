"""
Unit tests for CV parser service.
"""

from io import BytesIO

from services.cv_parser import parse_cv


class TestCVParser:
    """Test cases for CV parsing functionality."""

    def test_parse_txt_file(self):
        """Test parsing a simple text file."""
        # Create a mock text file
        content = b"John Doe\nSoftware Engineer\nExperience: 5 years"
        mock_file = BytesIO(content)
        mock_file.filename = "test.txt"

        result = parse_cv(mock_file)

        assert result is not None
        assert "John Doe" in result
        assert "Software Engineer" in result
        assert "Experience: 5 years" in result

    def test_parse_empty_file(self):
        """Test parsing an empty file."""
        mock_file = BytesIO(b"")
        mock_file.filename = "empty.txt"

        result = parse_cv(mock_file)

        assert result == ""

    def test_parse_unsupported_format(self):
        """Test parsing an unsupported file format."""
        mock_file = BytesIO(b"some content")
        mock_file.filename = "test.docx"

        result = parse_cv(mock_file)

        # Should return None or empty string for unsupported formats
        assert result is None or result == ""
