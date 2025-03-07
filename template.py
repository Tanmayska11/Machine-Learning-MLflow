import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

project_name = "mlproject"

list_of_files = [
    ".github/workflows/.gitkeep", #CI/CD workflow files
    f"src/{project_name}/__init__.py", 
    f"src/{project_name}/components/__init__.py", # Components of the project
    f"src/{project_name}/utils/__init__.py", # Utility functions for the project
    f"src/{project_name}/utils/common.py", # Common utility functions for the project
    f"src/{project_name}/config/__init__.py", # Configuration files for the project
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py", # Pipeline for the project
    f"src/{project_name}/entity/__init__.py", # Entity classes for the project
    f"src/{project_name}/entity/config_entity.py", 
    f"src/{project_name}/constants/__init__.py", # Constants for the project
    "config/config.yaml", # Configuration file for the project
    "requirements.txt", # List of dependencies
    "schema.yaml", # Schema for data validation
    "params.yaml", 
    "main.py", # Main entry point for the project
    "app.py", #Flask/Django FastAPI application for deploying the model.
    "Dockerfile", # Dockerfile for containerizing the application
    "setup.py", # Setup file for packaging the application
    "research/trials.ipynb", # Jupyter notebook for conducting hyperparameter tuning
    "templates/index.html" # HTML template for the Flask/Django FastAPI application
]

#This script automates the setup of a Machine Learning
#  Project by creating all the necessary folders and files. 
# Instead of manually setting up the project structure, 
# running this script ensures everything is properly organized and ready for development. 
# It saves time, avoids errors, and ensures consistency across different setups.


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory : {filedir} for the file :{filename}")
                     
        if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
            with open(filepath, "w") as f:
                pass
                logging.info(f"Created file: {filepath}")

        else:
            logging.info(f"File: {filepath} already exists")


    