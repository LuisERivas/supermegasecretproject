#!/usr/bin/env python3
import subprocess
from pathlib import Path
import tkinter as tk
from tkinter import messagebox


def run_git_clone(repo_url: str, dest_dir: Path):
    """Clone a git repository into the destination directory."""
    subprocess.run(
        ["git", "clone", repo_url],
        cwd=str(dest_dir),
        check=True
    )


def main():
    # Initialize Tkinter (hidden root window)
    root = tk.Tk()
    root.withdraw()

    # 1) Ask user if they want to proceed
    proceed = messagebox.askyesno("Setup", "Proceed with the repository setup?")
    if not proceed:
        messagebox.showinfo("Setup", "Cancelled.")
        return

    # 2) Find current file location, go up TWO directories, create new folder
    current_dir = Path(__file__).resolve().parent
    parent_dir = current_dir.parent.parent   # <-- goes up two levels

    # Folder name is fixed
    folder_name = "project_Folder"
    new_folder = parent_dir / folder_name
    new_folder.mkdir(parents=True, exist_ok=True)

    # 3) Repo URL placeholders (user will manually replace these)
    repo1 = "https://github.com/your-org/repo1.git"
    repo2 = "https://github.com/your-org/repo2.git"

    # 4) Clone repos
    try:
        run_git_clone(repo1, new_folder)
        run_git_clone(repo2, new_folder)
    except subprocess.CalledProcessError:
        messagebox.showerror(
            "Setup Error",
            "Git clone failed.\n\nMake sure you replaced the placeholder repo URLs."
        )
        return

    # 5) Let user know repos have been cloned
    messagebox.showinfo(
        "Setup Complete",
        f"Both repositories have been cloned into:\n\n{new_folder}"
    )

    # 6) Wait for user confirmation and exit
    messagebox.showinfo("Exit", "Press OK to close the setup.")


if __name__ == "__main__":
    main()
