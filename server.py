from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"GET endpoint reached")

    def do_POST(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"POST endpoint reached")

    def do_PUT(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"PUT endpoint reached")

    def do_DELETE(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"DELETE endpoint reached")

server = HTTPServer(("0.0.0.0", 8080), SimpleHandler)
print("Server running on port 8080...")
server.serve_forever()
