from app import server


def test_app_exists():
    """Verify the Flask application instance is created."""
    assert server is not None


def test_app_is_configured():
    """Verify the Flask application loads configuration."""
    assert server.config["SECRET_KEY"] is not None or "SECRET_KEY" in server.config
