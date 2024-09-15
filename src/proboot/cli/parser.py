import argparse

def create_parser():
    parser = argparse.ArgumentParser(description="Bootstrap a new project")
    parser.add_argument("project_name", help="Name of the project")
    parser.add_argument("--type", choices=["python"], default="python", help="Type of project to create")
    parser.add_argument("--no-git", action="store_true", help="Don't initialize a git repository")
    return parser
