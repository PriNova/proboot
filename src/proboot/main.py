"""
ProBoot: A Project Bootstrapper

This module contains the main functionality for the ProBoot tool, which helps
users bootstrap new projects. It includes functions for handling both
command-line and interactive modes of operation.

The main components of this module are:
- interactive_mode(): Prompts the user for project details interactively.
- main(): The entry point of the application, handling both CLI and interactive modes.

Supported project types:
- Python
- React with TypeScript
- Standalone TypeScript
"""
import sys

from proboot.cli.parser import create_parser
from proboot.features.python_project.bootstrapper import bootstrap_python_project
from proboot.features.react_typescript_project.bootstrapper import bootstrap_react_typescript_project
from proboot.features.typescript_project.bootstrapper import bootstrap_typescript_project


def interactive_mode():
    """
    Interactively prompt the user for project details.
    
    This function asks the user to input the project name, select the project type
    from a numbered list, and choose whether to initialize a git repository.
    
    Returns:
        tuple: A tuple containing:
            - project_name (str): The name of the project.
            - project_type (str): The type of the project (python, react-typescript, or typescript).
            - init_git (bool): Whether to initialize a git repository.
    """
    project_name = input("Enter the project name: ").strip()
    while not project_name:
        project_name = input("Project name cannot be empty. Please enter a valid name: ").strip()

    project_types = ["python", "react-typescript", "typescript"]
    print("Select the project type:")
    for i, ptype in enumerate(project_types, 1):
        print(f"{i}. {ptype}")

    while True:
        try:
            selection = int(input("Enter the number of your choice [default: 1]: ") or "1")
            if 1 <= selection <= len(project_types):
                project_type = project_types[selection - 1]
                break
            else:
                print(f"Please enter a number between 1 and {len(project_types)}.")
        except ValueError:
            print("Please enter a valid number.")

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
    elif project_type == "react-typescript":
        bootstrap_react_typescript_project(project_name, init_git)
    elif project_type == "typescript":
        bootstrap_typescript_project(project_name, init_git)
    else:
        print(f"Project type {project_type} is not supported yet.")

if __name__ == "__main__":
    main()
