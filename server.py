import http.server
import socketserver
import os
import json

PORT = 8000
DIRECTORY = "/home/issai/projetos/Servidor artvida.com.br/Central Artvida APP"

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_POST(self):
        if self.path == '/login':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data)

            username = data.get('username')
            password = data.get('password')
            
            # Verificação de credenciais para o usuário Issai
            if username == 'Issai' and password == '@Paitan1234':
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"status": "success"}).encode())
            else:
                self.send_response(401)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"status": "fail"}).encode())
        else:
            self.send_response(404)
            self.end_headers()

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

if __name__ == "__main__":
    os.chdir(DIRECTORY)
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print(f"Servidor ArtVida rodando em http://localhost:{PORT}")
        print(f"Modo: Central Artvida APP (com Login)")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServidor parado.")
            httpd.server_close()
