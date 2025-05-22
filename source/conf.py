# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'rtd_sphinx_needs'
copyright = '2025, nick'
author = 'nick'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_needs", "sphinx_plotly_directive"
]

templates_path = ['_templates']
exclude_patterns = []
needs_id_regex = r'^[A-Za-z0-9_]{5,}$'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = ['custom.css']

# -- Needs config------------ -------------------------------------------------
#needs_table_classes = ['no-sphinx-rtd-theme-table-styling']

needs_layouts = {
    'clean': {  # Override the default layout
        'grid': 'simple',
        'layout': {
            'head': ['<<meta("type_name")>>: **<<meta("title")>>** <<meta_id()>> <<collapse_button("meta", collapsed="icon:arrow-down-circle", visible="icon:arrow-right-circle", initial=True)>>'],
            'meta': ['**Status:** <<meta("status")>>', '**Tags:** <<meta("tags")>>', '**Covers:** <<meta_links("covers", incoming=False)>>', '**Covered by:** <<meta_links("covers", incoming=True)>>',
                    '**Validates:** <<meta_links("validates", incoming=False)>>', '**Validated by:** <<meta_links("validates", incoming=True)>>']
        }
    }
}

needs_extra_links = [
    {
        "option": "covers",
        "incoming": "covered by",
        "outgoing": "covers",
        "copy": True,
        "allow_dead_links": True,
    },
    {
        "option": "validates",      # The option name used in RST files
        "incoming": "validated by", # What it's called in the incoming direction
        "outgoing": "validates",    # What it's called in the outgoing direction
        "copy": True,               # Auto-create the reverse link
    },    
]

# In your conf.py file

needs_types = [
    # Default sphinx-needs types
    {
        "directive": "req",
        "title": "Requirement",
        "prefix": "REQ_",
        "color": "#BFD8D2",
        "style": "node",
    },
    {
        "directive": "spec",
        "title": "Specification",
        "prefix": "SPEC_",
        "color": "#FEDCD2",
        "style": "node",
    },
    {
        "directive": "impl",
        "title": "Implementation",
        "prefix": "IMPL_",
        "color": "#DF744A",
        "style": "node",
    },
    {
        "directive": "test",
        "title": "Test Case",
        "prefix": "TEST_",
        "color": "#DCB239",
        "style": "node",
    },
    # Your new type
    {
        "directive": "test_result",
        "title": "Test Result",
        "prefix": "RESULT_",
        "color": "#4CAF50",  # Green for test results
        "style": "node",
    }
]
