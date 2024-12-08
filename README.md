Streamlit Application Deployment on AWS EC2
Overview

This project demonstrates the deployment of a Streamlit-based web application for animal classification using a pre-trained VGG16 model. The application allows users to upload an image of an animal, which is then classified into specific categories.

The application is deployed on AWS Elastic Compute Cloud (EC2).
Project Structure

    app.py: The Streamlit application.
    Custom_Structure_Animal_Classification_VGG16_v2.h5: Pre-trained VGG16 model for animal classification.
    requirements.txt: Python dependencies required for the application.
    README.md: Documentation for running and deploying the application.

Features

    Animal Classification: Upload an image to classify animals using a fine-tuned VGG16 model.
    Streamlit Interface: Simple web interface for image upload and results display.
    AWS Deployment: The app is deployed on an EC2 instance for accessibility.

Setup and Installation
1. Clone the Repository

git clone https://github.com/EliseZam/DeployingAIA3.git
cd "/Users/EliseZamora_1/Documents/School/Education/Animal_Classification_Project/Assignment 3"

2. Install Dependencies

Make sure you have Python 3.9 installed. Install required Python packages using:

pip install -r requirements.txt

3. Run Locally

To run the application locally, execute:

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

ssh -i <YOUR_KEY.pem> ubuntu@<EC2_PUBLIC_IP>

Install Python and Pip:

sudo apt update
sudo apt install python3-pip -y

Transfer project files to the instance using SCP:

scp -i <YOUR_KEY.pem> -r <LOCAL_PROJECT_PATH> ubuntu@<EC2_PUBLIC_IP>:~/project

Navigate to the project directory and install dependencies:

    cd ~/project
    pip3 install -r requirements.txt

Run the Application:

    Start the Streamlit application:

        streamlit run app.py --server.port 8501 --server.enableCORS false

        The application will be accessible at http://<EC2_PUBLIC_IP>:8501.

Troubleshooting

    Port Access Issues:
        Ensure the EC2 instance's security group allows inbound traffic on port 8501.
    Python Compatibility:
        Ensure Python 3.9 is installed on the EC2 instance.

Contact

For questions or issues, please contact:

    Name: [Your Name]
    Email: [Your Email]
    # DeployingAIA3
