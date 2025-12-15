# Customer Complaint Intelligence & Prioritization System

An end-to-end NLP system that automatically classifies customer complaints and flags urgent cases to assist customer support teams in faster and more accurate decision-making.

⸻

## Key Features
- Complaint category classification using real-world financial complaints
- Urgency detection for escalation prioritization
- Clean, professional web interface
- Production-ready inference pipeline
- Deployed-ready for Hugging Face Spaces

⸻

## Problem Statement

Organizations receive thousands of unstructured customer complaints daily.
Manual triage is slow, inconsistent, and error-prone.

This system automates complaint analysis by:
	- Categorizing complaints into business-relevant classes
	- Identifying urgent cases that require immediate attention
	- Providing a clean interface for human agents

⸻

## Dataset
	- Source: Consumer Financial Protection Bureau (CFPB)
	- Size: ~12 million complaints (filtered to high-quality narratives)
	- Type: Real customer-written complaints
	- Domain: Banking & Financial Services

⸻

## Tech Stack
	- Python
	- Scikit-learn
	- TF-IDF Vectorization
	- Logistic Regression
	- Gradio (UI)
	- Git & GitHub

⸻

## System Architecture
    ```
    User Complaint
        ↓
    Text Preprocessing
        ↓
    TF-IDF Vectorizer
        ↓
    Classification Model
        ↓
    Urgency Decision Logic
        ↓
    Web Interface Output
    ```
## Application Interface

Users can:
	- Enter a customer complaint
	- View predicted category
	- See urgency level
	- Clear inputs and test multiple scenarios

⸻

## Run Locally
git clone https://github.com/<your-username>complaint-intelligence-system.git
cd complaint-intelligence-system
pip install -r requirements.txt
python app.py

## Deployment

The application is designed to be deployed on Hugging Face Spaces using Gradio.

Live Demo link:


## Screenshots