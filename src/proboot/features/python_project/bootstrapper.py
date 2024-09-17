"""
Bootstrap a new Python project

This module provides functionality to create a new Python project structure,
including necessary files, directories, and optionally initializing a Git repository.

The main function `bootstrap_python_project` orchestrates the creation of:
- Project directory
- Project structure (src, tests, etc.)
- Main Python file
- README file
- .gitignore file
- pyproject.toml file
- setup.py file
- Virtual environment
- Git repository (optional)

Functions:
- bootstrap_python_project: Main function to create a new Python project
"""

from proboot.features.python_project.file_creator import (
    activate_venv, create_gitignore, create_main_py, create_project_structure,
    create_pyproject_toml, create_readme, create_setup_py, create_venv)
from proboot.features.python_project.git_initializer import init_git_repo
from proboot.utils.directory_handler import create_project_directory


def bootstrap_python_project(project_name, init_git):
    """
    Bootstraps a new Python project by creating the necessary files and directories, 
    setting up a virtual environment, and optionally initializing a Git repository.

    Args:
        project_name (str): The name of the new Python project.
        init_git (bool): Whether to initialize a Git repository for the new project.

    Returns:
        None
    """
    create_project_directory(project_name)
    create_project_structure(project_name)
    create_main_py(project_name)
    create_readme(project_name)
    create_gitignore(project_name)
    create_pyproject_toml(project_name)
    create_setup_py(project_name)
    create_venv(project_name)
    activate_venv(project_name)
    if init_git:
        init_git_repo(project_name)
        #os.chdir(project_name)
        #subprocess.run(["git", "add", "."], check=True)
        #subprocess.run(["git", "commit", "-m", "Initial commit"], check=True)
