"""
ProBoot: A Python Project Bootstrapper

This module contains the main functionality for the ProBoot tool, which helps
users bootstrap new Python projects. It includes functions for handling both
command-line and interactive modes of operation.

The main components of this module are:
- interactive_mode(): Prompts the user for project details interactively.
- main(): The entry point of the application, handling both CLI and interactive modes.
"""
import sys

from proboot.cli.parser import create_parser
from proboot.features.python_project.bootstrapper import \
    bootstrap_python_project


def interactive_mode():
    """
    Interactively prompt the user for project details.
    
        This function asks the user to input the project name, project type,
        and whether to initialize a git repository.
    
        Returns:
            tuple: A tuple containing:
                - project_name (str): The name of the project.
                - project_type (str): The type of the project (currently only 'python' is supported).
                - init_git (bool): Whether to initialize a git repository.
    """
    project_name = input("Enter the project name: ").strip()
    while not project_name:
        project_name = input("Project name cannot be empty. Please enter a valid name: ").strip()

    project_type = input("Enter the project type (python) [default: python]: ").strip().lower()
    while project_type not in ['', 'python']:
        project_type = input("Invalid project type. Please enter 'python': ").strip().lower()

    if project_type == '' or project_type == 'python':
        project_type = 'python'

    init_git = input("Initialize git repository? (y/n) [default: y]: ").strip().lower()
    init_git = init_git != 'n'

    return project_name, project_type, init_git

def main():
    """
    Main function to handle the project bootstrapping process.
    
        This function determines whether to use command-line arguments or
        interactive mode to get project details. It then calls the appropriate
        bootstrapping function based on the project type.
    
        The function does the following:
        1. Checks if command-line arguments are provided.
        2. If arguments are provided, it parses them using the create_parser() function.
        3. If no arguments are provided, it calls the interactive_mode() function.
        4. Based on the project type, it calls the appropriate bootstrapping function.
        5. If the project type is not supported, it prints an error message.
    """
    if len(sys.argv) > 1:
        parser = create_parser()
        args = parser.parse_args()
        project_name = args.project_name
        project_type = args.type
        init_git = not args.no_git
    else:
        project_name, project_type, init_git = interactive_mode()

    if project_type == "python":
        bootstrap_python_project(project_name, init_git)
    else:
        print(f"Project type {project_type} is not supported yet.")

if __name__ == "__main__":
    main()
