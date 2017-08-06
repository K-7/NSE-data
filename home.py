import random
import string
import os, os.path
import time
import json
from cherrypy.process.plugins import Daemonizer
import cherrypy
from scrap import RedisStore

# json_data = {"time":"Aug 04, 2017 15:59:59","data":[{"symbol":"IOC","series":"EQ","openPrice":"395.00","highPrice":"426.80","lowPrice":"393.00","ltp":"418.00","previousPrice":"387.05","netPrice":"8.00","tradedQuantity":"1,56,08,306","turnoverInLakhs":"63,449.32","lastCorpAnnouncementDate":"18-Aug-2017","lastCorpAnnouncement":"Annual General Meeting\/Dividend - Re 1\/- Per Share"},{"symbol":"BPCL","series":"EQ","openPrice":"491.40","highPrice":"525.50","lowPrice":"491.00","ltp":"518.75","previousPrice":"490.00","netPrice":"5.87","tradedQuantity":"54,06,360","turnoverInLakhs":"27,302.66","lastCorpAnnouncementDate":"13-Jul-2017","lastCorpAnnouncement":"Bonus 1:2"},{"symbol":"TATASTEEL","series":"EQ","openPrice":"559.40","highPrice":"580.80","lowPrice":"559.30","ltp":"580.80","previousPrice":"559.30","netPrice":"3.84","tradedQuantity":"33,63,291","turnoverInLakhs":"19,166.72","lastCorpAnnouncementDate":"20-Jul-2017","lastCorpAnnouncement":"Annual General Meeting\/Dividend - Rs 10\/- Per Share"},{"symbol":"EICHERMOT","series":"EQ","openPrice":"30,665.00","highPrice":"31,925.00","lowPrice":"30,500.00","ltp":"31,700.00","previousPrice":"30,726.05","netPrice":"3.17","tradedQuantity":"47,523","turnoverInLakhs":"14,839.09","lastCorpAnnouncementDate":"31-Jul-2017","lastCorpAnnouncement":"Annual General Meeting\/Dividend - Rs 100\/- Per Share"},{"symbol":"COALINDIA","series":"EQ","openPrice":"242.00","highPrice":"250.20","lowPrice":"238.45","ltp":"249.20","previousPrice":"241.75","netPrice":"3.08","tradedQuantity":"65,73,068","turnoverInLakhs":"16,067.86","lastCorpAnnouncementDate":"27-Mar-2017","lastCorpAnnouncement":"Interim Dividend Rs 1.15 Per Share (Purpose Revised)"},{"symbol":"VEDL","series":"EQ","openPrice":"279.90","highPrice":"289.90","lowPrice":"278.10","ltp":"288.40","previousPrice":"279.95","netPrice":"3.02","tradedQuantity":"1,01,01,816","turnoverInLakhs":"28,899.28","lastCorpAnnouncementDate":"06-Jul-2017","lastCorpAnnouncement":"Annual General Meeting"},{"symbol":"HEROMOTOCO","series":"EQ","openPrice":"3,836.00","highPrice":"3,964.00","lowPrice":"3,816.40","ltp":"3,944.25","previousPrice":"3,838.35","netPrice":"2.76","tradedQuantity":"7,89,172","turnoverInLakhs":"30,890.80","lastCorpAnnouncementDate":"30-Jun-2017","lastCorpAnnouncement":"Annual General Meeting\/Dividend - Rs 30\/- Per Share"},{"symbol":"GAIL","series":"EQ","openPrice":"372.00","highPrice":"384.00","lowPrice":"370.00","ltp":"380.60","previousPrice":"370.55","netPrice":"2.71","tradedQuantity":"31,98,095","turnoverInLakhs":"12,013.00","lastCorpAnnouncementDate":"31-Aug-2017","lastCorpAnnouncement":"Dividend - Rs 2.70 Per Share"},{"symbol":"NTPC","series":"EQ","openPrice":"172.35","highPrice":"178.20","lowPrice":"169.60","ltp":"177.00","previousPrice":"172.55","netPrice":"2.58","tradedQuantity":"77,09,552","turnoverInLakhs":"13,456.25","lastCorpAnnouncementDate":"15-Feb-2017","lastCorpAnnouncement":"Interim Dividend Rs 2.61\/- Per Share (Purpose Revised)"},{"symbol":"HINDALCO","series":"EQ","openPrice":"218.35","highPrice":"225.90","lowPrice":"218.35","ltp":"225.45","previousPrice":"220.95","netPrice":"2.04","tradedQuantity":"57,60,887","turnoverInLakhs":"12,866.37","lastCorpAnnouncementDate":"05-Sep-2017","lastCorpAnnouncement":"Annual General Meeting\/Dividend - Rs 1.10 Per Share"}]}

class LandingPage(object):
    @cherrypy.expose
    def index(self):
        return open('home.html')

    @cherrypy.expose
    def get_data(self):
    	store = RedisStore()
    	gainers_data = json.loads(store.get("gainers"))
    	losers_data = json.loads(store.get("losers"))
    	data = {"gainers_data":gainers_data['data'],"losers_data":losers_data['data'], "time":gainers_data['time']}
        return json.dumps(data)


if __name__ == '__main__':
	cherrypy.config.update({
        'server.socket_host': '0.0.0.0',
        'server.socket_port': 8000,
        'environment': 'production',
        'log.screen': True,
        'show_tracebacks': True,
        'log.error_file': 'site.log',
	})
	
	conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }

	# Daemonizer(cherrypy.engine).subscribe()
	cherrypy.quickstart(LandingPage(), '/', conf)