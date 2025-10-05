# 🛠️ OpenOps CLI

A lightweight, extensible command-line utility for rapidly scaffolding OpenOps-compliant project structures.

---

## 📦 What is OpenOps CLI?

OpenOps CLI is a rapid project scaffolding tool built for the [OpenOps.dev](https://openops.dev) ecosystem. It enables developers to spin up a fully structured Python project with pre-defined templates and sensible defaults — ideal for new repositories, internal tools, and data-driven applications.

This CLI aligns with OpenOps conventions for source layout, environment handling, and tooling. It's especially useful for creating reproducible, clean codebases that work seamlessly across your organization.

---

## ⚙️ Features

- 🚀 Scaffold OpenOps-style projects in seconds  
- 📁 Built-in project template structure  
- 🧪 Clean separation of CLI and core logic  
- 🐍 Python virtual environment & editable install support  
- 🧼 Git initialization and cleanup  
- 🧩 Easily extendable with additional commands

---

## 🧰 Requirements

- Python 3.9 or later  
- `pip` package manager  
- Git Bash or WSL for Windows users (for best terminal experience)

---

## 🧪 Installation

You can install the CLI in "editable" mode so that changes to the source code reflect instantly.

1. **Clone the repository**

```bash
git clone https://github.com/OpenOpsDev/openops-cli.git
cd openops-cli
Set up a virtual environment

bash
Copy code
python -m venv .venv
source .venv/Scripts/activate  # On Windows
# OR
source .venv/bin/activate  # On Mac/Linux
Install in editable mode

bash
Copy code
pip install -e .
🚀 Usage
After installing, use the CLI via:

bash
Copy code
openops new <project-name>
This will create a new folder <project-name> using the OpenOps template.

Example
bash
Copy code
openops new my-cool-project
Result:

bash
Copy code
🚀 Creating new OpenOps project 'my-cool-project'...
✅ Project 'my-cool-project' created at: /your/path/my-cool-project
💡 Next steps:
   cd my-cool-project
   python -m venv .venv && source .venv/Scripts/activate
   pip install -e .
📂 Template Structure
The openops-template includes:

css
Copy code
my-cool-project/
├── src/
│   └── openops/
│       ├── __init__.py
│       └── cli.py
├── tests/
├── pyproject.toml
└── README.md
This structure aligns with modern Python packaging standards.

🧩 Project Structure
cpp
Copy code
openops-cli/
├── src/
│   └── openops_cli/
│       ├── __main__.py
│       └── new_project.py
├── templates/
│   └── openops-template/
│       └── (scaffolded project files here)
├── pyproject.toml
├── README.md
└── ...
🛠 Development Tips
You can modify the openops-template/ to customize your own project starter.

Add new CLI subcommands by editing src/openops_cli/__main__.py.

Use print() or click.echo() for debug output.

When editing the CLI logic, no need to reinstall if using pip install -e ..

🧪 Testing Your CLI
Activate your virtual environment, then test by running:

bash
Copy code
openops new test-project
cd test-project
If successful, you’ll see your new project created with all expected files.

❓Troubleshooting
Can't find command openops
Make sure your virtual environment is activated and installed via pip install -e .

Permission denied or command not found on Windows
Use Git Bash or Windows Subsystem for Linux (WSL) instead of Command Prompt or PowerShell.

Changes not reflected in CLI
Ensure you used pip install -e . so your changes reflect in real time.

🔗 Related Projects
OpenOps.dev

Python Packaging Guide

👤 Maintainers
Author: Conston Taylor
Organization: OpenOps.dev