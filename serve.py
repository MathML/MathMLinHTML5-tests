import SimpleHTTPServer
import SocketServer, socket
import sys

if len(sys.argv) > 2:
    print("usage: python %s [PORT]" % sys.argv[0])
    exit(1)

HOST = "localhost"
if len(sys.argv) == 2:
    PORT = int(sys.argv[1])
else:
    PORT = 8421

print("Starting server at http://%s:%d... " % (HOST, PORT))
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer((HOST, PORT), Handler, bind_and_activate=False)
httpd.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
httpd.server_bind()
httpd.server_activate()
httpd.serve_forever()
