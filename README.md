# Customer Complaint Intelligence & Prioritization System

An end-to-end NLP system that automatically classifies customer complaints and flags urgent cases to assist customer support teams in faster and more accurate decision-making.

---

## Key Features
- Complaint category classification using real-world financial complaints
- Urgency detection for escalation prioritization
- Clean, professional web interface
- Production-ready inference pipeline
- Deployed-ready for Hugging Face Spaces

---

## Problem Statement

Organizations receive thousands of unstructured customer complaints daily.
Manual triage is slow, inconsistent, and error-prone.

This system automates complaint analysis by:
	- Categorizing complaints into business-relevant classes
	- Identifying urgent cases that require immediate attention
	- Providing a clean interface for human agents

---

## Dataset
- Source: Consumer Financial Protection Bureau (CFPB)
- Size: ~12 million complaints (filtered to high-quality narratives)
- Type: Real customer-written complaints
- Domain: Banking & Financial Services

---

## Tech Stack
- Python
- Scikit-learn
- TF-IDF Vectorization
- Logistic Regression
- Gradio (UI)
- Git & GitHub

---

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

---

## Run Locally
1. ```bash
	git clone https://github.com/MathurakshiMahendrarajah/Complaint-intelligence-system.git
	cd Complaint-intelligence-system

	pip install -r requirements.txt
	
	python app.py

## Deployment

The application is designed to be deployed on Hugging Face Spaces using Gradio.

Live Demo link:
1. ```bash
	https://huggingface.co/spaces/MathurakshiM/Customer_Complaint_Intelligence_System


## Screenshots

<img width="1646" height="780" alt="Screenshot 2025-12-15 at 9 54 48 PM" src="https://github.com/user-attachments/assets/e720f23d-b90c-4ac3-91c2-c872d4b0f047" />

