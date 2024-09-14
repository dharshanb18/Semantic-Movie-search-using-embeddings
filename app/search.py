import requests
from flask import current_app

def generate_embedding(text: str) -> list[float]:
    response = requests.post(
        current_app.config['EMBEDDING_URL'],
        headers={"Authorization": f"Bearer {current_app.config['HF_TOKEN']}"},
        json={"inputs": text}
    )
    return response.json()

def search_movies(query, movie_collection):
    query_embedding = generate_embedding(query)
    results = movie_collection.aggregate([
        {
            "$vectorSearch": {
                "queryVector": query_embedding,
                "path": "plot_embedding_hf",
                "numCandidates": 10,
                "limit": 4,
                "index": "plotSemanticSearch",
            }
        }
    ])
    return [{"title": movie.get("title", "No Title"), "plot": movie.get("plot", "No Plot")} for movie in results]
