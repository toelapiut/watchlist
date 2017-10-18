from flask import render_template, request, redirect, url_for
from app import app
from .request import get_movies,get_movie, search_movie

@app.route('/')

def index():
   ##Getting popular movies
	popular_movies=get_movies('popular')
	upcoming_movie=get_movies('upcoming')
	now_showing_movie=get_movies("now_playing")

	print(popular_movies)
	title="Home Welcome to the best movie review website online"

	search_movie = request.args.get('movie_query')

	if search_movie:
  		return redirect(url_for('search', movie_name = search_movie))
	else: 
		return render_template("index.html",title=title, popular= popular_movies,upcoming= upcoming_movie, now_showing = now_showing_movie)



@app.route('/movie/<int:id>')
def movie(id):

	movie=get_movie(id)
	title=f"{movie.title}"

	return render_template("movie.html",title=title,movie=movie)

@app.route('/search/<movie_name>')
def search(movie_name):
	"""
	View function to display the search results
	"""
	movie_name_list = movie_name.split(" ")
	movie_name_format = "+".join(movie_name_list)
	searched_movies = search_movie(movie_name_format)
	title = f'search results for {movie_name}'
	return render_template('search.html', movies = searched_movies)