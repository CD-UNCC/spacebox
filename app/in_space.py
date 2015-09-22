import json, urllib
from flask import Markup

def in_space():
	html = ''
	page = urllib.urlopen('http://api.open-notify.org/astros.json')
	data = json.loads(page.read())
	for i in data['people']:
		html = html + '<li>' + i['name'] + ': ' + i['craft'] + '</li>'
	return Markup(html)
