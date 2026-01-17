from venv import create
from os.path import join, expanduser
import subprocess

# Define the directory for the new virtual environment
venv_dir = join(expanduser("~"), "my-venv")

# Create the virtual environment with pip
create(venv_dir, with_pip=True)

# Install packages from requirements.txt (if needed)
subprocess.run([join(venv_dir, "bin", "pip"), "install", "-r", "requirements.txt"], cwd=venv_dir)   