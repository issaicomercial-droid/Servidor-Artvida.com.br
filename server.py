from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response = {
            "status": "online",
            "message": "WSL Server is alive!",
            "connection": "external"
        }
        self.wri(json.dumps(response).encode())

    def wri(self, content):
        self.wfile.write(content)

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ('0.0.0.0', port)
    httpd = server_class(server_address, handler_class)
    print(f"Servidor rodando em http://0.0.0.0:{port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
