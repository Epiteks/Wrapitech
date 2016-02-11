from flask import Blueprint, request
import json
import hmac
import hashlib
import requester

subApp = Blueprint('blih', __name__)

def getCredentials():
	login = request.args.get('login')
	password = request.args.get('password')
	return (login != None and password != None), login, password

def	make_route(route):
	return "https://blih.epitech.eu" + route

def	make_body(login, password, data=None):
	password = bytearray(str(password), 'utf8')
	hash_signature = hmac.new(password, msg=bytearray(login, 'utf-8'), digestmod=hashlib.sha512)
	if data:
		hash_signature.update(bytearray(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')), 'utf8'))
	signature = hash_signature.hexdigest()
	result = {"user": login, "signature": signature}
	if data:
		result["data"] = data
	return result

@subApp.route('/', methods=['GET'])
def root():
	return requester.response({"status": True}, 200)

@subApp.route('/repository', methods=['GET'])
def getRepositoriesList():
	status, login, password = getCredentials()
	if not status:
		return requester.error("Missing credentials", 401)
	req = requester.Request(make_route("/repositories"), "GET", make_body(login, password))
	result = requester.executeRequest(req)
	repositories = []
	if result["code"] == 200:
		for repo in result["data"]["repositories"]:
			repositories.append(repo)
	repositories.sort(key=lambda x:x.lower())
	return requester.response(repositories, (200 if result["code"] in [200, 404] else result["code"]))

@subApp.route('/repository', methods=['POST'])
def newRepository():
	status, login, password = getCredentials()
	if not status:
		return requester.error("Missing credentials", 401)
	try:
		data = json.loads(request.data)
		if "name" not in data:
			return requester.error("Missing name", 400)
		if type(data["name"]) != str:
			return requester.error("Wrong name format", 400)
		repo = {"name": data["name"], "type": "git", "description": ("" if "description" not in data else data["description"])}
	except:
		return requester.error("Wrong body format", 400)
	req = requester.Request(make_route("/repositories"), "POST", make_body(login, password, repo))
	result = requester.executeRequest(req)
	return requester.response(result["data"], result["code"])

@subApp.route('/repository/<repo>', methods=['GET'])
def getRepositoryInfo(repo):
	status, login, password = getCredentials()
	if not status:
		return requester.error("Missing credentials", 401)
	req = requester.Request(make_route("/repository/{0}".format(repo)), "GET", make_body(login, password))
	result = requester.executeRequest(req)
	data = result["data"]["message"]
	data["name"] = repo
	return requester.response(data, result["code"])

@subApp.route('/repository/<repo>', methods=['DELETE'])
def deleteRepository(repo):
	status, login, password = getCredentials()
	if not status:
		return requester.error("Missing credentials", 401)
	req = requester.Request(make_route("/repository/{0}".format(repo)), "DELETE", make_body(login, password))
	result = requester.executeRequest(req)
	return requester.response(result["data"], result["code"])

@subApp.route('/repository/<repo>/acls', methods=['GET'])
def getRepositoryACL(repo):
	status, login, password = getCredentials()
	if not status:
		return requester.error("Missing credentials", 401)
	req = requester.Request(make_route("/repository/{0}/acls".format(repo)), "GET", make_body(login, password))
	result = requester.executeRequest(req)
	data = []
	if result["code"] == 200:
		for login in result["data"]:
			rights = result["data"][login]
			user = {"login": login,
					"read": ("r" in rights),
					"write": ("w" in rights),
					"admin": ("a" in rights)}
			data.append(user)
	data.sort(key=lambda x:x["login"].lower())
	return requester.response(data, (200 if result["code"] in [200, 404] else result["code"]))

@subApp.route('/repository/<repo>/acls/<user>', methods=['GET'])
def getRepositoryUserACL(repo, user):
	status, login, password = getCredentials()
	if not status:
		return requester.error("Missing credentials", 401)
	result = getRepositoryACL(repo)
	if int(result.status[:3]) != 200:
		return requester.error(result.requester.response[0], 404)
	users = json.loads(result.requester.response[0])
	result = filter(lambda x:x["login"].lower() == str(user), users)
	result = result[0] if len(result) else {"requester.error": "User not found"}
	return requester.response(result, (200 if "login" in result else 404))

@subApp.route('/repository/<repo>/acls/<user>', methods=['POST'])
def setRepositoryUserACL(repo, user):
	status, login, password = getCredentials()
	if not status:
		return requester.error("Missing credentials", 401)
	try:
		data = json.loads(request.data)
		acl = ""
		acl += ("a" if ("admin" in data and data["admin"]) else "")
		acl += ("w" if ("write" in data and data["write"]) else "")
		acl += ("r" if ("read" in data and data["read"]) else "")
		rights = {"user": user,
					"acl": acl}
	except:
		return requester.error("Missing key", 400)
	req = requester.Request(make_route("/repository/{0}/acls".format(repo)), "POST", make_body(login, password, rights))
	result = requester.executeRequest(req)
	return requester.response(result["data"], result["code"])

@subApp.route('/sshkey', methods=['GET'])
def getSSHKeysList():
	status, login, password = getCredentials()
	if not status:
		return requester.error("Missing credentials", 401)
	req = requester.Request(make_route("/sshkeys"), "GET", make_body(login, password))
	result = requester.executeRequest(req)
	keys = []
	if result["code"] == 200:
		for single in result["data"]:
			key = {"name": single, "key": result["data"][single]}
			keys.append(key)
		keys.sort(key=lambda x:x["name"].lower())
	return requester.response(keys, (200 if result["code"] in [200, 404] else result["code"]))

@subApp.route('/sshkey', methods=['POST'])
def newSSHKey():
	status, login, password = getCredentials()
	if not status:
		return requester.error("Missing credentials", 401)
	try:
		key = {"sshkey": json.loads(request.data)["key"]}
	except:
		return requester.error("Missing key", 400)
	req = requester.Request(make_route("/sshkeys"), "POST", make_body(login, password, key))
	result = requester.executeRequest(req)
	return requester.response(result["data"], result["code"])

@subApp.route('/sshkey/<key>', methods=['DELETE'])
def deleteSSHKey(key):
	status, login, password = getCredentials()
	if not status:
		return requester.error("Missing credentials", 401)
	req = requester.Request(make_route("/sshkey/{0}".format(key)), "DELETE", make_body(login, password))
	result = requester.executeRequest(req)
	return requester.response(result["data"], result["code"])

@subApp.route('/test', methods=['GET'])
def testConnection():
	status, login, password = getCredentials()
	if not status:
		return requester.error("Missing credentials", 401)
	req = requester.Request(make_route("/whoami"), "GET", make_body(login, password))
	result = requester.executeRequest(req)
	return requester.response({"status": (result["code"] == 200)}, result["code"])
