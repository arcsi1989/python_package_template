"""
Author: @arcsi1989
"""

import click

from src.cli import src_cli


@src_cli.command(help_priority=4)
@click.help_option("-h")
@click.option("-e", "--example",
              type=click.Choice(['option-A', 'option-B'], case_sensitive=False),
              default="option-A",
              help="Select an option; Valid values are 'option-A' and 'option-B'.")
def example(*args, **kwargs):
    ...
    # TODO define method to be executed
    # Alternatively one could define a example_exec(*args, **kwargs) separate method
    # if this method should be called separately
