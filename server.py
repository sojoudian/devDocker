from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import datetime

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        utcTime = datetime.datetime.utcnow()
        torotoTime = utcTime - datetime.timedelta(hours=5)
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        message = json.dumps({
            'TorontoTime': torotoTime.strftime('%Y-%m-%d %H:%M:%S')
        })
        self.wfile.write(message.encode('utf-8'))

def run(serverClass=HTTPServer, handlerClass=RequestHandler, port=8010):
    serverAddress = ('', port)
    httpd = HTTPServer(serverAddress, RequestHandler)
    print(f'Starting httpd server on port {port}...')
    httpd.serve_forever()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print('Stopping httpd server..')

if __name__ == '__main__':
    run()    