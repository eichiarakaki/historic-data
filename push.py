import os
import sys
import subprocess

def main():
    if len(sys.argv) < 2:
        print("Please provide the repository path and commit message")
        print("Use: push.py '[COMMIT_MSG]'")
        sys.exit(1)

    commit_msg = sys.argv[1]

    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", commit_msg], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("Changes pushed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
