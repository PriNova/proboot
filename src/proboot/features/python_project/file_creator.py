import os
import sys
import venv


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

This project was created using proboot.

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

def activate_venv(project_name):
    venv_path = os.path.join(project_name, 'venv')
    if os.path.exists(venv_path):
        if sys.platform == 'win32':
            activate_script = os.path.join(venv_path, 'Scripts', 'activate.bat')
        else:
            activate_script = os.path.join(venv_path, 'bin', 'activate')
        
        if os.path.exists(activate_script):
            print(f"To activate the virtual environment, run:")
            print(f"source {activate_script}")
        else:
            print("Virtual environment exists but activation script not found.")
    else:
        print("Virtual environment not found.")