import random
import string
import redis
import cherrypy
import requests
from celery import Celery
from datetime import timedelta


CELERYBEAT_SCHEDULE = {
    "poll_SO": {
        "task": "scrap.nse_data",
        "schedule": timedelta(seconds=30),
        "args": []
    }
}
app = Celery("NSE", broker='redis://guest@localhost//')
app.config_from_object("scrap")

class RedisStore(object):

	def __init__(self):
		self.r = redis.StrictRedis(host='localhost', port=6379, db=0)

	def set(self, key, data):
		self.r.set(key, data)

	def get(self, key):
		return self.r.get(key)

@app.task
def nse_data():
	store = RedisStore()
	gainers_url = "https://www.nseindia.com/live_market/dynaContent/live_analysis/gainers/niftyGainers1.json"
	losers_url = "https://www.nseindia.com/live_market/dynaContent/live_analysis/losers/niftyLosers1.json"
	gainers_req = requests.get(gainers_url)
	store.set("gainers",gainers_req.content)
	losers_req = requests.get(losers_url)
	store.set("losers",losers_req.content)
	print store.get("gainers")
	print "=================="
	print store.get("losers")
	
