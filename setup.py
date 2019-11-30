from pathlib import Path

from setuptools import find_packages, setup

import hellopy

readme = Path(__file__).with_name('README.md').read_text()

classifiers = [
    'Environment :: Console',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
]

setup(
    name='hellopy',
    version=hellopy.__version__,
    description='Hello, Python!',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/xymy/hellopy',
    author='xymy',
    author_email='thyfan@163.com',
    classifiers=classifiers,
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'hellopy = hellopy.hellopy:main'
        ]
    },
    python_requires='>=3.6'
)
