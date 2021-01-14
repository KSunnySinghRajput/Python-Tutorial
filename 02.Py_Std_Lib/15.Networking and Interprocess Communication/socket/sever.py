import http.server
import socketserver
import webbrowser

PORT = 80

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("http://localhost:"+str(PORT))
    webbrowser.open("http://localhost:"+str(PORT))
    httpd.serve_forever()
