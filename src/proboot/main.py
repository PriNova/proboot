import sys
from proboot.cli.parser import create_parser
from proboot.features.python_project.bootstrapper import bootstrap_python_project

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
