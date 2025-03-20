import os
import json
from dotenv import load_dotenv
from pinecone import Pinecone
from legalaid_module.cleanJson import cleanjson

# Load environment variables
load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_LEGALAID_API_KEY")
PINECONE_LEGALAID_HOST = os.getenv("PINECONE_LEGALAID_HOST")

# Initialize Pinecone client
pc = Pinecone(api_key=PINECONE_API_KEY)

# Define the index with the appropriate host
index = pc.Index(host=PINECONE_LEGALAID_HOST)  # Replace with actual host

def find_relevant_lawyers(query, top_k=5):
    if not query.strip():
        return json.dumps({"error": "Query cannot be empty."})

    results = index.search_records(
        namespace="ns1",
        query={"inputs": {"text": query}, "top_k": top_k},
        fields=["name", "place", "email", "contact_number", "expertise_text"]
    )

    # Convert response to dictionary
    results_dict = results.to_dict()

    # Extract hits from the correct path
    hits = results_dict.get("result", {}).get("hits", [])

    if not hits:
        return json.dumps({"error": "No relevant lawyers found."})

    # Ensure we respect the `top_k` limit
    hits = hits[:top_k]

    lawyers = []
    for match in hits:
        fields = match.get("fields", {})  # Extract metadata
        lawyer = {
            "name": fields.get("name", "Unknown"),
            "place": fields.get("place", "Unknown"),
            "email": fields.get("email", "Not Available"),
            "contact_number": fields.get("contact_number", "Not Available"),
            "expertise": fields.get("expertise_text", "General Law")
        }
        lawyers.append(lawyer)

    response = json.dumps({"lawyers": lawyers}, indent=4)
    return cleanjson(response)


# def main():
#     query = input()
#     print(find_relevant_lawyers(query))

# if __name__ == "__main__":
#     main()
