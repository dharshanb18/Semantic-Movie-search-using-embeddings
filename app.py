from flask import Flask, render_template, request
import pymongo
import requests

app = Flask(__name__)

# MongoDB connection
client = pymongo.MongoClient("mongodb+srv://dharshan:WHJo0D8U5RwID1ph@cluster0.oewot.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.sample_mflix
collection = db.movies

hf_token = "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"
embedding_url = "https://api-inference.huggingface.co/pipeline/feature-extraction/sentence-transformers/all-MiniLM-L6-v2"

# Generate embedding using Hugging Face API
def generate_embedding(text: str) -> list:
    response = requests.post(
        embedding_url,
        headers={"Authorization": f"Bearer {hf_token}"},
        json={"inputs": text}
    )
    return response.json()

# Home route (index) for rendering the form and showing results
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form.get('query')
        k = int(request.form.get('k', 4))  # Default to 4 if not provided
        threshold = float(request.form.get('threshold', 0))  # Default to 0 if not provided
        
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

# Health route
@app.route('/health', methods=['GET'])
def health():
    return "Server is running"

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
