#!/bin/sh python2
from flask import Flask
from srcs import blih

if __name__ == '__main__':
	try:
		app = Flask(__name__)
		app.register_blueprint(blih.blih, url_prefix='/blih')
		app.run(port=80, host="0.0.0.0", threaded=True)
	except Exception as e:
		print(e)