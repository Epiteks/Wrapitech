from flask import Blueprint
import news
import requester

subApp = Blueprint('other', __name__)

@subApp.route('/', methods=['GET'])
def root():
	return requester.response({"status": True}, 200)

@subApp.route('/news', methods=['GET'])
def getNews():
	journal = news.Journal()
	return requester.response(journal.getNews(), 200)

@subApp.route('/version', methods=['GET'])
def getVersion():
	with open(".version", "r") as vFile:
		nb = vFile.read()
	return requester.response({"version": nb}, 200)
