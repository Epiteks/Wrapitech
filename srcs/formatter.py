class DataError(Exception):

	def __init__(self, value):
		self.message = value
		self.value = "Data Error : " + self.message

	def __str__(self):
		return repr(self.value)

def _document(data):
	for index in range(0, len(data)):
		uselessKeys = ["type", "synchro", "noFolder", "archive", "isLeaf"]
		try:
			itemType = data[index]["type"]
			data[index]["isFolder"] = bool(itemType == "d")
			for key in uselessKeys:
				del data[index][key]
		except Exception as e:
			raise DataError(e.str())
	return data

def format(dataType, data):
	if dataType == "document":
		return _document(data)