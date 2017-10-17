import unittest
from .models import movie
Movie = movie.Movie

class MovieTest(unittest.TestCase):
	""" 
	Test Class to test the behaviour of the movie class
	"""
	def setUp(self):
		"""Set up method taht will run before every Test
		"""
		self.new_movie = Movie(1234, 'Python must be crazy', 'A thrilling new python series', 'https://developers.themoviedb.org/3/getting-started/images/khsjha27hbs', 8.5,129993)

	def test_instance(self):
		self.assertTrue(isinstance(self.new_movie,Movie))

	def test_init(self):
		self.assertEqual(self.new_movie.id,1234)
		self.assertEqual(self.new_movie.title,"Python must be crazy")
		self.assertEqual(self.new_movie.overview,"A thrilling new python series")
		self.assertEqual(self.new_movie.image,'https://developers.themoviedb.org/3/getting-started/imageshttps://developers.themoviedb.org/3/getting-started/images/khsjha27hbs')
		self.assertEqual(self.new_movie.vote_average,8.5)
		self.assertEqual(self.new_movie.vote_count,129993)

if __name__ == '__main__':
	unittest.main()