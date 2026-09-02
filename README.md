# CODTECH CI/CD Project

## Intern Details

**Intern ID:** CITS8945

## Project Title

CI/CD with GitHub Actions

## Project Description

This project demonstrates Continuous Integration and Continuous Deployment
using GitHub Actions.

The workflow automatically runs when code is pushed to the main branch.

## Technologies Used

- Python
- GitHub
- GitHub Actions

## CI/CD Pipeline

The GitHub Actions workflow performs the following steps:

1. Checkout the source code
2. Set up Python
3. Install dependencies
4. Run automated tests
5. Build the project
6. Upload the build artifact

## Project Structure

```text
codtech-cicd-project/
├── app.py
├── test_app.py
├── requirements.txt
├── README.md
└── .github/
    └── workflows/
        └── ci.yml
