=========
Changelog
=========

All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog <https://keepachangelog.com/en/1.0.0/>`_,
and this project adheres to `Semantic Versioning <https://semver.org/spec/v2.0.0.html>`_.

Version 3.48.6 ~ (2025-11-24 15:00:38:013178)
===============================================

Major Release - Table Module & Enhanced Features
-------------------------------------------------

Added
~~~~~

Table Module
^^^^^^^^^^^^

* **NEW: Table Module** - Create beautiful colored tables with Rich-style API

  - Rich-style API with ``add_column()`` and ``add_row()``
  - Traditional API compatible with classic table libraries
  - Full Rich markup support in headers, cells, and titles
  - Column-based styling with ``set_cols_color()``
  - Row-based styling with ``set_rows_color()``
  - Flexible alignment (horizontal and vertical)
  - Data type formatting (auto, text, float, exponential, integer)
  - Border customization and decoration control
  - All make_colors formats supported (abbreviations, full names, attributes)

  .. code-block:: python

      from make_colors.table import Table

      table = Table(title="Server Status", title_style="bold cyan")
      table.add_column("Service", style="bold")
      table.add_column("[white on blue]Status[/]")
      table.add_row("Web Server", "✓ Running")
      print(table.draw())

* **Column Colors** - ``set_cols_color()`` method for setting colors per column

  .. code-block:: python

      table.set_cols_color(["y", "r", "c"])  # yellow, red, cyan
      table.set_cols_color(["bold-red", "italic-cyan", "dim-yellow"])

* **Row Colors** - ``set_rows_color()`` method for setting colors per row

  .. code-block:: python

      # Status-based coloring
      table.set_rows_color(["green", "yellow", "bold-red", None])
      
      # Zebra striping
      table.set_rows_color(["dim", None, "dim", None, "dim"])

* **Rich Markup in Tables** - Full support for Rich markup format

  .. code-block:: python

      table.add_column("[bold white]Name[/]")
      table.add_column("[white on blue]Status[/]")
      table = Table(title="[bold cyan]My Report[/]")

Attribute Detection
^^^^^^^^^^^^^^^^^^^

* **Automatic Attribute Detection** - Detect text attributes from color strings

  .. code-block:: python

      from make_colors import make_colors
      
      # Bold text
      print(make_colors("Bold red", "bold-red"))
      
      # Italic text with background
      print(make_colors("Styled", "italic-blue-yellow"))
      
      # Multiple attributes
      print(make_colors("Complex", "bold-underline-green"))

* **Multiple Separator Support** - Use hyphen, underscore, or comma

  - Hyphen: ``"bold-red-yellow"``
  - Underscore: ``"italic_blue_white"``
  - Comma: ``"underline,green,black"``

* **Attribute List**:

  ================= =============================================
  Attribute         Description
  ================= =============================================
  ``bold``          Bold or bright text
  ``dim``           Dimmed text
  ``italic``        Italic text (terminal dependent)
  ``underline``     Underlined text
  ``blink``         Blinking text
  ``reverse``       Reverse foreground and background
  ``strikethrough`` Strikethrough text
  ``strike``        Alias for strikethrough
  ================= =============================================

Magic Functions
^^^^^^^^^^^^^^^

* **Direct color functions** - Call colors as functions

  .. code-block:: python

      from make_colors import *
      
      print(red("Error!"))
      print(bl("I'm Blue"))
      print(green_on_black("Success"))
      
      # Abbreviations
      print(w_bl("White on Blue"))
      print(lb_b("Light Blue on Black"))

* **Color class** - Object-oriented color handling

  .. code-block:: python

      from make_colors import Color, Colors
      
      color = Color('red', 'white')
      print(color("Text"))
      
      colors = Colors('white', 'blue')
      print(colors("Another text"))

Enhanced Features
^^^^^^^^^^^^^^^^^

* **Console class** - Alternative print interface

  .. code-block:: python

      from make_colors import Console
      
      console = Console()
      console.print("[white on red]Error message[/]")

* **Confirm class** - Interactive confirmation prompts

  .. code-block:: python

      from make_colors import Confirm
      
      if Confirm.ask("Are you sure?"):
          print("Confirmed!")

