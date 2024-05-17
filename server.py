from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            try:
                file_to_open = open("/home/factorlibre/test.html").read()
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(bytes(file_to_open, 'utf-8'))
            except:
                self.send_response(404)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'404 - Not Found')
        else:
            # self.send_response(200)
            # self.end_headers()
            # self.wfile.write(b'Hello, world!')
            try:
                self.send_response(200)
                self.send_header("Content-type", "text/csv")
                self.end_headers()
                with open('/home/factorlibre{}'.format(self.path), 'rb') as file: 
                    self.wfile.write(file.read())
                # self.wfile.write(bytes(file_to_open, 'utf-8'))
                # self.wfile.write(bytes(file_to_open, 'utf-8'))
            except:
                self.send_response(404)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'404 - Not Found')

httpd = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()