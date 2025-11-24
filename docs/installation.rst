Installation
============

Requirements
------------

- Python 3.6 or higher
- Operating System: Windows 10+, Linux, or macOS
- Terminal with TTY support (for automatic color detection)

Standard Installation
---------------------

Using pip
~~~~~~~~~

The easiest way to install make_colors is using pip:

.. code-block:: bash

   pip install make_colors

From Source
~~~~~~~~~~~

You can also install from source:

.. code-block:: bash

   git clone https://github.com/cumulus13/make_colors.git
   cd make_colors
   pip install -e .

Development Installation
------------------------

For development, install with additional dependencies:

.. code-block:: bash

   git clone https://github.com/cumulus13/make_colors.git
   cd make_colors
   pip install -e ".[dev]"

This installs additional tools for:

- Running tests
- Building documentation
- Code formatting and linting

Verifying Installation
----------------------

After installation, verify that make_colors is working correctly:

.. code-block:: python

   from make_colors import make_colors, MakeColors
   
   # Test basic functionality
   print(make_colors("Installation successful!", "green"))
   
   # Check color support
   if MakeColors.supports_color():
       print(make_colors("✓ Color support detected", "lightgreen"))
   else:
       print("⚠ No color support detected")

Platform-Specific Notes
-----------------------

Windows
~~~~~~~

On Windows 10 and later, ANSI escape sequences are supported by default. For earlier versions of Windows, you may need to:

1. Use a terminal emulator that supports ANSI codes (e.g., Windows Terminal, ConEmu)
2. Enable ANSICON environment variable
3. Use the ``force=True`` parameter to bypass color support detection

.. code-block:: python

   # Force colors on older Windows systems
   print(make_colors("Forced colors", "red", force=True))

Linux/macOS
~~~~~~~~~~~

Most modern terminals on Linux and macOS support ANSI escape codes by default. No additional configuration is needed.

Terminal Compatibility
~~~~~~~~~~~~~~~~~~~~~~

The following terminals are tested and confirmed to work:

- **Windows**: Windows Terminal, PowerShell, CMD (Win10+), ConEmu, Cmder
- **Linux**: GNOME Terminal, Konsole, xterm, rxvt, Terminator
- **macOS**: Terminal.app, iTerm2, Hyper
- **Cross-platform**: VS Code integrated terminal, PyCharm terminal

Upgrading
---------

To upgrade to the latest version:

.. code-block:: bash

   pip install --upgrade make_colors

Uninstallation
--------------

To remove make_colors:

.. code-block:: bash

   pip uninstall make_colors

Troubleshooting
---------------

No Colors Displayed
~~~~~~~~~~~~~~~~~~~

If colors are not appearing in your terminal:

1. Check if your terminal supports ANSI escape codes
2. Verify that output is going to a TTY (not redirected to a file)
3. Check environment variables: ``MAKE_COLORS`` should not be set to ``0``
4. Try forcing colors with ``force=True`` parameter

.. code-block:: python

   # Debug color support
   from make_colors import MakeColors
   import sys
   
   print(f"TTY detected: {sys.stdout.isatty()}")
   print(f"Color support: {MakeColors.supports_color()}")
   print(f"Platform: {sys.platform}")

Import Errors
~~~~~~~~~~~~~

If you encounter import errors:

.. code-block:: bash

   # Reinstall the package
   pip uninstall make_colors
   pip install make_colors
   
   # Or install from source
   pip install git+https://github.com/cumulus13/make_colors.git

Next Steps
----------

Now that you have make_colors installed, proceed to:

- :doc:`quickstart` - Learn basic usage
- :doc:`usage` - Explore all features
- :doc:`examples` - See practical examples