"""
This module handles directory operations for the proboot project.

It provides utility functions for creating and managing project directories
during the bootstrapping process. The main functionality includes:

- Creating new project directories
- Handling existing directory conflicts
- Providing informative output about directory operations

This module is part of the proboot utility package and is used to ensure
proper directory setup when initializing new projects.
"""
import os
import sys

def create_project_directory(project_name):
    """
    Creates a new project directory with the given name.
    
    Args:
        project_name (str): The name of the project directory to create.
    
    Raises:
        FileExistsError: If the project directory already exists.
    """
    try:
        os.makedirs(project_name)
        print(f"Created project directory: {project_name}")
    except FileExistsError:
        print(f"Directory {project_name} already exists.")
        sys.exit(1)
