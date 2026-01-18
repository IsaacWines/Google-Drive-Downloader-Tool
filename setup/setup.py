from pathlib import Path
import json
import subprocess
import venv

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
