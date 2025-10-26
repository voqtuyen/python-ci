"""Generate Sphinx documentation from Python docstrings."""

from pathlib import Path

# Create docs/source directory structure
docs_source = Path("docs/source")
docs_source.mkdir(parents=True, exist_ok=True)

# Create conf.py for Sphinx
conf_py = docs_source / "conf.py"
conf_py.write_text('''"""Sphinx configuration for python-calculator."""

project = "python-calculator"
author = "Your Name"
version = "0.1.0"
release = "0.1.0"

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
index_rst.write_text("""python-calculator Documentation
===============================

Welcome to the python-calculator documentation.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
''')

# Create modules.rst for autodoc
modules_rst = docs_source / "modules.rst"
modules_rst.write_text('''API Reference
=============

.. autosummary::
   :toctree: generated

   calculator

.. automodule:: src.calculator
   :members:
   :undoc-members:
   :show-inheritance:
""")

print("Documentation source files generated successfully!")
