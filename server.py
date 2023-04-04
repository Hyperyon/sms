#!/usr/bin/env python3
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from datetime import datetime


def red(filename):
    with open(filename, 'r',encoding='utf-8') as f:return f.read()
def ouate(data, filename):
    with open(filename,'w+') as f:f.write(data)
def get_time():
    return datetime.now().strftime('%d/%m %H:%M')

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        try:content= open(self.path[1:]).read()
        except:content=open("/home/hyperyon/Bureau/python/sms/sms.html").read()
        self.end_headers()
        self.wfile.write(bytes(content, "UTF-8"))


    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode("utf-8")
        self._set_headers() #print information

        req = json.loads(post_data)
        if req["action"] == "RECEIVED" and "message" in req:
            del req["action"], req["deviceId"]
            req["time"] = get_time()
            print(f"{req['time'].split()[-1]} {req['message']}")
            old_data = json.loads(red("data.json"))
            next_id = max([int(x) for x in old_data.keys()])+1
            old_data = dict(list(old_data.items())[:10])
            req = {next_id:req,**old_data}
            ouate(json.dumps(req,indent=4),"data.json")


def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd...')
    httpd.serve_forever()


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()