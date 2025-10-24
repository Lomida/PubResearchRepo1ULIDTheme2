import os
import sys
sys.path.insert(0, os.path.abspath('../src'))

html_theme = 'unary_theme'
html_theme_path = ['_themes']

exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
    'venv',
    '.venv',
    'sphinx_venv',
    'sphinx_venv/**',
    '**/sphinx_venv/**',
    '**/__pycache__',
    '**/*.pyc',
    '_static',
    '_templates',
]

html_theme_options = {
    'logo_image': 'logo.svg',
    'logo_link': 'https://www.unarylab.com/,

    'nav_link_1_text': 'Documentation',
    'nav_link_1_url': 'https://docs.example.com',

    'nav_link_2_text': 'GitHub',
    'nav_link_2_url': 'https://github.com/yourusername/yourrepo',
    
    'nav_link_3_text': 'About',
    'nav_link_3_url': 'https://example.com/about',
}

html_static_path = ['_static']