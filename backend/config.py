import os

class Config:
    # Flask Configuration
    FLASK_APP = os.getenv('FLASK_APP', 'app.py')
    FLASK_ENV = os.getenv('FLASK_ENV', 'production')
    DEBUG = os.getenv('DEBUG', 'False') == 'True'

    # Ollama API Configuration
    OLLAMA_URL = os.getenv('OLLAMA_URL', 'http://localhost:11434/api/generate')

    # Neo4j Database Configuration
    NEO4J_URI = os.getenv('NEO4J_URI', 'bolt://localhost:7687')
    NEO4J_USER = os.getenv('NEO4J_USER', 'neo4j')
    NEO4J_PASSWORD = os.getenv('NEO4J_PASSWORD', 'testneo4j')

    # Secret Key for Flask sessions
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key')

    # Logging Configuration
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')

