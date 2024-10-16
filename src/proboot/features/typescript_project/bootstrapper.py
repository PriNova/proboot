"""
Bootstrap a new standalone TypeScript project

This module provides functionality to create a new standalone TypeScript project structure,
including necessary files, directories, and optionally initializing a Git repository.

The main function `bootstrap_typescript_project` orchestrates the creation of:
- Project directory
- Standalone TypeScript project setup
- Installation of dependencies
- Git repository (optional)

Functions:
- bootstrap_typescript_project: Main function to create a new standalone TypeScript project
"""

import os
import subprocess

from proboot.features.typescript_project.dependency_installer import (
    install_dependencies,
)
from proboot.features.typescript_project.project_creator import (
    create_typescript_project,
)
from proboot.utils.directory_handler import create_project_directory


def bootstrap_typescript_project(project_name, init_git):
    """
    Bootstraps a new standalone TypeScript project by creating the necessary files and directories,
    setting up the project, and optionally initializing a Git repository.

    Args:
        project_name (str): The name of the new TypeScript project.
        init_git (bool): Whether to initialize a Git repository for the new project.

    Returns:
        None
    """
    create_project_directory(project_name)
    os.chdir(project_name)
    create_typescript_project(project_name)
    install_dependencies()
    if init_git:
        subprocess.run(["git", "init", "--initial-branch=main"], check=True)
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "Initial commit"], check=True)

    print(
        f"Standalone TypeScript project '{project_name}' has been created successfully."
    )
    print("To build the project, run:")
    print(f"cd {project_name}")
    print("npm run build")
