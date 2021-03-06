from flask import Blueprint, request
import json
from time import strftime
from datetime import timedelta, date, datetime
import requester
import formatter

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
	args = request.args.get(key)
	head = request.headers.get(key)
	if not args and not head:
		if default != None:
			return default
		else:
			raise URLArgError("Missing argument {0}".format(key))
	return (args if args else head)

def checkAuth():
	try:
		getArg("token")
		return True
	except URLArgError:
		return False

def	getTokenRequest(url, method, data=None):
	req = requester.Request(url, method, data)
	try:
#		req.setCookie("PHPSESSID", getArg("token"))
		req.setCookie("user", getArg("token"))
		return req
	except URLArgError:
		return None

@subApp.route('/', methods=['GET'])
def root():
	return requester.response({"status": True}, 200)

@subApp.route('/status', methods=['GET'])
def status():
	try:
		import os, platform
		ping_str = "-n 1" if  platform.system().lower()=="windows" else "-c 1"
		status = os.system("ping " + ping_str + " " + make_route("").replace("https://", "")) == 0
		return requester.response({"status": bool(status)}, 200)
	except Exception:
		return requester.response({"status": False}, 200)

@subApp.route('/login', methods=['POST'])
def login():
	try:
		data = json.loads(request.data)
		for value in ["login", "password"]:
			if value not in data:
				return requester.error("Missing {0}".format(value), 400)
		if type(data["login"]) not in [str, unicode]:
			return requester.error("Wrong login format", 400)
		body = {"login": data["login"], "password": data["password"]}
	except:
		return requester.error("Wrong login format", 400)
	req = requester.Request(make_route("/?format=json"), "POST", body)
	result = requester.executeRequest(req)
	if result["code"] == 200:
		token = req.getCookies()['user']
		return requester.response({"token": token}, 200)
	else:
		if "message" in result["data"]:
			return requester.error(result["data"]["message"], 401)
		elif "error" in result["data"]:
			return requester.error(result["data"]["error"], 401)
		else:
			return requester.error("There is an error, try again", 401)

@subApp.route('/infos', methods=['GET'])
def getInfos():
	req = getTokenRequest(make_route("/?format=json"), "GET")
	if not req:
		return requester.error("Missing token", 401)
	result = requester.executeRequest(req)
	if result["code"] == 200:
		return requester.response(result["data"], 200)
	if "message" in result["data"]:
		return requester.error(result["data"]["message"], 401)
	elif "error" in result["data"]:
		return requester.error(result["data"]["error"], 401)
	else:
		return requester.error("There is an error, try again", 401)

@subApp.route('/planning', methods=['GET'])
def getPlanning():
	try:
		start = getArg("start", strftime("%Y-%m-%d", date.today().timetuple()))
		end = getArg("end", (datetime.strptime(start, "%Y-%m-%d") + timedelta(days=6)))
		route = "/intra/planning/load?format=json&start={0}&end={1}".format(start, end)
	except URLArgError as e:
		return requester.error(e.message, 401)
	req = getTokenRequest(make_route(route), "POST")
	if not req:
		return requester.error("Missing token", 401)
	result = requester.executeRequest(req)
	if result["code"] == 200:
		return requester.response(result["data"], 200)
	if "message" in result["data"]:
		return requester.error(result["data"]["message"], 401)
	elif "error" in result["data"]:
		return requester.error(result["data"]["error"], 401)
	else:
		return requester.error("There is an error, try again", 401)

@subApp.route('/planning', methods=['POST'])
def subscribePlanning():
	try:
		route = "/intra/planning/{0}/{1}/subscribe?format=json".format(getArg("calendar"), getArg("event"))
	except URLArgError as e:
		return requester.error(e.message, 401)
	req = getTokenRequest(make_route(route), "POST")
	if not req:
		return requester.error("Missing token", 401)
	result = requester.executeRequest(req)
	if result["code"] == 200:
		return requester.response(result["data"], 200)
	if "message" in result["data"]:
		return requester.error(result["data"]["message"], 401)
	elif "error" in result["data"]:
		return requester.error(result["data"]["error"], 401)
	else:
		return requester.error("There is an error, try again", 401)

@subApp.route('/planning', methods=['DELETE'])
def unsubscribePlanning():
	try:
		route = "/intra/planning/{0}/{1}/unsubscribe?format=json".format(getArg("calendar"), getArg("event"))
	except URLArgError as e:
		return requester.error(e.message, 401)
	req = getTokenRequest(make_route(route), "POST")
	if not req:
		return requester.error("Missing token", 401)
	result = requester.executeRequest(req)
	if result["code"] == 200:
		return requester.response(result["data"], 200)
	if "message" in result["data"]:
		return requester.error(result["data"]["message"], 401)
	elif "error" in result["data"]:
		return requester.error(result["data"]["error"], 401)
	else:
		return requester.error("There is an error, try again", 401)

@subApp.route('/projects', methods=['GET'])
def getProjects():
	try:
		start = getArg("start", strftime("%Y-%m-%d", date.today().timetuple()))
		end = getArg("end", datetime.strptime(start, "%Y-%m-%d") + timedelta(days=365))
		route = "/module/board/?format=json&start={0}&end={1}".format(start, end)
	except URLArgError as e:
		return requester.error(e.message, 401)
	req = getTokenRequest(make_route(route), "POST")
	if not req:
		return requester.error("Missing token", 401)
	result = requester.executeRequest(req)
	if result["code"] == 200:
		return requester.response(result["data"], 200)
	if "message" in result["data"]:
		return requester.error(result["data"]["message"], 401)
	elif "error" in result["data"]:
		return requester.error(result["data"]["error"], 401)
	else:
		return requester.error("There is an error, try again", 401)

@subApp.route('/project', methods=['GET'])
def getProject():
	try:
		route = "/module/{0}/{1}/{2}/{3}/project?format=json".format(getArg("year"), getArg("module"), getArg("instance"), getArg("activity"))
	except URLArgError as e:
		return requester.error(e.message, 401)
	req = getTokenRequest(make_route(route), "POST")
	if not req:
		return requester.error("Missing token", 401)
	result = requester.executeRequest(req)
	if result["code"] == 200:
		return requester.response(result["data"], 200)
	if "message" in result["data"]:
		return requester.error(result["data"]["message"], 401)
	elif "error" in result["data"]:
		return requester.error(result["data"]["error"], 401)
	else:
		return requester.error("There is an error, try again", 401)

@subApp.route('/project', methods=['POST'])
def subscribeProject():
	try:
		route = "/module/{0}/{1}/{2}/{3}/project/register?format=json".format(getArg("year"), getArg("module"), getArg("instance"), getArg("activity"))
	except URLArgError as e:
		return requester.error(e.message, 401)
	req = getTokenRequest(make_route(route), "POST")
	if not req:
		return requester.error("Missing token", 401)
	result = requester.executeRequest(req)
	if result["code"] == 200:
		return requester.response(result["data"], 200)
	if "message" in result["data"]:
		return requester.error(result["data"]["message"], 401)
	elif "error" in result["data"]:
		return requester.error(result["data"]["error"], 401)
	else:
		return requester.error("There is an error, try again", 401)

@subApp.route('/project', methods=['DELETE'])
def unsubscribeProject():
	try:
		route = "/module/{0}/{1}/{2}/{3}/project/destroygroup?format=json".format(getArg("year"), getArg("module"), getArg("instance"), getArg("activity"))
	except URLArgError as e:
		return requester.error(e.message, 401)
	req = getTokenRequest(make_route(route), "POST")
	if not req:
		return requester.error("Missing token", 401)
	result = requester.executeRequest(req)
	if result["code"] == 200:
		return requester.response(result["data"], 200)
	if "message" in result["data"]:
		return requester.error(result["data"]["message"], 401)
	elif "error" in result["data"]:
		return requester.error(result["data"]["error"], 401)
	else:
		return requester.error("There is an error, try again", 401)

