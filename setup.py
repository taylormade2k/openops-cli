from setuptools import setup, find_packages

setup(
    name="openops-cli",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "click",
        "jinja2",
    ],
    entry_points={
        "console_scripts": [
            "openops=openops_cli.__main__:main",
        ],
    },
)
