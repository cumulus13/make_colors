Welcome to make_colors Documentation
====================================

**make_colors** is a comprehensive Python module for creating colored text output in terminals with support for both ANSI escape codes and Rich console formatting. It provides cross-platform compatibility for Windows 10+, Linux, and macOS terminals.

.. image:: https://img.shields.io/badge/python-3.6+-blue.svg
   :target: https://www.python.org/downloads/
   :alt: Python Version

.. image:: https://img.shields.io/badge/license-MIT-green.svg
   :target: https://github.com/cumulus13/make_colors/blob/master/LICENSE
   :alt: License

.. image:: _static/example_usage.gif
   :alt: Example usage

Key Features
------------

- 🎨 **ANSI Escape Code Based Coloring** - Full support for terminal colors
- 🌈 **Rich Console Format Support** - Advanced text formatting
- 💻 **Windows Console Color Support** - Native Windows 10+ compatibility
- 🔧 **Environment Variable Controls** - Global color settings management
- ⚡ **Flexible Color Specification** - Full names, abbreviations, or codes
- 🎭 **Background and Foreground Combinations** - Mix and match colors
- 📝 **Multiple Rich Markup Tags** - Complex formatting support
- ⚙️ **Attribute Detection** - Parse attributes from color strings
- 🔄 **Multiple Separators Support** - Use `-`, `_`, or `,` as delimiters

Quick Start
-----------

Installation
~~~~~~~~~~~~

.. code-block:: bash

   pip install make_colors

Basic Usage
~~~~~~~~~~~

.. code-block:: python

   from make_colors import make_colors

   # Simple colored text
   print(make_colors("Hello World!", "red"))
   
   # With background
   print(make_colors("Warning!", "yellow", "on_black"))
   
   # Using abbreviations
   print(make_colors("Info", "lb"))  # Light blue
   
   # Rich markup format
   print(make_colors("[bold red]Error![/]"))
   
   # Attribute detection (NEW!)
   print(make_colors("Success", "bold-green"))

Documentation Contents
----------------------

.. toctree::
   :maxdepth: 2
   :caption: User Guide
   
   installation
   quickstart
   usage
   examples
   rich_markup
   attributes

.. toctree::
   :maxdepth: 2
   :caption: API Reference
   
   api/main_functions
   api/classes
   api/utilities
   api/constants

.. toctree::
   :maxdepth: 1
   :caption: Advanced Topics
   
   advanced/environment_vars
   advanced/performance
   advanced/cross_platform
   advanced/custom_formatters

.. toctree::
   :maxdepth: 1
   :caption: Additional Information
   
   changelog
   contributing
   license

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`