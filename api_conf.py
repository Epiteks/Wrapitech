import os

server_url = "https://intra.epitech.eu"
listen_port = int(os.environ.get("PORT", 8080))
listen_host = "0.0.0.0"
debug = True
ssl_verify= False
