# Copyright 2020-2022 XMOS LIMITED.
# This Software is subject to the terms of the XMOS Public Licence: Version 1.

# -*- coding: utf-8 -*-
#
# Programming Guide documentation build configuration file, created by
# sphinx-quickstart on Wed Jul 15 09:51:17 2020.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os

from sphinx.builders.html import StandaloneHTMLBuilder

# -- Project information -----------------------------------------------------

project = u"lib_xcore_math"
copyright = u"2022, XMOS"
author = "XMOS"

# The full version, including alpha/beta/rc tags
release = "2.1.1"

# -- General configuration ---------------------------------------------------


# NOTE: By default, .png files are favored over .gif.  Reversing the order here in order for anaimated GIFs
#       to be favored.  See: https://www.sphinx-doc.org/en/master/usage/builders/index.html
StandaloneHTMLBuilder.supported_image_types = [
    "image/svg+xml",
    "image/gif",
    "image/png",
    "image/jpeg",
]


extensions = [
    "sphinx.ext.todo",
    "sphinx_copybutton",
    "sphinx_inline_tabs",
    "breathe",
]

# Breathe Configuration
breathe_projects = {"lib_xcore_math": "_build/_doxygen/xml/"}
breathe_default_project = "lib_xcore_math"

breathe_domain_by_extension = { "h" : "c" }

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = [
    "_doxygen",
    "_build",
    "_download",
    "Thumbs.db",
    ".DS_Store",
    "README.rst",
    "requirements.txt",
]

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "furo"

# Can't place logo in subfolder (e.g. ./images/sdk_logo.png) because sphinx is broken (on Windows?) -- correctly copies 
# it to _static/sdk_logo.png, but it tries to load it from _static/images/sdk_logo.png, which doesn't exist.
html_logo = os.path.join(".", "sdk_logo.png")
html_theme_options = {
    "sidebar_hide_name": True,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- Options for sphinx_copybutton -------------------------------------------

copybutton_prompt_text = r"\$ |\(gdb\) "
copybutton_prompt_is_regexp = True