* **print_exception()** - Colored exception printing

  .. code-block:: python

      from make_colors import print_exception
      
      try:
          raise ValueError("Something went wrong")
      except:
          print_exception(tb_color="lc", tp_color="y", tv_color="white-red-blink")

* **MakeColorsHelpFormatter** - Colored argparse help

  .. code-block:: python

      import argparse
      from make_colors import MakeColorsHelpFormatter
      
      parser = argparse.ArgumentParser(formatter_class=MakeColorsHelpFormatter)

* **colorize() function** - Flexible colorization

  .. code-block:: python

      from make_colors import colorize
      
      print(colorize("Text", data="bold-red"))
      print(colorize("Text", fg="r", bg="y", attrs=["underline"]))

Improved
~~~~~~~~

* **Rich Markup Parser** - Enhanced ``parse_rich_markup()`` function

  - Support for multiple markup sections
  - Better attribute detection
  - Improved error handling

* **getSort() function** - Enhanced color parsing

  - Automatic attribute detection from strings
  - Support for multiple separators
  - Better fallback handling

* **Performance** - Optimized color rendering

  - Faster ANSI code generation
  - Reduced string allocations
  - Better caching for repeated colors

* **Documentation** - Comprehensive updates

  - New Table module documentation
  - Enhanced API reference
  - More examples and use cases
  - Sphinx documentation for Table module

Changed
~~~~~~~

* **API Enhancement** - ``make_colors()`` function now supports:

  - Attribute detection from color strings
  - Multiple separators (hyphen, underscore, comma)
  - Rich markup format with multiple tags

* **Color Detection** - Improved terminal color support detection

  - Better Windows 10+ detection
  - Enhanced ANSICON support
  - Improved TTY detection

Fixed
~~~~~

* **Rich Markup** - Fixed multiple tag parsing issues
* **Windows Console** - Improved ANSI mode detection on Windows
* **Color Abbreviations** - Better handling of edge cases
* **Memory Leaks** - Fixed potential memory issues in long-running applications

Version 1.5.0 (2024-XX-XX)
==========================

Rich Markup Support
-------------------

Added
~~~~~

* **Rich Markup Format** - Support for Rich-style markup

  .. code-block:: python

      print(make_colors("[red]Error[/] [bold white on blue]INFO[/]"))

* **Multiple Markup Tags** - Support multiple tags in single string

  .. code-block:: python

      print(make_colors("[cyan]Debug[/] [yellow]Warning[/] [red]Error[/]"))

* **Style Attributes in Markup** - Support attributes in Rich markup

  .. code-block:: python

      print(make_colors("[bold red]Bold Red[/]"))
      print(make_colors("[italic blue on white]Styled[/]"))

Version 1.4.0 (2024-XX-XX)
==========================

Enhanced Color Support
----------------------

Added
~~~~~

* **Light Color Variants** - Added light versions of all colors

  - ``lightred``, ``lightgreen``, ``lightblue``, etc.
  - Abbreviations: ``lr``, ``lg``, ``lb``, etc.

* **Color Abbreviations** - Short codes for quick usage

  ========== ============
  Color      Abbreviation
  ========== ============
  red        r, rd, re
  green      g, gr, ge
  blue       bl
  yellow     y, ye, yl
  magenta    m, mg, ma
  cyan       c, cy, cn
  white      w, wh, wi, wt
  black      b, bk
  ========== ============

* **Combined Format** - Separator notation support

  .. code-block:: python

      print(make_colors("Text", "red-yellow"))  # red on yellow
      print(make_colors("Text", "r_y"))         # same with abbreviations

Version 1.3.0 (2024-XX-XX)
==========================

Attributes Support
------------------

Added
~~~~~

* **Text Attributes** - Support for text styling

  - ``bold`` - Bold text
  - ``dim`` - Dimmed text
  - ``italic`` - Italic text
  - ``underline`` - Underlined text
  - ``blink`` - Blinking text
  - ``reverse`` - Reverse colors
  - ``strikethrough`` - Strikethrough text

  .. code-block:: python

      print(make_colors("Bold", "red", attrs=["bold"]))
      print(make_colors("Multiple", "blue", attrs=["bold", "underline"]))

Version 1.2.0 (2024-XX-XX)
==========================

Environment Control
-------------------

Added
~~~~~