@subApp.route('/project/files', methods=['GET'])
def getProjectFiles():
	try:
		route = "/module/{0}/{1}/{2}/{3}/project/file/?format=json".format(getArg("year"), getArg("module"), getArg("instance"), getArg("activity"))
	except URLArgError as e:
		return requester.error(e.message, 401)
	req = getTokenRequest(make_route(route), "POST")
	if not req:
		return requester.error("Missing token", 401)
	result = requester.executeRequest(req)
	if result["code"] == 200:
		return requester.response(result["data"], 200)
	if "message" in result["data"]:
		return requester.error(result["data"]["message"], 401)
	elif "error" in result["data"]:
		return requester.error(result["data"]["error"], 401)
	else:
		return requester.error("There is an error, try again", 401)

@subApp.route('/project/marks', methods=['GET'])
def getProjectMarks():
	try:
		route = "/module/{0}/{1}/{2}/{3}/note?format=json".format(getArg("year"), getArg("module"), getArg("instance"), getArg("activity"))
	except URLArgError as e:
		return requester.error(e.message, 401)
	req = getTokenRequest(make_route(route), "POST")
	if not req:
		return requester.error("Missing token", 401)
	result = requester.executeRequest(req)
	if result["code"] == 200:
		return requester.response(result["data"], 200)
	if "message" in result["data"]:
		return requester.error(result["data"]["message"], 401)
	elif "error" in result["data"]:
		return requester.error(result["data"]["error"], 401)
	else:
		return requester.error("There is an error, try again", 401)

@subApp.route('/allmodules', methods=['GET'])
def getModules():
	try:
		year = getArg("year")
		location = getArg("location")
		course = getArg("course")
		route = "/course/filter?format=json&preload=1&location=FR&location={0}&course={1}&scolaryear={2}".format(location, course, year)
	except URLArgError as e:
		return requester.error(e.message, 401)
	req = getTokenRequest(make_route(route), "GET")
	if not req:
		return requester.error("Missing token", 401)
	result = requester.executeRequest(req)
	if result["code"] == 200:
		return requester.response(result["data"], 200)
	if "message" in result["data"]:
		return requester.error(result["data"]["message"], 401)
	elif "error" in result["data"]:
		return requester.error(result["data"]["error"], 401)
	else:
		return requester.error("There is an error, try again", 401)

@subApp.route('/modules', methods=['GET']) #ERROR500
def getUserModules():
	try:
		login = getArg("login")
		route = "/user/{0}/notes".format(login)
	except:
		route = "/user/#!/netsoul"
	req = getTokenRequest(make_route(route + "?format=json"), "POST")
	if not req:
		return requester.error("Missing token", 401)
	req.execute()
	if req.getCode() == 200:
		raw = req.getText()
		start = raw.find("window.user = $.extend(window.user || {}, {")
		end = raw.find("notes: [")
		result = json.loads(raw[start + 54:end - 4])
		return requester.response(result, 200)
	return requester.error("Results not found", 401)

@subApp.route('/module', methods=['GET'])
def getModule():
	try:
		route = "/module/{0}/{1}/{2}?format=json".format(getArg("year"), getArg("module"), getArg("instance"))
	except URLArgError as e:
		return requester.error(e.message, 401)
	req = getTokenRequest(make_route(route), "POST")
	if not req:
		return requester.error("Missing token", 401)
	result = requester.executeRequest(req)
	if result["code"] == 200:
		return requester.response(result["data"], 200)
	if "message" in result["data"]:
		return requester.error(result["data"]["message"], 401)
	elif "error" in result["data"]:
		return requester.error(result["data"]["error"], 401)
	else:
		return requester.error("There is an error, try again", 401)

