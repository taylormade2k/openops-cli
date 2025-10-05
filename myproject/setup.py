from setuptools import setup, find_packages

setup(
    name="openops-template",
    version="0.1.0",
    author="OpenOps.dev",
    description="OpenOps.dev project template",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "openops-template=openops_module.cli:main"
        ]
    },
)