* **Environment Variables** - Control colors via environment

  - ``MAKE_COLORS`` - Enable/disable colors (``0`` or ``1``)
  - ``MAKE_COLORS_FORCE`` - Force colors (``1`` or ``True``)
  - ``MAKE_COLORS_DEBUG`` - Enable debug mode (``1``, ``true``, ``True``)

* **Force Mode** - ``force`` parameter to force color output

  .. code-block:: python

      print(make_colors("Always colored", "red", force=True))

Version 1.1.0 (2024-XX-XX)
==========================

Cross-platform Support
----------------------

Added
~~~~~

* **Windows 10+ Support** - Native ANSI color support on Windows

  - Automatic console mode configuration
  - ANSI escape sequence processing

* **Platform Detection** - ``supports_color()`` method

  .. code-block:: python

      from make_colors import MakeColors
      
      if MakeColors.supports_color():
          print("Colors supported!")

Changed
~~~~~~~

* **Import Structure** - Reorganized module imports
* **Error Handling** - Better fallback for unsupported colors

Version 1.0.0 (2024-XX-XX)
==========================

Initial Release
---------------

Added
~~~~~

* **Basic Color Support** - 8 standard colors

  - black, red, green, yellow, blue, magenta, cyan, white

* **Background Colors** - Background color support with ``on_`` prefix

  .. code-block:: python

      print(make_colors("Text", "white", "on_red"))

* **Simple API** - Easy-to-use function interface

  .. code-block:: python

      print(make_colors("Colored text", "red"))

* **Color Fallback** - Graceful fallback for unsupported colors

Features
~~~~~~~~

* Cross-platform color support (Windows, Linux, macOS)
* Zero external dependencies
* Lightweight and fast
* Simple and intuitive API

Migration Guide
===============

From 1.x to 2.0
---------------

Table Module
~~~~~~~~~~~~

New feature, no breaking changes. To use tables:

.. code-block:: python

    # Old way - just colored text
    print(make_colors("Server: Running", "green"))
    
    # New way - structured tables
    from make_colors.table import Table
    
    table = Table()
    table.add_column("Server")
    table.add_column("Status", style="green")
    table.add_row("Web Server", "Running")
    print(table.draw())

Attribute Detection
~~~~~~~~~~~~~~~~~~~

Enhancement, no breaking changes. Old code still works:

.. code-block:: python

    # Old way - still works
    print(make_colors("Bold", "red", attrs=["bold"]))
    
    # New way - more convenient
    print(make_colors("Bold", "bold-red"))

Magic Functions
~~~~~~~~~~~~~~~

New feature, optional import:

.. code-block:: python

    # Import only what you need
    from make_colors import make_colors  # Basic
    
    # Or import magic functions
    from make_colors import *  # Includes red(), blue(), etc.

Deprecation Notices
===================

None
----

No features are deprecated in this release. All existing APIs remain stable and supported.

Future Plans
============

Planned for Version 2.1
------------------------

* **Table Templates** - Pre-defined table styles
* **Table Export** - Export tables to markdown, HTML, CSV
* **Color Themes** - Predefined color schemes
* **Gradient Support** - Gradient color effects
* **True Color Support** - 24-bit RGB colors
* **Image to ANSI** - Convert images to colored text

Planned for Version 3.0
------------------------

* **Async Support** - Async rendering for large tables
* **Streaming Tables** - Real-time table updates
* **Interactive Tables** - User-interactive tables
* **Chart Support** - ASCII charts and graphs

Contributing
============

Contributions are welcome! Please see `CONTRIBUTING.md` for guidelines.

When adding new features:

1. Add tests
2. Update documentation
3. Add changelog entry
4. Follow code style guidelines

License
=======

This project is licensed under the MIT License - see the LICENSE file for details.

See Also
========

* :doc:`installation` - Installation guide
* :doc:`quickstart` - Quick start guide
* :doc:`table` - Table module documentation
* :doc:`api/main_functions` - Complete API reference
* :doc:`examples` - Usage examples

.. note::
   For detailed migration guides and breaking changes, see the individual
   version sections above.

.. tip::
   Always check the changelog before upgrading to see what's new and
   what might affect your code.

.. warning::
   Major version changes (e.g., 1.x to 2.x) may include breaking changes.
   Always test your application after upgrading.