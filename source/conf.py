# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sys, os

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
plots_path = os.path.join(project_root, "processing", "plots")
sys.path.append(plots_path)
sys.path.append(os.path.dirname(__file__))  # <-- Add this line to make 'conf' importable

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
    {
        "directive": "test_result",
        "title": "Test Result",
        "prefix": "RESULT_",
        "color": "#4CAF50",
        "style": "node",
    }
]

needs_layouts = {

    'req': {
        'grid': 'simple',
        'layout': {
            'head': ['<<meta("type_name")>>: **<<meta("title")>>** <<meta_id()>> <<collapse_button("meta", collapsed="icon:arrow-down-circle", visible="icon:arrow-right-circle", initial=True)>>'],
            'meta': ['**Status:** <<meta("status")>>', '**Tags:** <<meta("tags")>>', '**Covered by:** <<meta_links("covers", incoming=True)>>',
                    ]
        }
    },    
    'test': {
        'grid': 'simple',
        'layout': {
            'head': ['<<meta("type_name")>>: **<<meta("title")>>** <<meta_id()>> <<collapse_button("meta", collapsed="icon:arrow-down-circle", visible="icon:arrow-right-circle", initial=True)>>'],
            'meta': ['**Status:** <<meta("status")>>', '**Tags:** <<meta("tags")>>', '**Covers:** <<meta_links("covers", incoming=False)>>', '**Validated by:** <<meta_links("validates", incoming=True)>>',
                    ]
        }
    },
    'result': {
        'grid': 'simple',
        'layout': {
            'head': ['<<meta("type_name")>>: **<<meta("title")>>** <<meta_id()>> <<collapse_button("meta", collapsed="icon:arrow-down-circle", visible="icon:arrow-right-circle", initial=True)>>'],
            'meta': ['**Status:** <<meta("status")>>', '**Tags:** <<meta("tags")>>',
                    '**Validates:** <<meta_links("validates", incoming=False)>>',
                    '**Margin:** <<meta("margin")>> dB']
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
        "allow_dead_links": True,
    },    
]

# Add to your configuration
needs_extra_options = ['validated_by_result', 'margin']


# -- Custom functions------------ -------------------------------------------------

def find_test_result_ids(app, need, needs, *args, **kwargs):
    """
    This function finds all test results that validate a given requirement.
    It allows a needtable to display requirements, test cases, and their associated test results.
    """
    if need['type'] != 'req':
        return ""
    
    test_results = []
    
    # Find test cases that cover this requirement
    for need_id, other_need in needs.items():
        if other_need['type'] == 'test' and need['id'] in other_need.get('covers', []):
            # Find test results that validate this test case
            for result_id, result_need in needs.items():
                if (result_need['type'] == 'test_result' and 
                    need_id in result_need.get('validates', [])):
                    test_results.append(result_id)
                    # Also add the reverse link
                    if 'validates' not in needs[result_id]:
                        needs[result_id]['validates'] = []
                    if need['id'] not in needs[result_id]['validates']:
                        needs[result_id]['validates'].append(need['id'])
    
    return ""  # Don't return anything for display    

def calc_margin(app, need, needs, *args, **kwargs):
    return 99

# Add to configuration
needs_functions = [find_test_result_ids, calc_margin]