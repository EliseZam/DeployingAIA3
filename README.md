# Streamlit Application Deployment on AWS EC2

## Overview

This project demonstrates the deployment of a Streamlit-based web application for animal classification using a pre-trained VGG16 model. The application allows users to upload an image of an animal, which is then classified into specific categories.

The application is deployed on AWS Elastic Compute Cloud (EC2).

---

## Project Structure

- `app.py`: The Streamlit application.
- `Custom_Structure_Animal_Classification_VGG16_v3.ipynb`: Jupyter notebook used for training and dynamically loading the VGG16 model for animal classification.
- `requirements.txt`: Python dependencies required for the application.
- `README.md`: Documentation for running and deploying the application.

---

## Features

1. **Animal Classification**:
   - Upload an image to classify animals using a fine-tuned VGG16 model.

2. **Streamlit Interface**:
   - Simple web interface for image upload and results display.

3. **AWS Deployment**:
   - The app is deployed on an EC2 instance for accessibility.

---

## Setup and Installation

### 1. Clone the Repository
```bash
git clone https://github.com/EliseZam/DeployingAIA3.git
Navigate to the project directory:

bash
Copy code
cd DeployingAIA3
2. Install Dependencies
Make sure you have Python 3.9 installed. Install the required Python packages:

bash
Copy code
pip install -r requirements.txt
3. Run Locally
To run the application locally, execute:

bash
Copy code
streamlit run app.py
This will launch the application at http://localhost:8501.

Deploying on AWS EC2
Steps to Deploy:
Launch an EC2 Instance:

Go to the AWS Management Console and launch an EC2 instance.
Choose an instance type with at least 2 vCPUs and 4GB RAM (e.g., t2.medium).
Configure the instance security group to allow inbound traffic on port 8501.
Install Python and Dependencies on the Instance:

Connect to the EC2 instance via SSH:

bash
Copy code
ssh -i AnimalClassificationA4.pem ubuntu@34.238.40.72
Install Python and Pip:

bash
Copy code
sudo apt update
sudo apt install python3-pip -y
Transfer project files to the instance using SCP:

bash
Copy code
scp -i AnimalClassificationA4.pem -r /Users/EliseZamora_1/Documents/School/Education/Animal_Classification_Project/Assignment\ 3 ubuntu@34.238.40.72:~/project
Navigate to the project directory and install dependencies:

bash
Copy code
cd ~/project
pip3 install -r requirements.txt
Run the Application:

Start the Streamlit application:
bash
Copy code
streamlit run app.py --server.port 8501 --server.enableCORS false
The application will be accessible at http://34.238.40.72:8501.
Troubleshooting
Port Access Issues:

Ensure the EC2 instance's security group allows inbound traffic on port 8501.
Python Compatibility:

Ensure Python 3.9 is installed on the EC2 instance.