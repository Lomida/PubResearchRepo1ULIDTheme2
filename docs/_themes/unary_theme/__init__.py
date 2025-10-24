from pathlib import Path

def get_theme_path():
    \"\"\"Return path to theme directory.\"\"\"
    return str(Path(__file__).parent.resolve())

def setup(app):
    \"\"\"Setup function called by Sphinx.\"\"\"
    app.add_html_theme('custom_theme', get_theme_path())
    return {
        'version': '0.1.0',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }