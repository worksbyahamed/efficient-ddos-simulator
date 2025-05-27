# fake_server.py
# Author: worksbyahamed

import http.server
import socketserver
import threading

PORT = 8080
request_count = 0
lock = threading.Lock()

class TrafficHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory="static", **kwargs)

    def do_GET(self):
        global request_count
        with lock:
            request_count += 1
            current_count = request_count
        print(f"[{self.client_address[0]}] {self.command} {self.path} | Total requests: {current_count}")
        if self.path == "/count":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(f'{{"count": {current_count}}}'.encode())
        else:
            super().do_GET()

if __name__ == "__main__":
    with socketserver.ThreadingTCPServer(("", PORT), TrafficHandler) as httpd:
        print(f"Serving fake web page at http://127.0.0.1:{PORT}")
        httpd.serve_forever()
