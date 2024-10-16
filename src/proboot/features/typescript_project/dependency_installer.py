"""
Install dependencies for a standalone TypeScript project

This module provides functionality to install necessary dependencies
for a standalone TypeScript project.

Functions:
- install_dependencies: Install TypeScript and other necessary dependencies
"""
import subprocess

def install_dependencies():
    """
    Install TypeScript and other necessary dependencies for the project.

    Returns:
        None
    """
    subprocess.run(["pnpm", "install", "--save-dev", "typescript", "@types/node"], check=True)
    print("Installed TypeScript and dependencies.")
