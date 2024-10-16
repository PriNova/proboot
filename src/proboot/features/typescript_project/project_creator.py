"""
Create a new standalone TypeScript project

This module provides functionality to set up the basic structure and files
for a new standalone TypeScript project.

Functions:
- create_typescript_project: Set up the basic structure and files for a TypeScript project
"""
import os
import json
import subprocess

def create_typescript_project(project_name):
    """
    Set up the basic structure and files for a standalone TypeScript project.

    Args:
        project_name (str): The name of the new TypeScript project.

    Returns:
        None
    """
    # Initialize npm project
    subprocess.run(["npm", "init", "-y"], check=True)

    # Create src directory
    os.makedirs("src", exist_ok=True)

    # Create a simple TypeScript file
    with open("src/index.ts", "w") as f:
        f.write('console.log("Hello, TypeScript!");')

    # Install TypeScript
    subprocess.run(["npm", "install", "typescript"], check=True)

    # Create tsconfig.json
    subprocess.run(["npx", "tsc", "--init"], check=True)

    # Update package.json with build script
    with open("package.json", "r+") as f:
        package_json = json.load(f)
        package_json["scripts"] = package_json.get("scripts", {})
        package_json["scripts"]["build"] = "tsc"
        f.seek(0)
        json.dump(package_json, f, indent=2)
        f.truncate()

    print(f"Created TypeScript project structure for {project_name}")
