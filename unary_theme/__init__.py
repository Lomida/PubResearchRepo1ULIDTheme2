"""unary lab theme."""
from pathlib import Path
from os import path

__version__ = '0.1.0'


# Depreciated in newer Sphinx
def get_html_theme_path():
    """Return list of HTML theme paths"""
    return [path.abspath(path.dirname(__file__))]


def get_path():
    """Return path to theme directory
    
    This is used by Sphinx's html_theme_path configuration.
    """
    return path.abspath(path.dirname(path.dirname(__file__)))


def setup(app):
    """Setup function called by Sphinx"""
    app.add_html_theme('unary_theme', path.abspath(path.dirname(__file__)))
    
    return {
        'version': __version__,
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }