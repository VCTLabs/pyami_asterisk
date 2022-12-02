# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

import pkg_resources
from recommonmark.parser import CommonMarkParser

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

__version__ = pkg_resources.get_distribution('pyami_asterisk').version

def visit_document(*_):
    pass


# Removes irrelevant warning messages during md file parsing.
# REF: https://github.com/readthedocs/recommonmark/issues/177
# Hopefully will be unnecessary in the future...
setattr(CommonMarkParser, 'visit_document', visit_document)

# -- Project information -----------------------------------------------------

project = 'pyami_asterisk'
copyright = '2022, Denis Streltsov'
author = 'Denis Streltsov'

description = 'AsyncIO python library to play with Asterisk Manager Interface (AMI)'
# The full version, including alpha/beta/rc tags
version = __version__
release = version


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_git',
    'sphinxcontrib.apidoc',
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
    'recommonmark',
]

apidoc_module_dir = '../../pyami_asterisk/'
apidoc_output_dir = 'api'
apidoc_excluded_paths = ['tests']
apidoc_separate_modules = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The master toctree document.
master_doc = 'index'

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = ['.rst', '.md']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build']

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
#html_theme = "alabaster"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# theme => alabaster
# html_theme_options = {
    # "show_powered_by": False,
    # "github_user": "streltsovdenis",
    # "github_repo": "pyami_asterisk",
    # "github_banner": True,
    # "github_button": True,
    # "github_type": "star",
    # "show_related": False,
# }

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = False

# Output file base name for HTML help builder.
htmlhelp_basename = 'pyami_asteriskdoc'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  (master_doc, 'pyami_asterisk.tex', 'pyami_asterisk Documentation',
   [author], 'manual'),
]

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'pyami_asterisk', 'pyami_asterisk Documentation',
     [author], 1)
]

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  (master_doc, 'pyami_asterisk', 'pyami_asterisk Documentation',
   author, 'pyami_asterisk', description,
   'Miscellaneous'),
]