@subApp.route('/module', methods=['POST'])
def subscribeModule():
	try:
		route = "/module/{0}/{1}/{2}/register?format=json".format(getArg("year"), getArg("module"), getArg("instance"))
	except URLArgError as e:
		return requester.error(e.message, 401)
	req = getTokenRequest(make_route(route), "POST")
	if not req:
		return requester.error("Missing token", 401)
	result = requester.executeRequest(req)
	if result["code"] == 200:
		return requester.response(result["data"], 200)
	if "message" in result["data"]:
		return requester.error(result["data"]["message"], 401)
	elif "error" in result["data"]:
		return requester.error(result["data"]["error"], 401)
	else:
		return requester.error("There is an error, try again", 401)

@subApp.route('/module', methods=['DELETE'])
def unsubscribeModule():
	try:
		route = "/module/{0}/{1}/{2}/unregister?format=json".format(getArg("year"), getArg("module"), getArg("instance"))
	except URLArgError as e:
		return requester.error(e.message, 401)
	req = getTokenRequest(make_route(route), "POST")
	if not req:
		return requester.error("Missing token", 401)
	result = requester.executeRequest(req)
	if result["code"] == 200:
		return requester.response(result["data"], 200)
	if "message" in result["data"]:
		return requester.error(result["data"]["message"], 401)
	elif "error" in result["data"]:
		return requester.error(result["data"]["error"], 401)
	else:
		return requester.error("There is an error, try again", 401)

@subApp.route('/module/registered', methods=['GET'])
def registeredModule():
	try:
		route = "/module/{0}/{1}/{2}/registered?format=json".format(getArg("year"), getArg("module"), getArg("instance"))
	except URLArgError as e:
		return requester.error(e.message, 401)
	req = getTokenRequest(make_route(route), "POST")
	if not req:
		return requester.error("Missing token", 401)
	result = requester.executeRequest(req)
	if result["code"] == 200:
		return requester.response(result["data"], 200)
	if "message" in result["data"]:
		return requester.error(result["data"]["message"], 401)
	elif "error" in result["data"]:
		return requester.error(result["data"]["error"], 401)
	else:
		return requester.error("There is an error, try again", 401)

@subApp.route('/event', methods=['GET'])
def getEvent():
	try:
		route = "/module/{0}/{1}/{2}/{3}/{4}?format=json".format(getArg("year"), getArg("module"), getArg("instance"), getArg("activity"), getArg("event"))
	except URLArgError as e:
		return requester.error(e.message, 401)
	req = getTokenRequest(make_route(route), "POST")
	if not req:
		return requester.error("Missing token", 401)
	result = requester.executeRequest(req)
	if result["code"] == 200:
		return requester.response(result["data"], 200)
	if "message" in result["data"]:
		return requester.error(result["data"]["message"], 401)
	elif "error" in result["data"]:
		return requester.error(result["data"]["error"], 401)
	else:
		return requester.error("There is an error, try again", 401)

@subApp.route('/event', methods=['POST'])
def subscribeEvent():
	try:
		route = "/module/{0}/{1}/{2}/{3}/{4}/register?format=json".format(getArg("year"), getArg("module"), getArg("instance"), getArg("activity"), getArg("event"))
	except URLArgError as e:
		return requester.error(e.message, 401)
	req = getTokenRequest(make_route(route), "POST")
	if not req:
		return requester.error("Missing token", 401)
	result = requester.executeRequest(req)
	if result["code"] == 200:
		return requester.response(result["data"], 200)
	if "message" in result["data"]:
		return requester.error(result["data"]["message"], 401)
	elif "error" in result["data"]:
		return requester.error(result["data"]["error"], 401)
	else:
		return requester.error("There is an error, try again", 401)

