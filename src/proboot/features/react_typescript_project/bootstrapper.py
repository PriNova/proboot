"""
Bootstrap a new React TypeScript project

This module provides functionality to create a new React TypeScript project structure,
including necessary files, directories, and optionally initializing a Git repository.

The main function `bootstrap_react_typescript_project` orchestrates the creation of:
- Project directory
- React TypeScript project using pnpm and Vite
- Installation of dependencies
- Git repository (optional)

Functions:
- bootstrap_react_typescript_project: Main function to create a new React TypeScript project
"""
import os

from proboot.features.python_project.git_initializer import init_git_repo
from proboot.features.react_typescript_project.dependency_installer import \
    install_dependencies
from proboot.features.react_typescript_project.project_creator import \
    create_react_typescript_project
from proboot.utils.directory_handler import create_project_directory


def bootstrap_react_typescript_project(project_name, init_git):
    """
    Bootstraps a new React TypeScript project by creating the necessary files and directories, 
    setting up the project using pnpm and Vite, and optionally initializing a Git repository.

    Args:
        project_name (str): The name of the new React TypeScript project.
        init_git (bool): Whether to initialize a Git repository for the new project.

    Returns:
        None
    """
    create_project_directory(project_name)
    os.chdir(project_name)
    create_react_typescript_project(project_name)
    install_dependencies()
    if init_git:
        init_git_repo(project_name)

    print(f"React TypeScript project '{project_name}' has been created successfully.")
    print("To start the development server, run:")
    print(f"cd {project_name}")
    print("pnpm run dev")
