# MLOps CI/CD Pipeline

## Overview
This project demonstrates a basic MLOps CI/CD pipeline using GitHub Actions.

## Technologies Used
- Python
- Scikit-learn
- Pytest
- Git and GitHub
- GitHub Actions

## Project Description
The project uses the Iris dataset to train a Logistic Regression model and predict flower species.

## Model Testing
Unit testing is performed using Pytest to verify that the model achieves at least 80% accuracy.

## CI/CD Workflow
The GitHub Actions workflow automatically:
1. Checks out the repository.
2. Sets up Python.
3. Installs project dependencies.
4. Runs unit tests.
5. Simulates deployment if all tests pass on the main branch.

## Run Locally
Install dependencies:

```bash
pip install -r requirements.txt
```

Run the ML application:

```bash
python app.py
```

Run tests:

```bash
pytest -v
```