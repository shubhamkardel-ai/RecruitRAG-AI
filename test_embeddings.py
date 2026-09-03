from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Create an embedding
text = "Python developer with experience in machine learning"
embedding = model.encode(text)

print("Embedding created successfully!")
print("Vector dimension:", len(embedding))
