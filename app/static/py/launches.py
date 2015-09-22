import json, urllib

def get_launches():
	results = json.load(urllib.urlopen("https://www.kimonolabs.com/api/ddi9jle8?apikey=a0OfY1qbs4Nn8a0cfkeuUzCOwOQzn1s8"))
	data = results['results']['launches']
	return data
