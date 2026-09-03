import os
from dotenv import load_dotenv
from qdrant_client import QdrantClient

# Load environment variables
load_dotenv()

# Get Qdrant credentials
qdrant_url = os.getenv("QDRANT_URL")
qdrant_api_key = os.getenv("QDRANT_API_KEY")

# Connect to Qdrant Cloud
client = QdrantClient(
    url=qdrant_url,
    api_key=qdrant_api_key
)

# Test connection
collections = client.get_collections()

print("✅ Qdrant connection successful!")
print("Collections:", collections)