from pathlib import Path
from setuptools import setup
import json, subprocess, venv

# read file function for README
def readfile(filename):
    with open(filename, 'r+') as f:
        return f.read()
    
# ROOT and SETUP pathing
ROOT = Path(__file__).resolve().parents[1]
SETUP = Path(__file__).resolve().parents[0]

# load config
config_path = SETUP / "config.json"
config = json.loads(config_path.read_text())

venv_dir = (ROOT / config["venv_dir"]).resolve()
req_file = (SETUP / config["dependencies"]).resolve()

# upgrade_deps=True will upgrade pip/setuptools/wheel after creation
venv.EnvBuilder(with_pip=True, upgrade_deps=True).create(venv_dir)

# use the venv python to run pip
venv_python = venv_dir / "bin" / "python"
subprocess.check_call([str(venv_python), "-m", "pip", "install", "-r", str(req_file)])

# setup(
#     name="GDDownloader",
#     version="2026.01.18",
#     description="CLI Tool for downloading files from Google Drive, made specifically for WSL.",
#     long_description=readfile((ROOT / 'README.MD').resolve()),
#     author="Isaac Wines",
#     author_email="isaacjwines@yahoo.com",
#     url="https://github.com/IsaacWines/Google-Drive-Downloader-Tool",
#     py_modules=['GDDownloader'],
#     license=readfile((ROOT / 'LICENSE.txt').resolve()),
#     entry_points={
#         'console_scripts': [
#             'GDDownloader = GDDownloader:download'
#         ]
#     },
# )
