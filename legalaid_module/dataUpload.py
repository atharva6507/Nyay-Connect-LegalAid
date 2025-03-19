import pandas as pd
from pinecone import Pinecone
import uuid
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_LEGALAID_API_KEY")

# Initialize Pinecone client
pc = Pinecone(api_key=PINECONE_API_KEY)

# Ensure index exists
try:
    index_list = pc.list_indexes()
    if "probono-lawyers-index" not in index_list:
        pc.create_index_for_model(
            name="probono-lawyers-index",
            cloud="aws",
            region="us-east-1",
            embed={
                "model": "llama-text-embed-v2",
                "field_map": {
                    "text": "expertise_text"  # Field to embed
                }
            }
        )
        print("Index 'probono-lawyers-index' created successfully.")
    else:
        print("Index already exists.")
except Exception as e:
    print(f"Index creation error: {e}")
    print("Continuing with existing index...")

# Connect to Pinecone index
try:
    index = pc.Index("probono-lawyers-index")
    print("Connected to Pinecone index successfully.")
except Exception as e:
    print(f"Failed to connect to index: {e}")
    exit(1)  # Stop execution if index connection fails

def dump_probono_data(file_path="resource/probono_lawyers.csv"):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return
        
    data = pd.read_csv(file_path)
    print(f"Loaded {len(data)} records from CSV.")
    
    records = []
    for _, row in data.iterrows():
        record = {
            "id": str(uuid.uuid4()),
            "name": str(row["Name"]) if pd.notna(row["Name"]) else "Unknown",
            "place": str(row["Place"]) if pd.notna(row["Place"]) else "Unknown",
            "email": str(row["Email"]) if pd.notna(row["Email"]) else "Not Available",
            "expertise_text": str(row["Expertise"]) if pd.notna(row["Expertise"]) else "General Law"
        }
        records.append(record)
    
    batch_size = 50
    for i in range(0, len(records), batch_size):
        batch = records[i:i+batch_size]
        try:
            index.upsert_records(
                namespace="ns1",
                records=batch  # Store everything as fields
            )
            print(f"Uploaded batch {i//batch_size + 1}/{(len(records)-1)//batch_size + 1}")
        except Exception as e:
            print(f"Error uploading batch {i//batch_size + 1}: {e}")
            if batch:
                print(f"Sample record causing error: {batch[0]}")

    print("Data upload completed!")

if __name__ == "__main__":
    dump_probono_data()
