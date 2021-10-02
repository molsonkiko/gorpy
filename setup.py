from setuptools import setup
import os

import gorpy.gorp as package


with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README.md')) as f:
    readme = f.read()

setup(
    name='gorpy',
    version=package.__version__,
    packages=['gorp'],
    # package_data={'gorp': ['cmap/*.pickle.gz']},
    install_requires=[
        'math_eval',
        'python-dateutil',
    ],
    extras_require={
        "pdf": ["pdfminer.six", "sortedcollections"],
        "docs": ["sphinx", "sphinx-argparse"],
        "docx": ['docx'],
        'tab': ['pandas'],
        'x_option': ['lxml', 'cssselect'],
        'xl': ['openpyxl'],
        'y_option': ['pyyaml'],
    },
    description='Grep tool with extensions for reading files in many different ways',
    long_description=readme,
    long_description_content_type='text/markdown',
    license='MIT/X',
    author='Mark Johnston Olson',
    author_email='mjolsonsfca@gmail.com',
    url='https://github.com/molsonkiko/gorpy',
    # scripts=[ # maybe __main__ should be considered a script?
    # ],
    keywords=[
        'grep tool',
        'text mining',
        'JSON analysis',
    ],
    python_requires='>=3.6',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Topic :: Text Processing',
    ],
)