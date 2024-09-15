import subprocess

def init_git_repo(project_name):
    subprocess.run(['git', 'init'], cwd=project_name, check=True)
    print("Initialized git repository")
