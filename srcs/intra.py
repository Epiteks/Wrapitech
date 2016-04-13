from flask import Blueprint, request#, Response
import json
from time import strftime, strptime
from datetime import timedelta, date
import requester

subApp = Blueprint('intra', __name__)

def	make_route(route):
	return "https://intra.epitech.eu" + route

class URLArgError(Exception):

	def __init__(self, value):
		self.message = value
		self.value = "URLArg Error : " + self.message

	def __str__(self):
		return repr(self.value)

def getArg(key, default=None):
	res = request.args.get(key)
	if not res:
		if default:
			return default
		else:
			raise URLArgError("Missing argument {0}".format(key))
	return res

def	getTokenRequest(url, method, data=None):
	req = requester.Request(url, method, data)
	req.setCookie("PHPSESSID", getArg("token"))
	return req if request.args.get("token") else None

@subApp.route('/', methods=['GET'])
def root():
	return requester.response({"status": True}, 200)

@subApp.route('/login', methods=['POST'])
def login():
	try:
		data = json.loads(request.data)
		for value in ["login", "password"]:
			if value not in data:
				return requester.error("Missing {0}".format(value), 400)
		if type(data["login"]) not in [str, unicode]:
			print(type(data["login"]))
			return requester.error("Wrong login format", 400)
		body = {"login": data["login"], "password": data["password"]}
	except:
		return requester.error("Wrong login format""Wrong login format", 400)
	req = requester.Request(make_route("/?format=json"), "POST", body)
	result = requester.executeRequest(req)
	if result["code"] == 200:
		token = req.getCookies()['PHPSESSID']
		return requester.response({"token": token}, 200)
	else:
		return requester.error(result["data"]["message"], 401)

@subApp.route('/infos', methods=['GET'])
def getInfos():
	req = getTokenRequest(make_route("/?format=json"), "GET")
	if not req:
		return requester.error("Missing token", 401)
	result = requester.executeRequest(req)
	if result["code"] == 200:
		return requester.response(result["data"], 200)
	return requester.error(result["data"]["message"], 401)

@subApp.route('/planning', methods=['GET'])
def getPlanning():
	try:
		route = "/intra/planning/load?format=json&start={0}&end={1}".format(getArg("start"), getArg("end"))
	except URLArgError as e:
		return requester.error(e.message, 401)
	req = getTokenRequest(make_route(route), "POST")
	if not req:
		return requester.error("Missing token", 401)
	result = requester.executeRequest(req)
	if result["code"] == 200:
		return requester.response(result["data"], 200)
	return requester.error(result["data"]["message"], 401)

@subApp.route('/susies', methods=['GET'])
def getSusies():
	return requester.error("Available soon", 501)

@subApp.route('/susie', methods=['GET'])
def getSusie():
	return requester.error("Available soon", 501)

@subApp.route('/susie', methods=['POST'])
def subscribeSusie():
	return requester.error("Available soon", 501)

@subApp.route('/susie', methods=['DELETE'])
def unsubscribeSusie():
	return requester.error("Available soon", 501)

@subApp.route('/projects', methods=['GET'])
def getProjects():
	try:
		now = getArg("start", strftime("%Y-%m-%d", date.today().timetuple()))
		end = strptime(now, "%Y-%m-%d") + timedelta(days=365)
		print(now)
		print(end)
		route = "/module/board/?format=json&start={0}&end={1}".format(now, end)
	except URLArgError as e:
		return requester.error(e.message, 401)
	req = getTokenRequest(make_route(route), "POST")
	if not req:
		return requester.error("Missing token", 401)
	result = requester.executeRequest(req)
	if result["code"] == 200:
		return requester.response(result["data"], 200)
	return requester.error(result["data"]["message"], 401)

@subApp.route('/project', methods=['GET'])
def getProject():
	return requester.error("Available soon", 501)

@subApp.route('/project', methods=['POST'])
def subscribeProject():
	return requester.error("Available soon", 501)

@subApp.route('/project', methods=['DELETE'])
def unsubscribeProject():
	return requester.error("Available soon", 501)

@subApp.route('/project/files', methods=['GET'])
def getProjectFiles():
	return requester.error("Available soon", 501)

@subApp.route('/modules', methods=['GET'])
def getUserModules():
	return requester.error("Available soon", 501)

@subApp.route('/allmodules', methods=['GET'])
def getModules():
	return requester.error("Available soon", 501)

@subApp.route('/module', methods=['GET'])
def getModule():
	return requester.error("Available soon", 501)

@subApp.route('/module', methods=['POST'])
def subscribeModule():
	return requester.error("Available soon", 501)

@subApp.route('/module', methods=['DELETE'])
def unsubscribeModule():
	return requester.error("Available soon", 501)

@subApp.route('/event', methods=['GET'])
def getEvent():
	return requester.error("Available soon", 501)

@subApp.route('/event', methods=['POST'])
def subscribeEvent():
	return requester.error("Available soon", 501)

@subApp.route('/event', methods=['DELETE'])
def unsubscribeEvent():
	return requester.error("Available soon", 501)

@subApp.route('/marks', methods=['GET'])
def getMarks():
	return requester.error("Available soon", 501)

@subApp.route('/messages', methods=['GET'])
def getMessages():
	return requester.error("Available soon", 501)

@subApp.route('/alerts', methods=['GET'])
def getAlerts():
	return requester.error("Available soon", 501)

#TODO : Need auth?
#TODO : Check if user exist
@subApp.route('/photo', methods=['GET'])
def getPhoto():
	login = getArg("login", "")
	if login:
		result = {"url": "https://cdn.local.epitech.eu/userprofil/profilview/{0}.jpg".format(login)}
		return requester.response(result, 200)
	else:
		return requester.error("Missing login", 401)

@subApp.route('/token', methods=['POST'])
def setToken():
	return requester.error("Available soon", 501)

@subApp.route('/trombi', methods=['GET'])
def getUserList():
	return requester.error("Available soon", 501)
