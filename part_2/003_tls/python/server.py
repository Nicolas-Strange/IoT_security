import ssl

from flask import Flask
from gevent.pywsgi import WSGIServer

app = Flask(__name__)

HOST = "192.168.3.14"
PORT = 38440


@app.route("/logic", methods=["POST"])
def logic():
    return "Hello from the server"


if __name__ == '__main__':
    certfile = 'server.crt'
    keyfile = 'server.key'

    # Create SSL/TLS context
    ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    ssl_context.load_cert_chain(certfile, keyfile)

    http_server = WSGIServer((HOST, PORT), app, ssl_context=ssl_context)
    http_server.serve_forever()
