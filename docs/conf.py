import os
import sys

sys.path.append(os.path.abspath('.'))

html_theme = 'unary_lab_theme'
html_theme_path = ['_themes']

html_theme_options = {
    'logo_image': 'logo.svg',
    'logo_link': 'https://example.com',
    'nav_link_1_text': 'Documentation',
    'nav_link_1_url': 'https://docs.example.com',
    'nav_link_2_text': 'GitHub',
    'nav_link_2_url': 'https://github.com/yourusername/yourrepo',
    'nav_link_3_text': 'About',
    'nav_link_3_url': 'https://example.com/about',
}

html_static_path = ['_static']