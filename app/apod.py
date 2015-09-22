import urllib, json

def get_apod():
	data = json.load(urllib.urlopen("https://api.nasa.gov/planetary/apod?api_key=3VDBYresFKk8DruDWqepKl5KHez4fu81Vo0Njx5C&format=JSON"))
	return data['url']