from venv import create
from os.path import join, expanduser
import subprocess, json

# loading the config file
with open("./setup/config.json", 'r') as config:
    config = config.load()

# Create the virtual environment with pip
create(config["venv_dir"], with_pip=True)

# Install packages from requirements.txt
subprocess.run([join(config["venv_dir"], "bin", "pip"), "install", "-r", config["dependancies"]], cwd=config["venv_dir"])   