import json

class Journal(object):
	"""docstring for Journal"""
	def __init__(self):
		super(Journal, self).__init__()
		self._news = {}
		self.refresh()

	def refresh(self):
		self._news = _temporaryJournal()
		pass

	def getNews(self):
		return self._news

def _temporaryJournal():
	with open("news.json") as news:
		result = json.load(news)
	if type(result) is dict:
		result = [result]
	return result
