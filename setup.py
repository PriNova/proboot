from setuptools import setup, find_packages

setup(
    name='proboot',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'proboot=proboot:main',
        ],
    },
    install_requires=[
        'argparse',
    ],
    python_requires='>=3.10',
    author='PriNova',
    author_email='info@prinova.de',
    description='A CLI tool for bootstrapping Python projects',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/PriNova/bootstrap-apps',
    license='MIT',
)
