import subprocess
import sys

def update_repo():
    try:
        print(f"Pulling latest changes in ...")
        subprocess.run(
            ["git", "pull"],
            check=True,
            capture_output=True,
            text=True
        )
    except subprocess.CalledProcessError as e:
        print("Error pulling from remote:", e.stderr.strip())
        sys.exit(1)

def print_commits_by_day(contributor):
    try:
        result = subprocess.run(
            [
                "git", "log",
                f"--author={contributor}",
                "--since=3.days",
                "--pretty=format:%ad|%s",
                "--date=short"
            ],
            capture_output=True,
            text=True,
            check=True
        )
    except subprocess.CalledProcessError as e:
        print("Git error:", e.stderr.strip())
        return

    output = result.stdout.strip()
    if not output:
        print("No commits found.")
        return

    last_date = None
    for line in output.splitlines():
        try:
            date_str, message = line.split("|", 1)
        except ValueError:
            continue

        if date_str != last_date:
            print(f"\nDate: {date_str}")
            last_date = date_str
        print(f"  - {message.strip()}")
        
        
def main():
    if len(sys.argv) != 2:
        print("Usage: git jirate <contributor>")
        sys.exit(1)

    contributor = sys.argv[1]

    update_repo()
    print_commits_by_day(contributor)

if __name__ == "__main__":
    main()

