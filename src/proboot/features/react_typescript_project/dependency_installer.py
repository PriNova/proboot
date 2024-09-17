"""
React TypeScript Project Dependency Installer

This module contains the function to install dependencies for a React TypeScript project using pnpm.
"""

import subprocess

def install_dependencies():
    """
    Installs project dependencies using pnpm.
    """
    subprocess.run(["pnpm", "install"], check=True)
    print("Dependencies installed successfully.")
