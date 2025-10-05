# -*- coding: utf-8 -*-

import os
import shutil
import sys
from pathlib import Path

def create_new_project(name: str):
    """Scaffold a new project using the OpenOps template."""
    base_dir = Path(__file__).resolve().parents[2] / "templates" / "openops-template"
    target_dir = Path.cwd() / name

    if target_dir.exists():
        print(f"‚ùå Folder '{name}' already exists.")
        sys.exit(1)

    print(f"Ì∫Ä Creating new OpenOps project '{name}'...")

    shutil.copytree(base_dir, target_dir)

    git_dir = target_dir / ".git"
    if git_dir.exists():
        shutil.rmtree(git_dir)

    print(f"‚úÖ Project '{name}' created at: {target_dir.resolve()}")
    print("Ì≤° Next steps:")
    print(f"   cd {name}")
    print("   python -m venv .venv && source .venv/Scripts/activate")
    print("   pip install -e .")

