"""Generate Sphinx documentation from Python docstrings."""

from pathlib import Path
import shutil
import tomllib

# Read version from pyproject.toml
pyproject_path = Path(__file__).parent.parent / "pyproject.toml"
with open(pyproject_path, "rb") as f:
    pyproject = tomllib.load(f)
    version = pyproject["project"]["version"]
    project_name = pyproject["project"]["name"]
    project_description = pyproject["project"]["description"]

# Create docs/source directory structure
docs_source = Path("docs/source")
docs_source.mkdir(parents=True, exist_ok=True)

# Remove old modules.rst if it exists
old_modules = docs_source / "modules.rst"
if old_modules.exists():
    old_modules.unlink()

# Create required subdirectories
(docs_source / "_static").mkdir(exist_ok=True)
(docs_source / "_templates").mkdir(exist_ok=True)

# Create conf.py for Sphinx
conf_py = docs_source / "conf.py"
conf_py.write_text(f'''"""Sphinx configuration for {project_name}."""

import sys
from pathlib import Path

# Add the project root to sys.path so autodoc can find the modules
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

project = "{project_name}"
author = "Your Name"
version = "{version}"
release = "{version}"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
''')

# Create index.rst
index_rst = docs_source / "index.rst"
index_rst.write_text(f"""{project_name} Documentation
{'=' * len(project_name + ' Documentation')}

**Version:** {version}

{project_description}

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   api

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
""")

# Create api.rst for autodoc
api_rst = docs_source / "api.rst"
api_rst.write_text("""API Reference
=============

.. automodule:: src.calculator
   :members:
   :undoc-members:
   :show-inheritance:
""")

print("Documentation source files generated successfully!")
