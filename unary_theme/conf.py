import os
import sys

sys.path.append(os.path.abspath('.'))

html_theme = 'unary_theme'
html_theme_path = ['_themes']

exclude_patterns = [
    '_build',     
    'Thumbs.db',       
    '.DS_Store',         
    'venv',              
    '.venv',             
    '_static',           
    '_templates',        
    'conf.py',           
    'Makefile',          
    'make.bat',         
    '**/__pycache__',    
    '**/*.pyc',          
    'docs/_build',      
    'docs/_static',     
    'docs/_templates',   
    '.git',              
    '.github'         
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