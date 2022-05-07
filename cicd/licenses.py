#!/usr/bin/env python
#
# Sub-packages licenses manager: Update the licenses of the packages present in the production requirements.

"""
Author: @matteobe
"""

import re
from pathlib import Path


def update_licenses(requirements_file: Path):
    """
    Retrieve the licenses of the packages used in the Template package and add them to the licenses folder

    Args:
        requirements_file (str):
    """

    with open(requirements_file, "r") as f:
        requirements = f.read()

    packages = re.findall(r"^[^#^\n]+", requirements, re.MULTILINE)

    # TODO: Retrieve the licenses from the respective repos and update here


if __name__ == "__main__":
    requirements = Path(".").parent / "requirements" / "production.txt"
    update_licenses(requirements)
