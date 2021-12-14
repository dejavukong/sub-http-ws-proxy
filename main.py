from http.server import HTTPServer, BaseHTTPRequestHandler

import websocket

# todo get this link from command
host = ('localhost', 9933)
# websocket endpoint
endpoint = "wss://peregrine.kilt.io/"

class Resquest(BaseHTTPRequestHandler):
    def do_POST(self):
        content_len = int(self.headers.get('Content-Length'))
        post_body = self.rfile.read(content_len)
        # get required body
        print(post_body)
        
        ws = websocket.WebSocket()
        # todo get this link from command
        ws.connect(endpoint)
        ws.send(post_body)
        print("send to websocket channel and wait...")
        res = ws.recv()
        print(res)
        ws.close()

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(bytes(res, encoding='utf8'))

if __name__ == '__main__':
    server = HTTPServer(host, Resquest)
    print("Starting server, listen at: %s:%s" % host)
    server.serve_forever()