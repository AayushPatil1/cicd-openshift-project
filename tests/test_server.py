"""Unit tests for the sample service."""
import unittest
from unittest.mock import Mock
from app.server import Handler


class TestServerHandler(unittest.TestCase):
    """Check handler response logic using a minimal mocked request."""

    def test_root_body(self):
        handler = Handler.__new__(Handler)
        handler.path = "/"
        handler.wfile = Mock()
        handler.send_response = Mock()
        handler.send_header = Mock()
        handler.end_headers = Mock()
        handler.do_GET()
        handler.send_response.assert_called_once_with(200)
        handler.wfile.write.assert_called_once_with(b"SERVICERUNNING")

    def test_unknown_path_body(self):
        handler = Handler.__new__(Handler)
        handler.path = "/missing"
        handler.wfile = Mock()
        handler.send_response = Mock()
        handler.send_header = Mock()
        handler.end_headers = Mock()
        handler.do_GET()
        handler.send_response.assert_called_once_with(404)
        handler.wfile.write.assert_called_once_with(b"Not Found")


if __name__ == "__main__":
    unittest.main()
