import os
import logging
from logging.handlers import RotatingFileHandler
from app import app as app
import requester

levels = {"INFO": logging.INFO,
			"ERROR": logging.ERROR,
			"WARNING": logging.WARNING}

def getLevel():
	try:
		level = os.environ["EPITECH_API_LOGGER_LEVEL"]
		if level in levels:
			return levels[level]
		else:
			return logging.INFO
	except:
		return logging.INFO

logger = RotatingFileHandler('api.log', backupCount=500)
logger.setLevel(getLevel())
logger.format("[%(asctime)s] {%(pathname)s:%(lineno)d} ~%(levelname)s~ - %(message)s")
try:
	slackLevel = os.environ["EPITECH_API_SLACK_LEVEL"]
	slackURL = "https://hooks.slack.com/services/" + os.environ["EPITECH_API_SLACK_TOKEN"]
except:
	slackLevel = False
	slackURL = None

def toSlack(message):
	message = message.replace("~WARNING~", ":bangbang:").replace("~ERROR~", ":exclamation:").replace("~INFO~", ":information_source:")
	if not slackLevel or not slackURL:
		return
	res = requester.post(slackURL, {"text": message}, parse=False)
	print(res)

def formatMessage(message, level):
	return "[{0}] {1}".format(level, message)

def warning(message):
	message = formatMessage(message, "WARNING")
	app.logger.warning(message)
	if slackLevel:
		toSlack(message)

def error(message):
	message = formatMessage(message, "ERROR")
	app.logger.error(message)
	if slackLevel in ["INFO", "ERROR"]:
		toSlack(message)

def info(message):
	message = formatMessage(message, "INFO")
	app.logger.info(message)
	if slackLevel == "INFO":
		toSlack(message)
