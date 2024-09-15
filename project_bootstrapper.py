#!/usr/bin/env python3

import argparse
import os
import subprocess
import venv
import sys

def create_project_directory(project_name):
    try:
        os.makedirs(project_name)
        print(f"Created project directory: {project_name}")
    except FileExistsError:
        print(f"Directory {project_name} already exists.")
        sys.exit(1)

def create_main_py(project_name):
    main_py_content = '''
def main():
    print("Hello, World!")

if __name__ == "__main__":
    main()
'''
    with open(os.path.join(project_name, 'main.py'), 'w') as f:
        f.write(main_py_content.strip())
    print("Created main.py")

def create_readme(project_name):
    readme_content = f'''
# {project_name}

This project was created using the project_bootstrapper.

## Getting Started

1. Activate the virtual environment:
`source venv/bin/activate`

2. Run the main script:
`python main.py`


## License

This project is open source and available under the [MIT License](LICENSE).
'''
    with open(os.path.join(project_name, 'README.md'), 'w') as f:
        f.write(readme_content.strip())
    print("Created README.md")

def create_gitignore(project_name):
    gitignore_content = '''
# Python
__pycache__/
*.py[cod]
*$py.class
venv/

# IDEs
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db
'''
    with open(os.path.join(project_name, '.gitignore'), 'w') as f:
        f.write(gitignore_content.strip())
    print("Created .gitignore")

def create_venv(project_name):
    venv.create(os.path.join(project_name, 'venv'), with_pip=True)
    print("Created virtual environment")

def init_git_repo(project_name):
    subprocess.run(['git', 'init'], cwd=project_name, check=True)
    print("Initialized git repository")

def bootstrap_python_project(project_name, init_git):
    create_project_directory(project_name)
    create_main_py(project_name)
    create_readme(project_name)
    create_gitignore(project_name)
    create_venv(project_name)
    if init_git:
        init_git_repo(project_name)

def interactive_mode():
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
    if len(sys.argv) > 1:
        parser = argparse.ArgumentParser(description="Bootstrap a new project")
        parser.add_argument("project_name", help="Name of the project")
        parser.add_argument("--type", choices=["python"], default="python", help="Type of project to create")
        parser.add_argument("--no-git", action="store_true", help="Don't initialize a git repository")

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