@subApp.route('/event', methods=['DELETE'])
def unsubscribeEvent():
	try:
		route = "/module/{0}/{1}/{2}/{3}/{4}/unregister?format=json".format(getArg("year"), getArg("module"), getArg("instance"), getArg("activity"), getArg("event"))
	except URLArgError as e:
		return requester.error(e.message, 401)
	req = getTokenRequest(make_route(route), "POST")
	if not req:
		return requester.error("Missing token", 401)
	result = requester.executeRequest(req)
	if result["code"] == 200:
		return requester.response(result["data"], 200)
	if "message" in result["data"]:
		return requester.error(result["data"]["message"], 401)
	elif "error" in result["data"]:
		return requester.error(result["data"]["error"], 401)
	else:
		return requester.error("There is an error, try again", 401)

@subApp.route('/event/rdv', methods=['GET'])
def getEventSlots():
	try:
		route = "/module/{0}/{1}/{2}/{3}/rdv?format=json".format(getArg("year"), getArg("module"), getArg("instance"), getArg("activity"))
	except URLArgError as e:
		return requester.error(e.message, 401)
	req = getTokenRequest(make_route(route), "GET")
	if not req:
		return requester.error("Missing token", 401)
	result = requester.executeRequest(req)
	if result["code"] == 200:
		return requester.response(result["data"], 200)
	if "message" in result["data"]:
		return requester.error(result["data"]["message"], 401)
	elif "error" in result["data"]:
		return requester.error(result["data"]["error"], 401)
	else:
		return requester.error("There is an error, try again", 401)

@subApp.route('/event/rdv', methods=['POST'])
def subscribeEventSlot():
	try:
		team = getArg("team", False)
		if team:
			target = "id_team={0}".format(team)
		else:
			target = "login={0}".format(getArg("login"))
		route = "/module/{0}/{1}/{2}/{3}/rdv/register?id_creneau={4}&{5}&format=json".format(getArg("year"), getArg("module"), getArg("instance"), getArg("activity"), getArg("creneau"), target)
	except URLArgError as e:
		return requester.error(e.message, 401)
	req = getTokenRequest(make_route(route), "POST")
	if not req:
		return requester.error("Missing token", 401)
	result = requester.executeRequest(req)
	if result["code"] == 200:
		return requester.response(result["data"], 200)
	if "message" in result["data"]:
		return requester.error(result["data"]["message"], 401)
	elif "error" in result["data"]:
		return requester.error(result["data"]["error"], 401)
	else:
		return requester.error("There is an error, try again", 401)

@subApp.route('/event/rdv', methods=['DELETE'])
def unsubscribeEventSlot():
	try:
		team = getArg("team", False)
		if team:
			target = "id_team={0}".format(team)
			body = { "value" : { "id_creneau" : str(getArg("creneau")), "id_team" : team } }
		else:
			target = "login={0}".format(getArg("login"))
			body = { "value[0][id_creneau]" : str(getArg("creneau")), "value[0][login]" : getArg("login") }
		route = "/module/{0}/{1}/{2}/{3}/rdv/unregister?id_creneau={4}&{5}&format=json".format(getArg("year"), getArg("module"), getArg("instance"), getArg("activity"), getArg("creneau"), target)
	except URLArgError as e:
		return requester.error(e.message, 401)
	req = getTokenRequest(make_route(route), "POST", body)
	if not req:
		return requester.error("Missing token", 401)
	result = requester.executeRequest(req)
	if result["code"] == 200:
		return requester.response(result["data"], 200)
	if "message" in result["data"]:
		return requester.error(result["data"]["message"], 401)
	elif "error" in result["data"]:
		return requester.error(result["data"]["error"], 401)
	else:
		return requester.error("There is an error, try again", 401)

