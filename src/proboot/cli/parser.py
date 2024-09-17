"""
Command-line interface parser for the proboot project.

This module provides functionality to create and configure an ArgumentParser
for handling command-line arguments when bootstrapping a new project using proboot.

The main function in this module is `create_parser()`, which sets up the
argument parser with the necessary options and arguments for project creation.

Usage:
    from proboot.cli.parser import create_parser
    parser = create_parser()
    args = parser.parse_args()

Available arguments:
    - project_name: The name of the project to create (positional argument)
    - --type: The type of project to create (default: "python")
    - --no-git: Flag to disable git repository initialization

For more details on each argument, refer to the `create_parser()` function documentation.
"""
import argparse

def create_parser():
    """
    Create an ArgumentParser instance to handle command-line arguments for bootstrapping a new project.
    
    The parser supports the following arguments:
    - `project_name`: The name of the project to create.
    - `--type`: The type of project to create, currently only supporting "python".
    - `--no-git`: If set, do not initialize a git repository for the new project.
    
    Returns:
        argparse.ArgumentParser: The configured ArgumentParser instance.
    """
    parser = argparse.ArgumentParser(description="Bootstrap a new project")
    parser.add_argument("project_name", help="Name of the project")
    parser.add_argument("--type", choices=["python"], default="python", help="Type of project to create")
    parser.add_argument("--no-git", action="store_true", help="Don't initialize a git repository")
    return parser
