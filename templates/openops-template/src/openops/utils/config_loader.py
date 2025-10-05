import json
import yaml
from pathlib import Path

def load_config(path: str):
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(f"Config not found: {path}")
    if file_path.suffix in [".yaml", ".yml"]:
        with open(file_path, "r") as f:
            return yaml.safe_load(f)
    elif file_path.suffix == ".json":
        with open(file_path, "r") as f:
            return json.load(f)
    else:
        raise ValueError("Unsupported config format (use YAML or JSON)")