@subApp.route('/event/registered', methods=['GET'])
def registeredEvent():
	try:
		route = "/module/{0}/{1}/{2}/{3}/{4}/registered?format=json".format(getArg("year"), getArg("module"), getArg("instance"), getArg("activity"), getArg("event"))
	except URLArgError as e:
		return requester.error(e.message, 401)
	req = getTokenRequest(make_route(route), "POST")
	if not req:
		return requester.error("Missing token", 401)
	result = requester.executeRequest(req)
	if result["code"] == 200:
		return requester.response(result["data"], 200)
	if "message" in result["data"]:
		return requester.error(result["data"]["message"], 401)
	elif "error" in result["data"]:
		return requester.error(result["data"]["error"], 401)
	else:
		return requester.error("There is an error, try again", 401)

@subApp.route('/marks', methods=['GET'])
def getMarks():
	try:
		login = getArg("login")
		route = "/user/{0}/#!/notes".format(login)
	except:
		route = "/user/#!/netsoul"
	req = getTokenRequest(make_route(route + "?format=json"), "POST")
	if not req:
		return requester.error("Missing token", 401)
	req.execute()
	if req.getCode() == 200:
		raw = req.getText()
		start = raw.find("notes: [")
		end = raw.find("});", start)
		result = json.loads(raw[start + 7:end])
		return requester.response(result, 200)
	return requester.error("Results not found", 401)

@subApp.route('/messages', methods=['GET'])
def getMessages():
	route = "/intra/user/notification/message?format=json"
	req = getTokenRequest(make_route(route), "POST")
	if not req:
		return requester.error("Missing token", 401)
	result = requester.executeRequest(req)
	if result["code"] == 200:
		return requester.response(result["data"], 200)
	if "message" in result["data"]:
		return requester.error(result["data"]["message"], 401)
	elif "error" in result["data"]:
		return requester.error(result["data"]["error"], 401)
	else:
		return requester.error("There is an error, try again", 401)

@subApp.route('/alerts', methods=['GET'])
def getAlerts():
	route = "/intra/user/notification/alert?format=json"
	req = getTokenRequest(make_route(route), "POST")
	if not req:
		return requester.error("Missing token", 401)
	result = requester.executeRequest(req)
	if result["code"] == 200:
		return requester.response(result["data"], 200)
	if "message" in result["data"]:
		return requester.error(result["data"]["message"], 401)
	elif "error" in result["data"]:
		return requester.error(result["data"]["error"], 401)
	else:
		return requester.error("There is an error, try again", 401)

#TODO : Check if user exist
@subApp.route('/photo', methods=['GET'])
def getPhoto():
	try:
		if not checkAuth():
			return requester.error("Missing token", 401)
		login = getArg("login", "")
		result = {"url": "https://cdn.local.epitech.eu/userprofil/profilview/{0}.jpg".format(login)}
		return requester.response(result, 200)
	except URLArgError as e:
		return requester.error(e.message, 401)

#TODO : Check if rate and comment are usefull or not
@subApp.route('/token', methods=['POST'])
def setToken():
	try:
		data = json.loads(request.data)
		if "token" not in data:
			return requester.error("Missing token", 400)
		data = {"token": data["token"]}# Optional : {"rate": 1, "comment": ""}
		route = "/module/{0}/{1}/{2}/{3}/{4}/token?format=json".format(getArg("year"), getArg("module"), getArg("instance"), getArg("activity"), getArg("event"))
	except URLArgError as e:
		return requester.error(e.message, 401)
	req = getTokenRequest(make_route(route), "POST", data)
	if not req:
		return requester.error("Missing token", 401)
	result = requester.executeRequest(req)
	if result["code"] == 200:
		return requester.response(result["data"], 200)
	if "message" in result["data"]:
		return requester.error(result["data"]["message"], 401)
	elif "error" in result["data"]:
		return requester.error(result["data"]["error"], 401)
	else:
		return request.error("There's an error, try again", 401)

