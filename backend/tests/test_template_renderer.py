"""
Unit tests for template renderer service.
"""

import pytest

from services.template_renderer import render_template


class TestTemplateRenderer:
    """Test cases for template rendering functionality."""

    @pytest.fixture
    def sample_cv_data(self):
        """Sample CV data for testing."""
        return {
            "personal_info": {
                "name": "Jane Smith",
                "email": "jane@example.com",
                "phone": "+1234567890",
                "linkedin": "linkedin.com/in/janesmith",
                "location": "San Francisco, CA",
            },
            "summary": "Experienced software engineer with 5 years in web development.",
            "skills": ["Python", "JavaScript", "React", "Docker"],
            "experience": [
                {
                    "title": "Senior Developer",
                    "company": "Tech Corp",
                    "dates": "2020-2024",
                    "description": ["Led team of 5", "Built scalable systems"],
                }
            ],
            "education": [
                {
                    "degree": "BS Computer Science",
                    "school": "Stanford University",
                    "dates": "2015-2019",
                }
            ],
        }

    def test_render_modern_template(self, sample_cv_data):
        """Test rendering the modern template."""
        result = render_template(sample_cv_data, "modern", "")

        assert result is not None
        assert "Jane Smith" in result
        assert "jane@example.com" in result
        assert "Python" in result
        assert "Senior Developer" in result

    def test_render_classic_template(self, sample_cv_data):
        """Test rendering the classic template."""
        result = render_template(sample_cv_data, "classic", "")

        assert result is not None
        assert "Jane Smith" in result
        assert "Tech Corp" in result

    def test_render_with_profile_picture(self, sample_cv_data):
        """Test rendering with a profile picture."""
        fake_base64 = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg=="

        result = render_template(sample_cv_data, "modern", fake_base64)

        assert result is not None
        assert "data:image" in result or fake_base64 in result

    def test_render_all_templates(self, sample_cv_data):
        """Test that all template IDs work."""
        templates = ["modern", "classic", "creative", "professional", "elegant"]

        for template_id in templates:
            result = render_template(sample_cv_data, template_id, "")
            assert result is not None
            assert len(result) > 0
            assert "Jane Smith" in result

    def test_render_with_missing_fields(self):
        """Test rendering with minimal data."""
        minimal_data = {
            "personal_info": {"name": "Test User"},
            "summary": "Test summary",
            "skills": [],
            "experience": [],
            "education": [],
        }

        result = render_template(minimal_data, "modern", "")

        assert result is not None
        assert "Test User" in result
