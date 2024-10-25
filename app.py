from flask import Flask, render_template, request
import pymongo
import requests

app = Flask(__name__)

# MongoDB connection
client = pymongo.MongoClient("mongodb+srv://<password>@cluster0.oewot.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.sample_mflix
collection = db.movies

hf_token = "your api key"
embedding_url = "https://api-inference.huggingface.co/pipeline/feature-extraction/sentence-transformers/all-MiniLM-L6-v2"

# Generate embedding
def generate_embedding(text: str) -> list:
    response = requests.post(
        embedding_url,
        headers={"Authorization": f"Bearer {hf_token}"},
        json={"inputs": text}
    )
    return response.json()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form.get('query')
        k = int(request.form.get('k', 4))
        threshold = float(request.form.get('threshold', 0))
        
        results = collection.aggregate([
            {"$vectorSearch": {
                "queryVector": generate_embedding(query),
                "path": "plot_embedding_hf",
                "numCandidates": 100,
                "limit": k,
                "index": "plotSemanticSearch",
            }}
        ])

        return render_template('index.html', results=results, query=query)
    
    return render_template('index.html', results=None)

@app.route('/health', methods=['GET'])
def health():
    return "Server is running"

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
