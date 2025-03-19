# Nyay-Connect

Nyay-Connect is a legal aid platform that leverages AI-powered search capabilities using Pinecone for efficient and accurate retrieval of legal resources. This project aims to connect users with relevant legal assistance and information.

## 🚀 Features

- **FastAPI Backend** - A high-performance API built using FastAPI.
- **Pinecone Integration** - Utilizes Pinecone for semantic search and vector indexing.
- **Legal Aid Module** - Organizes and retrieves legal information efficiently.
- **Environment Variables** - Uses `.env` to manage API keys and configurations securely.

## 🛠 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/Nyay-Connect.git
cd Nyay-Connect
```

### 2️⃣ Create and Activate Virtual Environment  
Using Python's `venv`:
```bash
python -m venv myenv
source myenv/Scripts/activate  # On Windows
source myenv/bin/activate      # On Mac/Linux
```

### 3️⃣ Install Dependencies  
```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables  
Create a `.env` file in the project root and add:
```ini
PINECONE_LEGALAID_API_KEY=<PINECONE_API_KEY>
PINECONE_LEGALAID_INDEX_NAME=<PINECONE_INDEX_NAME>
PINECONE_LEGALAID_HOST=<PINECONE_HOST>
```

### 5️⃣ Run the FastAPI Server  
```bash
uvicorn main:app --reload
```

## 📈 API Endpoints
| Method | Endpoint | Description |
|--------|-------------|-------------|
| POST   | `/search`  | Search legal documents |

## 👥 Contact
For queries, reach out at **atharvaraut103@gmail.com**.

