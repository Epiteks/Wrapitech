#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import json
import time
import urllib2

debug = True
url = "http://epitech.hug33k.fr"

def	getUser(token, login):
	try:
		route = url + "/user?token={0}&user={1}".format(token, login)
		req = urllib2.Request(route)
		resp = urllib2.urlopen(req)
		content = resp.read()
		return json.loads(content)
	except Exception as e:
		if debug:
			print("Erreur")
			print(e)
			print(login)
		time.sleep(1)
		return getUser(token, login)

# def	getCityUsers(token, city, year=2015):
# 	try:
# 		route = url + "/trombi?token={0}&year={1}&location={2}&promo=tek3".format(token, year, city)
# 		req = urllib2.Request(route)
# 		resp = urllib2.urlopen(req)
# 		content = resp.read()
# 		return json.loads(content)
# 	except Exception as e:
# 		print("Erreur")
# 		print(e)
# 		sys.exit(42)

def	getIntraUsers(token, year):
	users = []
	# city = ["FR/BDX","FR/LIL","FR/LYN","FR/MAR","FR/MPL","FR/NCY","FR/NAN","FR/NCE","FR/PAR","FR/REN","FR/STG","FR/TLS"]
	# for item in city:
		# tmp = getCityUsers(token, item)
		# for user in tmp["items"]:
			# users.append(user)
		# if debug:
			# print("{0} done".format(item))
			# print("{0} users".format(len(tmp["items"])))
	try:
		route = "http://ws.paysdu42.fr/JSON/?action=get_logins&auth_login=schoch_h&auth_password=XS4suq,e&school=epitech&promo={0}".format(year)
		req = urllib2.Request(route)
		resp = urllib2.urlopen(req)
		content = resp.read()
		data = json.loads(content)
	except Exception as e:
		if debug:
			print("Erreur")
			print(e)
	for user in data["result"]:
		users.append(user)
	if debug:
		# print("All cities done")
		print("Total : {0} users".format(len(users)))
	return users

def cleanList(users):
	res = []
	index = 0
	for user in users:
		try:
			intraData = getUser(token, user)
			#intraData["studentyear"] == 3 and
			if not intraData["close"] and "gpa" in intraData and len(intraData["gpa"]) and "gpa" in intraData["gpa"][0]:
				res.append(intraData)
		except:
			pass
		index += 1
		if not (index % 10):
			print("{0} done".format(index))
	return res

def	getGPA(users):
	allUsers = []
	for user in users:
		try:
			gpa = float(user["gpa"][0]["gpa"])
			city = user["location"]
			allUsers.append({"login": user["login"],
							"gpa": str(gpa),
							"city": city})
		except:
			pass
	return allUsers

def save(users, year):
	name = "rank{0}.json".format(year)
	with open(name, "w") as dataFile:
		dataFile.write(json.dumps(users))

if __name__ == '__main__':
	token = "3vs1vuu4ioc49cbiu1l2qjusn0"
	for year in ["2016", "2017", "2018", "2019", "2020"]:
		users = getIntraUsers(token, year)
		users = cleanList(users)
		if debug:
			print(len(users))
		allUsers = getGPA(users)
		save(allUsers, year)
