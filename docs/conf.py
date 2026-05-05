"""Sphinx configuration for YanglabPDK documentation."""

from __future__ import annotations

import sys
from pathlib import Path


DOCS_DIR = Path(__file__).resolve().parent
PACKAGE_DIR = DOCS_DIR.parent
PACKAGE_PARENT = PACKAGE_DIR.parent

sys.path.insert(0, str(PACKAGE_PARENT))

project = "YanglabPDK"
author = "Prof. Lan Yang Lab"
copyright = "2026, Prof. Lan Yang Lab"

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]

source_suffix = {
    ".md": "markdown",
}

master_doc = "index"
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
]

html_theme = "furo"
html_title = "YanglabPDK"
html_static_path = ["_static"]

autodoc_member_order = "bysource"
autodoc_typehints = "description"
napoleon_google_docstring = True
napoleon_numpy_docstring = True

# These mocks keep Sphinx useful even on a documentation-only environment.  The
# recommended build path is still the normal layout environment with gdsfactory
# installed, because that enables accurate API imports and preview rendering.
autodoc_mock_imports = [
    "gdsfactory",
    "kfactory",
    "klayout",
]

myst_enable_extensions = [
    "colon_fence",
]
myst_heading_anchors = 3
