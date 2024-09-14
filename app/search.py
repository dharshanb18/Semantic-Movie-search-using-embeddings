import requests
from flask import current_app

def generate_embedding(text: str) -> list[float]:
    response = requests.post(
        current_app.config['EMBEDDING_URL'],
        headers={"Authorization": f"Bearer {current_app.config['HF_TOKEN']}"},
        json={"inputs": text}
    )
    return response.json()

def search_movies(query: str, collection, limit: int = 4):
    embedding = generate_embedding(query)
    
    results = collection.aggregate([
        {"$vectorSearch": {
            "queryVector": embedding,
            "path": "plot_embedding_hf",
            "numCandidates": 100,
            "limit": limit,
            "index": "plotSemanticSearch",
        }}
    ])

    return results