@subApp.route('/trombi', methods=['GET'])
def getUserList():
	route = "/user/filter/user?format=json"
	args = ["location", "year"]
	opt = ["bachelor", "promo"]
	for arg in args:
		try:
			value = getArg(arg)
			route += "&{0}={1}".format(arg, value)
		except URLArgError as e:
			return requester.error(e.message, 401)
	for arg in opt:
		try:
			value = getArg(arg)
			route += "&{0}={1}".format(arg, value)
		except:
			pass
	req = getTokenRequest(make_route(route), "POST")
	if not req:
		return requester.error("Missing token", 401)
	result = requester.executeRequest(req)
	if result["code"] == 200:
		return requester.response(result["data"], 200)
	if "message" in result["data"]:
		return requester.error(result["data"]["message"], 401)
	elif "error" in result["data"]:
		return requester.error(result["data"]["error"], 401)
	else:
		return requester.error("There is an error, try again", 401)

#TODO : Use current user's login if no arg
@subApp.route('/user', methods=['GET'])
def getUserInfos():
	try:
		login = getArg("login")
		route = "/user/{0}?format=json".format(login)
	except URLArgError as e:
		return requester.error(e.message, 401)
	req = getTokenRequest(make_route(route), "POST")
	if not req:
		return requester.error("Missing token", 401)
	result = requester.executeRequest(req)
	if result["code"] == 200:
		return requester.response(result["data"], 200)
	if "message" in result["data"]:
		return requester.error(result["data"]["message"], 401)
	elif "error" in result["data"]:
		return requester.error(result["data"]["error"], 401)
	else:
		return requester.error("There is an error, try again", 401)

#TODO : Automatically use current user's login
@subApp.route('/user/files', methods=['GET'])
def getUserFiles():
	try:
		raw = bool(getArg("raw", "false").lower() == "true")
		login = getArg("login")
		folder = getArg("folder", "")
		route = "/user/{0}/document/{1}?format=json".format(login, folder)
		print(route)
	except URLArgError as e:
		return requester.error(e.message, 401)
	req = getTokenRequest(make_route(route), "POST")
	if not req:
		return requester.error("Missing token", 401)
	result = requester.executeRequest(req)
	if result["code"] == 200:
		try:
			output = result["data"] if raw else formatter.format("document", result["data"])
			return requester.response(output, 200)
		except formatter.DataError as e:
			return requester.error(e.message, 401)
	if "message" in result["data"]:
		return requester.error(result["data"]["message"], 401)
	elif "error" in result["data"]:
		return requester.error(result["data"]["error"], 401)
	else:
		return requester.error("There is an error, try again", 401)

@subApp.route('/user/flags', methods=['GET'])
def getUserFlags():
	try:
		login = getArg("login")
		route = "/user/{0}/#!/flags/?format=json".format(login)
	except URLArgError as e:
		return requester.error(e.message, 401)
	req = getTokenRequest(make_route(route), "POST")
	if not req:
		return requester.error("Missing token", 401)
	result = requester.executeRequest(req, False)
	resTxt = req.getText()
	startPattern = "window.user = $.extend(window.user || {}, {flags: {"
	start = resTxt.find(startPattern)
	end = resTxt.find("}});")
	resTxt = '{"flags": { ' + resTxt[start + len(startPattern) : end + 2]
	if req.getCode() == 200:
		return requester.response(json.loads(resTxt.replace("\n", "").replace("\t", "")), 200)
	if "message" in result["data"]:
		return requester.error(result["data"]["message"], 401)
	elif "error" in result["data"]:
		return requester.error(result["data"]["error"], 401)
	else:
		return requester.error("There is an error, try again", 401)





#@subApp.route('/project/<pid>', methods=['GET'])
#def test(pid):
#	try:
#		route = "/module/{0}/?format=json".format(pid)
#	except URLArgError as e:
#		return requester.error(e.message, 401)
#	req = getTokenRequest(make_route(route), "POST")
#	if not req:
#		return requester.error("Missing token", 401)
#	result = requester.executeRequest(req)
#	if result["code"] == 200:
#		return requester.response(result["data"], 200)
#	return requester.error(result["data"]["message"], 401)
