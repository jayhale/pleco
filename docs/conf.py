# -- Project information -----------------------------------------------------

project = "Pleco"
copyright = "2025, James Hale"
author = "James Hale"

# -- General configuration ---------------------------------------------------

extensions = ["sphinx.ext.autodoc", "sphinx.ext.autosummary"]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

autodoc_class_signature = "separated"
autosummary_generate = True
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
