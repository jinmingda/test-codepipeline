"""Unittests for the views module."""


class TestViews:
    """Test views."""

    def test_home(self, testapp):
        """Test homepage."""
        response = testapp.get("/")
        assert response.status_code == 200
        assert response.text == "HelloWorld"
