.. gorpy documentation master file, created by
   sphinx-quickstart on Fri Oct  1 10:14:51 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. to build this as HTML, use the terminal, go to gorp's directory, and enter
   sphinx-build -b html docs/source docs/build/html
   
.. 80 characters is the recommended maximum line length for reST.

Welcome to gorpy's documentation!
=================================
**gorpy: Good Old Regex and Python**

This is a grep/sed/ls/mv tool for Python 3.6-3.9 that includes:
    * piping syntax, 
    * a built-in jsonpath implementation for searching and manipulating JSON/YAML documents, comparable to jsonpath_ng in power and extensibility.
    * Text extraction from PDF's and Word documents
    * support for XPath and CSS selectors to filter HTML and XML documents
    * automatically opening all files found if desired (-p option)
    * and much more

It can be conveniently used via the command line, through an interactive prompt,
    or programmatically using a :class:`.readfiles.GorpSession` object.

Wait: yet another grep tool? Didn't we already have enough of those?

Yes, no doubt. For sed-type tasks, you're probably better off using the Unix 
    standard grep or something similar. I personally will continue using 
    Notepad++ to edit my text files most of the time.

For renaming and finding files, I will usually stick to the Windows File 
Explorer.

I envision gorpy being most useful as a tool for editing JSON and YAML based on 
    the strength of the jsonpath module.
I also find the ability to automatically open files found convenient.

.. note:: This project is under active development.
    
    Features to be added soon:
    
    * a "tab" option for reading in tabular files (e.g. csv) and Excel documents as pandas DataFrames
        - you could use the same jsonpath query language to manipulate and filter these DataFrames just like JSON and YAML documents 

Table of Contents
==================

.. toctree::
   :maxdepth: 2
   
   installation
   command line
   modules/jsonpath
   modules/readfiles

.. the ".." precedes a comment
   this is in the same comment block (because of indentation)
   the first dedented line after the beginning of the block marks the end of the block

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
