from flask import Blueprint, request, render_template
from .search import search_movies
from app import db

bp = Blueprint('api', __name__)

@bp.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form.get('query')
        movie_collection = db.movies
        results = search_movies(query, movie_collection)

        # Render results on the HTML page
        return render_template('search.html', results=results, query=query)

    # For GET request, render the search form
    return render_template('search.html', results=None)
