# Automated AWS S3 Backup Tool

A Python-based DevOps project that demonstrates automating AWS S3
operations using Boto3.

## Features

- Connects to AWS using configured credentials
- Creates an S3 bucket
- Generates a demo file using Python
- Uploads the file to S3
- Lists objects in the bucket
- Verifies the uploaded file

## Technologies

- Python
- Boto3
- AWS S3
- AWS IAM

## Setup

Clone the repository:

    git clone <repository-url>

Navigate into the project:

    cd aws-s3-python-lab

Create a virtual environment:

    python3 -m venv .venv

Activate it:

    source .venv/bin/activate

Install dependencies:

    pip install -r requirements.txt

Configure AWS credentials using AWS CLI or another supported
AWS credential provider.

## Run

    python s3_demo.py

## Security

Do not commit AWS credentials, access keys, secret keys,
or other sensitive information to GitHub.
