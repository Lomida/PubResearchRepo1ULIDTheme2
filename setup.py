from setuptools import setup, find_packages

setup(
    name='unary_theme',
    version='0.1.0',
    description='the unary lab theme',
    author='Devon Lister',
    author_email='DevonLister@yahoo.com',
    url='https://github.com/Lomida/PubResearchRepo1ULIDTheme2',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'sphinx>=4.0',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ],
    entry_points={
        'sphinx.html_themes': [
            'unary_theme = unary_theme',
        ]
    },
)