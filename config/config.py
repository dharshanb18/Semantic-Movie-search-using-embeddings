import os

class Config:
    # MongoDB configuration
    MONGO_URI = os.environ.get('MONGO_URI', 'mongodb+srv://dharshan:WHJo0D8U5RwID1ph@cluster0.oewot.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
    DB_NAME = os.environ.get('DB_NAME', 'sample_mflix')

    # Hugging Face API Configuration
    HF_TOKEN = os.environ.get('HF_TOKEN', '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')
    EMBEDDING_URL = 'https://api-inference.huggingface.co/pipeline/feature-extraction/sentence-transformers/all-MiniLM-L6-v2'
