# -*- coding: utf-8 -*-

import click
from .new_project import create_new_project

@click.group()
def cli():
    """OpenOps CLI - Scaffolding and automation for OpenOps projects."""
    pass

@cli.command()
@click.argument("name")
def new(name):
    """Create a new OpenOps project."""
    create_new_project(name)

def main():
    cli()

if __name__ == "__main__":
    main()
