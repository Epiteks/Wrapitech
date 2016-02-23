from flask import Blueprint, request#, Response
import json
import requester

subApp = Blueprint('intra', __name__)

def	make_route(route):
	return "https://intra.epitech.eu" + route

def	getTokenRequest(url, method, data=None):
	req = requester.Request(url, method, data)
	req.setCookie("PHPSESSID", request.args.get("token"))
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
	pass

@subApp.route('/susies', methods=['GET'])
def getSusies():
	pass

@subApp.route('/susie', methods=['GET'])
def getSusie():
	pass

@subApp.route('/susie', methods=['POST'])
def subscribeSusie():
	pass

@subApp.route('/susie', methods=['DELETE'])
def unsubscribeSusie():
	pass

@subApp.route('/projects', methods=['GET'])
def getProjects():
	pass

@subApp.route('/project', methods=['GET'])
def getProject():
	pass

@subApp.route('/project', methods=['POST'])
def subscribeProject():
	pass

@subApp.route('/project', methods=['DELETE'])
def unsubscribeProject():
	pass

@subApp.route('/project/files', methods=['GET'])
def getProjectFiles():
	pass

@subApp.route('/modules', methods=['GET'])
def getUserModules():
	pass

@subApp.route('/allmodules', methods=['GET'])
def getModules():
	pass

@subApp.route('/module', methods=['GET'])
def getModule():
	pass

@subApp.route('/module', methods=['POST'])
def subscribeModule():
	pass

@subApp.route('/module', methods=['DELETE'])
def unsubscribeModule():
	pass

@subApp.route('/event', methods=['GET'])
def getEvent():
	pass

@subApp.route('/event', methods=['POST'])
def subscribeEvent():
	pass

@subApp.route('/event', methods=['DELETE'])
def unsubscribeEvent():
	pass

@subApp.route('/marks', methods=['GET'])
def getMarks():
	pass

@subApp.route('/messages', methods=['GET'])
def getMessages():
	pass

@subApp.route('/alerts', methods=['GET'])
def getAlerts():
	pass

@subApp.route('/photo', methods=['GET'])
def getPhoto():
	pass

@subApp.route('/token', methods=['POST'])
def setToken():
	pass

@subApp.route('/trombi', methods=['GET'])
def getUserList():
	pass
