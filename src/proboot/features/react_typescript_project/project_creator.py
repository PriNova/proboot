"""
React TypeScript Project Creator

This module contains the function to create a new React TypeScript project using pnpm and Vite.
"""

import subprocess

def create_react_typescript_project(project_name):
    """
    Creates a new React TypeScript project using pnpm and Vite.

    Args:
        project_name (str): The name of the new React TypeScript project.
    """
    subprocess.run(["pnpm", "create", "vite@latest", ".", "--template", "react-ts"], check=True)
    print(f"React TypeScript project '{project_name}' has been created successfully.")
