"""
This module contains functions for creating and setting up files and directories
for a new Python project using the proboot tool.

It provides functionality to:
- Create the project structure
- Generate main.py
- Create README.md
- Set up .gitignore
- Create pyproject.toml
- Create setup.py
- Set up and activate a virtual environment

These functions are used to bootstrap a new Python project with a standardized
structure and common configuration files.
"""
import os
import sys
import venv


def create_project_structure(project_name):
    """
    Creates the basic project structure for a new Python project.

    Args:
        project_name (str): The name of the new Python project.

    Returns:
        None
    """
    os.makedirs(
        os.path.join(project_name, "src", project_name, "features"), exist_ok=True
    )
    open(
        os.path.join(project_name, "src", project_name, "__init__.py"),
        "a",
        encoding="utf-8",
    ).close()
    open(
        os.path.join(project_name, "src", project_name, "features", "__init__.py"),
        "a",
        encoding="utf-8",
    ).close()
    print(f"Created project structure for {project_name}")


def create_main_py(project_name):
    """
    Creates the main.py file for a new Python project.

    Args:
        project_name (str): The name of the new Python project.

    Returns:
        None
    """
    main_py_content = """
def main():
    print("Hello, World!")

if __name__ == "__main__":
    main()
"""
    with open(
        os.path.join(project_name, "src", project_name, "main.py"),
        "w",
        encoding="utf-8",
    ) as f:
        f.write(main_py_content.strip())
    print("Created main.py")


def create_readme(project_name):
    """
    Creates the README.md file for a new Python project.

    Args:
        project_name (str): The name of the new Python project.

    Returns:
        None
    """
    readme_content = f"""
# {project_name}

This project was created using proboot.

## Getting Started

1. Install the project:
`pip install -e .`

2. Activate the virtual environment:
`source venv/bin/activate`

3. Run the main script:
`python -m {project_name}.main`

## License

This project is open source and available under the [MIT License](LICENSE).
"""
    with open(os.path.join(project_name, "README.md"), "w", encoding="utf-8") as f:
        f.write(readme_content.strip())
    print("Created README.md")


def create_gitignore(project_name):
    """
    Creates a .gitignore file for a new Python project.

    Args:
        project_name (str): The name of the new Python project.

    Returns:
        None
    """
    gitignore_content = """
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

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
"""
    with open(os.path.join(project_name, ".gitignore"), "w", encoding="utf-8") as f:
        f.write(gitignore_content.strip())
    print("Created .gitignore")


def create_pyproject_toml(project_name):
    """
    Creates a pyproject.toml file for a new Python project.

    Args:
        project_name (str): The name of the new Python project.

    Returns:
        None
    """
    pyproject_content = f"""
[build-system]
requires = ["setuptools>=45", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "{project_name}"
version = "0.1.0"
description = "A project created with proboot"
authors = [{{name = "Your Name", email = "your.email@example.com"}}]
readme = "README.md"
requires-python = ">=3.7"

[project.scripts]
{project_name} = "{project_name}.main:main"
"""
    with open(os.path.join(project_name, "pyproject.toml"), "w", encoding="utf-8") as f:
        f.write(pyproject_content.strip())
    print("Created pyproject.toml")


def create_setup_py(project_name):
    """
    Creates a setup.py file for a new Python project.

    Args:
        project_name (str): The name of the new Python project.

    Returns:
        None
    """
    setup_content = """
from setuptools import setup, find_packages

setup(
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
"""
    with open(os.path.join(project_name, "setup.py"), "w", encoding="utf-8") as f:
        f.write(setup_content.strip())
    print("Created setup.py")


def create_venv(project_name):
    """
    Creates a new virtual environment for the Python project.

    Args:
        project_name (str): The name of the new Python project.

    Returns:
        None
    """
    venv.create(os.path.join(project_name, "venv"), with_pip=True)
    print("Created virtual environment")


def activate_venv(project_name):
    """
    Activates the virtual environment for the specified Python project.

    Args:
        project_name (str): The name of the Python project.

    Returns:
        None
    """
    venv_path = os.path.join(project_name, "venv")
    if os.path.exists(venv_path):
        if sys.platform == "win32":
            activate_script = os.path.join(venv_path, "Scripts", "activate.bat")
        else:
            activate_script = os.path.join(venv_path, "bin", "activate")

        if os.path.exists(activate_script):
            print("To activate the virtual environment, run:")
            print(f"source {activate_script}")
        else:
            print("Virtual environment exists but activation script not found.")
    else:
        print("Virtual environment not found.")
