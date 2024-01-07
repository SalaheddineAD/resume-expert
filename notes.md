## 1- How to read .env file
It's good practice to add .env to .gitignore 
### Code:
**-------------------------------------------------------------**
import os
from dotenv import load_dotenv

load_dotenv()

GCP_PROJECT_ID = os.getenv('GCP_PROJECT_ID')
SERVICE_ACCOUNT_FILE = os.getenv('SERVICE_ACCOUNT_FILE')
STORAGE_BUCKET_NAME = os.getenv('STORAGE_BUCKET_NAME')
**-------------------------------------------------------------**
load_dotenv() will first look for a .env file and if it finds one, it will load the environment variables from the file and make them accessible to your project like any other environment variable would be.

If an environment variable is not found in the .env file, load_dotenv will then search for a variable by the given name in the host environment. This means that when your project is running locally and the .env file is present, the variables defined in the file will be used. When your project is deployed to a host environment like a virtual machine or Docker container where the .env file is not present, the environment variables defined in the host environment will be used instead.

By default load_dotenv will look for the .env file in the current working directory or any parent directories however you can also specify the path if your particular use case requires it be stored elsewhere.
### Code:
**-------------------------------------------------------------**
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('path/to/.env')
load_dotenv(dotenv_path=dotenv_path)
**-------------------------------------------------------------**