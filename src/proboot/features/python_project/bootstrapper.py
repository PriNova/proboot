from proboot.features.python_project.file_creator import (create_gitignore,
                                                          create_main_py,
                                                          create_readme,
                                                          create_venv)
from proboot.features.python_project.git_initializer import init_git_repo
from proboot.utils.directory_handler import create_project_directory


def bootstrap_python_project(project_name, init_git):
    create_project_directory(project_name)
    create_main_py(project_name)
    create_readme(project_name)
    create_gitignore(project_name)
    create_venv(project_name)
    if init_git:
        init_git_repo(project_name)
