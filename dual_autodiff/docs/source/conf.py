# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

#-- Path setup -----------------------------------------------------
# Add paths
import os
import sys
sys.path.insert(0, os.path.abspath('/Users/conkey/Documents/dual_autodiff'))  # Ensure your package is in the path

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'c1_coursework'
copyright = '2024, Lewis McConkey'
author = 'Lewis McConkey'
release = 'v1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Extensions
extensions = [
    'sphinx.ext.autodoc',    # Auto-generate documentation from docstrings
    'sphinx.ext.napoleon',   # Support for Google/NumPy-style docstrings
    'sphinx.ext.viewcode',   # Add links to source code
    'nbsphinx',              # Render Jupyter notebooks
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

