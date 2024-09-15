# proboot

proboot is a command-line interface (CLI) tool designed to bootstrap Python projects quickly and efficiently. It automates the process of setting up a new project structure, creating essential files, and initializing a git repository.

## Features

- Create a new project directory
- Set up a Python virtual environment
- Generate a basic `main.py` file
- Create a README.md template
- Add a .gitignore file with common Python ignores
- Optionally initialize a git repository
- Interactive mode for guided project setup

## Installation

To install proboot, run the following command:
`pip install proboot`


## Usage

You can use proboot in two ways:

1. Command-line mode:
`proboot my_new_project --type python`
Use the `--no-git` flag if you don't want to initialize a git repository.

2. Interactive mode:
`proboot`

Follow the prompts to set up your project.

## Options

- `project_name`: Name of the project (required)
- `--type`: Type of project to create (default: python)
- `--no-git`: Don't initialize a git repository

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
