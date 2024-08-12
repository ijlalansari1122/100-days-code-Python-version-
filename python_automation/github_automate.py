import subprocess

def run_command(command):
    """Runs a shell command and returns the output."""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print(result.stdout)
    else:
        print(f"Error: {result.stderr}")

def add_changes():
    run_command("git add .")

def commit_changes():
    commit_message = input("Enter the commit message: ")
    run_command(f'git commit -m "{commit_message}"')

def push_changes(branch_name="master"):
    run_command(f"git push origin {branch_name}")

def pull_updates(branch_name="master"):
    run_command(f"git pull origin {branch_name}")

# Example Usage
if __name__ == "__main__":
    # Pull latest updates from the master branch
    pull_updates()

    # Add all changes
    add_changes()

    # Commit changes with a message provided by the user
    commit_changes()

    # Push changes to the master branch
    push_changes()
