
"""
Git Initializer Module

This module provides functionality to initialize a Git repository
for a new Python project. It includes a function to run the 'git init'
command with appropriate flags to set up a new repository with the
main branch as the initial branch.

Functions:
    init_git_repo(project_name): Initialize a new Git repository in the
                                 specified project directory.
"""
import subprocess


def init_git_repo(project_name):
    """
    Initialize a new Git repository in the specified project directory.
    
        This function runs the 'git init' command with the '--initial-branch=main' flag
        to create a new Git repository in the given project directory. It sets the
        initial branch name to 'main'.
    
        Args:
            project_name (str): The name of the project directory where the Git
                                repository will be initialized.
    
        Raises:
            subprocess.CalledProcessError: If the 'git init' command fails.
    
        Returns:
            None
    """
    subprocess.run(['git', 'init', '--initial-branch=main'], cwd=project_name, check=True)
    print("Initialized git repository")
