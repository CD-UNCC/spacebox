import json
import urllib
from flask import Markup
def get_news():
	results = json.load(urllib.urlopen("https://www.kimonolabs.com/api/3rawroxe?apikey=a0OfY1qbs4Nn8a0cfkeuUzCOwOQzn1s8"))
	data = results['results']['news']
	marquee = ''
	for i in range(len(data)):
		pass
		#marquee = marquee + '<a href="{0}">{1}</a>{2}'.format(data[i]['headline']['href'],data[i]['headline']['text'], '&nbsp;'*10)
	return Markup(marquee)