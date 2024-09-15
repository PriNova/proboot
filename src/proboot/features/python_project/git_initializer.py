import subprocess


def init_git_repo(project_name):
    subprocess.run(['git', 'init', '--initial-branch=main'], cwd=project_name, check=True)
    print("Initialized git repository")
