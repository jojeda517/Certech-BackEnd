import os
import sys
from django.conf import settings

sys.path.insert(0, os.path.abspath("..")) 

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Certech'
copyright = '2024, José Ojeda, Karen Moyolema, Eduardo Pila, Anthony Solis, Jonathan Villafuerte'
author = 'José Ojeda, Karen Moyolema, Eduardo Pila, Anthony Solis, Jonathan Villafuerte'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    # ...
    'sphinx.ext.autodoc',
    # ...
]

templates_path = ['_templates']
exclude_patterns = []

language = 'es'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
