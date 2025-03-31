<<<<<<< HEAD
# Document AI System

A comprehensive document processing system that uses Azure Document Intelligence and OpenAI for OCR and data extraction.

## Features

- Document OCR processing using Azure Document Intelligence
- GPT-powered data extraction and analysis
- Support for multiple document types including HRA documents
- Interactive web interface for file processing and data exploration
- Azure Functions-based backend processing
- Cosmos DB for data storage and configuration management

## Prerequisites

- Python 3.11 or higher
- Azure subscription with the following services:
  - Azure Document Intelligence
  - Azure Functions
  - Azure Cosmos DB
  - Azure Blob Storage
  - Azure OpenAI Service
- Azure CLI (for local development)

## Setup

1. Clone the repository:
```bash
git clone <your-repo-url>
cd DocAI
```

2. Create and activate virtual environment:
```bash
# For Windows
python -m venv .venv
.venv\Scripts\activate

# For Linux/Mac
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:
```bash
# Install frontend dependencies
cd frontend
pip install -r requirements.txt

# Install backend dependencies
cd ../src/functionapp
pip install -r requirements.txt
```

4. Set up environment variables:
   - Copy `.env.example` to `.env` in both frontend and backend directories
   - Fill in your Azure service credentials and configuration

5. Configure Azure Functions:
   - Copy `local.settings.json.example` to `local.settings.json` in the function app directory
   - Update with your Azure service credentials

## Running the Application

1. Start the Azure Function:
```bash
cd src/functionapp
func start
```

2. Start the frontend application:
```bash
cd frontend
streamlit run app.py
```

3. Access the application at `http://localhost:8501`

## Project Structure

```
DocAI/
├── frontend/                 # Streamlit frontend application
│   ├── app.py              # Main application file
│   ├── process_files.py    # File processing logic
│   ├── explore_data.py     # Data exploration logic
│   └── requirements.txt    # Frontend dependencies
├── src/
│   └── functionapp/        # Azure Function backend
│       ├── function_app.py # Main function app
│       ├── ai_ocr/         # OCR processing logic
│       └── requirements.txt # Backend dependencies
└── example-datasets/       # Example dataset configurations
    └── hra-dataset/       # HRA document processing config
```

## Configuration

The application uses several environment variables for configuration:

- `DOCUMENT_INTELLIGENCE_ENDPOINT`: Azure Document Intelligence endpoint
- `DOCUMENT_INTELLIGENCE_KEY`: Azure Document Intelligence key
- `COSMOS_DB_ENDPOINT`: Azure Cosmos DB endpoint
- `COSMOS_DB_KEY`: Azure Cosmos DB key
- `OPENAI_API_KEY`: Azure OpenAI API key
- `BLOB_CONN_STR`: Azure Blob Storage connection string

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 
=======
# docai
>>>>>>> a29d26ed6cdc8d95f2786e3e853544b679c67d84
