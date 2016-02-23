from flask import Response
import json
import requests

class RequestError(Exception):

	def __init__(self, value):
		self.value = "Request Error : " + value

	def __str__(self):
		return repr(self.value)

class	Request(object):

	def	__init__(self, url, method, data=None):
		super(Request, self).__init__()

		self._done = False
		self._url = url
		self._types = {"GET": requests.get,
					"POST": requests.post,
					"DELETE": requests.delete}
		if method not in self._types:
			raise RequestError("Wrong method")
		self._method = method
		self._data = bytearray(json.dumps(data), "utf8")
		self._error = None
		self._request = None
		self._cookies = {}

	def	execute(self):
		self._done = True
		self._request = self._types[self._method](self._url, data=self._data, headers={"Content-Type": "application/json"}, cookies=self._cookies)
		return True if self._request.status_code == 200 else False

	def	parse(self):
		if self._done and not self._error and self._request.status_code == 200:
			return {"code": self._request.status_code, "data": self._request.json()}
		return None

	def	getError(self):
		return {"code": self._request.status_code, "data": self._request.json()}

	def	getCookies(self):
		return self._request.cookies if self._request else None

	def	setCookie(self, key, value):
		self._cookies[key] = value

def executeRequest(req):
	status = req.execute()
	return req.parse() if status else req.getError()

def response(res, code):
	return Response(response=json.dumps(res), mimetype="application/json", status=code)

def error(message, code):
	return response({"error": message}, code)
