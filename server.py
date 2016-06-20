#!/bin/sh python2
import os
from srcs import app, log, blih, intra

def	getVar(name, default=None):
	try:
		return os.environ[name]
	except:
		return default

if __name__ == '__main__':
	try:
		api = app.app
		if bool(getVar("EPITECH_API_LOGGER", False)):
			api.logger.addHandler(log.logger)
		api.register_blueprint(blih.subApp, url_prefix='/blih')
		api.register_blueprint(intra.subApp, url_prefix='/intra')
		api.run(port=int(getVar("EPITECH_API_PORT", 8080)), host="0.0.0.0", threaded=True, debug=bool(getVar("EPITECH_API_DEBUG", False)))
	except Exception as e:
		print(e)