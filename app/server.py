
"""Minimal HTTP service for the CI/CD assignment."""

from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    """Respond with a service status message."""

    def do_GET(self):
        """Return SERVICERUNNING on the root endpoint."""
        if self.path == "/":
            body = b"SERVICERUNNING"
            self.send_response(200)
        else:
            body = b"Not Found"
            self.send_response(404)

        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()


