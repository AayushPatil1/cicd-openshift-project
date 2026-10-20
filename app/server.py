
"""Minimal HTTP service for the CI/CD assignment."""

from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    """Respond with a service status message."""

    def do_GET(self):
        """Return SERVICERUNNING on the root endpoint."""
        if self.path == "/":
            body = b"SERVICERUNNING"
            status = 200
        else:
            body = b"Not Found"
            status = 404

        self.send_response(status)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)
        print(f"GET {self.path} {status}", flush=True)

    def log_message(self, format, *args):
        """Keep HTTP request logs visible in the container logs."""
        print(f"{self.address_string()} - {format % args}", flush=True)


if __name__ == "__main__":
    print("service starting", flush=True)
    server = HTTPServer(("0.0.0.0", 8000), Handler)
    print("listening on 0.0.0.0:8000", flush=True)
    print("SERVICERUNNING", flush=True)
    server.serve_forever()
