from flask import Flask, render_template, Markup
from in_space import in_space
from launches import get_launches
from news import get_news 
from apod import get_apod
import os
app = Flask(__name__)      
 
@app.route('/index')
@app.route('/')
def home():
  	return render_template('index.html', string = in_space(), apod_pic = get_apod())

@app.route('/news')
def news():
	return render_template('news.html', apod_pic = get_apod())

@app.route('/launches')
def launches():
	return render_template('launches.html', launches = get_launches(), apod_pic = get_apod())


if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)





#https://api.nasa.gov/planetary/apod?api_key=3VDBYresFKk8DruDWqepKl5KHez4fu81Vo0Njx5C&format=JSON