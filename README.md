# proboot

proboot is a versatile command-line interface (CLI) tool designed to bootstrap various types of projects quickly and efficiently. It automates the process of setting up new project structures, creating essential files, and initializing a git repository.

## Features

- Create a new project directory
- Set up project-specific environments (e.g., Python virtual environment)
- Generate basic project files (e.g., `main.py` for Python projects)
- Create a README.md template
- Add a .gitignore file with project-specific ignores
- Optionally initialize a git repository
- Interactive mode for guided project setup
- Support for multiple project types (currently Python and React with TypeScript)

## Installation

To install proboot, run the following command:
`pip install proboot`

## Usage

You can use proboot in two ways:

1. Command-line mode:
`proboot my_new_project --type python`
or
`proboot my_new_project --type react-typescript`

Use the `--no-git` flag if you don't want to initialize a git repository.

2. Interactive mode:
`proboot`

Follow the prompts to set up your project.

## Options

- `project_name`: Name of the project (required)
- `--type`: Type of project to create (choices: python, react-typescript; default: python)
- `--no-git`: Don't initialize a git repository

## Project Types

- Python: Sets up a Python project with virtual environment and basic structure
- React with TypeScript: Creates a React project with TypeScript configuration

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
