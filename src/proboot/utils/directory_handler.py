import os
import sys

def create_project_directory(project_name):
    try:
        os.makedirs(project_name)
        print(f"Created project directory: {project_name}")
    except FileExistsError:
        print(f"Directory {project_name} already exists.")
        sys.exit(1)
