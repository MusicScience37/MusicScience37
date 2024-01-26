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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = "MusicScience37"
copyright = "2022, MusicScience37 (Kenta Kabashima)"
author = "MusicScience37"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_parser",
    "sphinxcontrib.youtube",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# setting of opengraph
# https://pypi.org/project/sphinxext-opengraph/
extensions += ["sphinxext.opengraph"]
ogp_site_url = "https://www.musicscience37.com/ja/"
ogp_site_name = "MusicScience37"
ogp_image = "https://kicon.musicscience37.com/KIcon128white.png"


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_orange_book_theme"


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = [
    "_static",
]


html_title = "MusicScience37"

html_logo = "https://kicon.musicscience37.com/KIcon80.png"
html_favicon = "https://kicon.musicscience37.com/KIcon.ico"

html_theme_options = {
    "show_prev_next": False,
    "logo": {
        "text": html_title,
    },
    "pygment_light_style": "gruvbox-light",
    "pygment_dark_style": "native",
    "repository_url": "https://gitlab.com/MusicScience37/MusicScience37",
    "use_repository_button": True,
}


# -- Options for internationalization ----------------------------------------

language = "ja"
locale_dirs = ["locale/"]
gettext_compact = False
