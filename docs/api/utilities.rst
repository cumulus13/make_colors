Utility Functions
=================

This section documents utility and helper functions in the make_colors module.

Color Mapping Functions
-----------------------

color_map()
~~~~~~~~~~~

.. py:function:: color_map(color)

   Map color abbreviations and short codes to full color names.

   This function expands common color abbreviations into their full names
   for use with the color banks. It provides convenient shortcuts for
   frequently used colors.

   :param str color: Color abbreviation or short code
   :return: Full color name corresponding to the abbreviation
   :rtype: str

   **Supported Abbreviations:**

   ============= ==============
   Abbreviation  Full Name
   ============= ==============
   b, bk         black
   bl            blue
   r, rd, re     red
   g, gr, ge     green
   y, ye, yl     yellow
   m, mg, ma     magenta
   c, cy, cn     cyan
   w, wh, wi, wt white
   lb            lightblue
   lr            lightred
   lg            lightgreen
   ly            lightyellow
   lm            lightmagenta
   lc            lightcyan
   lw            lightwhite
   lk            lightblack
   ============= ==============

   **Example:**

   .. code-block:: python

      from make_colors import color_map
      
      print(color_map("r"))      # Returns: "red"
      print(color_map("bl"))     # Returns: "blue"
      print(color_map("lg"))     # Returns: "lightgreen"
      print(color_map("xyz"))    # Returns: "lightwhite" (fallback)

   .. note::
      If an unrecognized abbreviation is provided, the function falls back 
      to "lightwhite" as the default color.

color_map_colors()
~~~~~~~~~~~~~~~~~~

.. py:function:: color_map_colors(color)

   Alternative implementation of color mapping (from colors.py module).

   This function provides the same functionality as :py:func:`color_map`
   but is implemented in the colors submodule.

   :param str color: Color abbreviation or short code
   :return: Full color name
   :rtype: str

   **Example:**

   .. code-block:: python

      from make_colors import color_map_colors
      
      print(color_map_colors("r"))   # Returns: "red"
      print(color_map_colors("lb"))  # Returns: "lightblue"

Parsing Functions
-----------------

getSort()
~~~~~~~~~

.. py:function:: getSort(data=None, foreground='', background='', attrs=[])

   Parse and sort color specifications and attributes from combined format strings.

   This function intelligently parses color strings that may contain foreground,
   background, and attribute specifications in various formats. It now also 
   detects text attributes (bold, italic, underline, etc.) from the input 
   strings and returns them as a separate list.

   :param str data: Combined color string with format "foreground-background" 
                    or "foreground_background" or "foreground,background" (optional)
   :param str foreground: Explicit foreground color specification (optional)
   :param str background: Explicit background color specification (optional)
   :param list attrs: Existing attributes list (optional)
   :return: Tuple of (foreground_color, background_color, attributes_list)
   :rtype: tuple[str, str|None, list]

   **Supported Formats:**

   - Single color: ``"red"``
   - Hyphen separator: ``"red-yellow"``
   - Underscore separator: ``"blue_white"``
   - Comma separator: ``"green,black"``
   - With attributes: ``"bold-red-yellow"``
   - Abbreviations: ``"r-y"``, ``"lb_b"``

   **Default Behavior:**

   - Foreground defaults to ``'white'`` if not specified
   - Background defaults to ``None`` if not specified
   - Attributes are extracted and returned as a list
   - Duplicate attributes are automatically removed

   **Example:**

   .. code-block:: python

      from make_colors import getSort
      
      # Simple format
      fg, bg, attrs = getSort("red-yellow")
      print(f"FG: {fg}, BG: {bg}, Attrs: {attrs}")
      # Output: FG: red, BG: yellow, Attrs: []
      
      # With attributes
      fg, bg, attrs = getSort("bold-red-yellow")
      print(f"FG: {fg}, BG: {bg}, Attrs: {attrs}")
      # Output: FG: red, BG: yellow, Attrs: ['bold']
      
      # Abbreviations
      fg, bg, attrs = getSort("r_b")
      print(f"FG: {fg}, BG: {bg}")
      # Output: FG: red, BG: black
      
      # Explicit parameters
      fg, bg, attrs = getSort(foreground="blue", background="white")
      print(f"FG: {fg}, BG: {bg}")
      # Output: FG: blue, BG: white
      
      # Mixed format
      fg, bg, attrs = getSort("italic-green", attrs=["bold"])
      print(f"FG: {fg}, BG: {bg}, Attrs: {attrs}")
      # Output: FG: green, BG: None, Attrs: ['bold', 'italic']

   .. note::
      This function is used internally by :py:func:`make_colors` to parse
      color specifications. You can use it directly for custom parsing needs.

translate()
~~~~~~~~~~~

.. py:function:: translate(*args, **kwargs)

   Alias function for :py:func:`getSort`.

   This function provides an alternative name for getSort() for better 
   semantic clarity in some contexts.

   :param args: Positional arguments passed to getSort
   :param kwargs: Keyword arguments passed to getSort
   :return: Same as getSort()
   :rtype: tuple[str, str|None, list]

   **Example:**

   .. code-block:: python

      from make_colors import translate
      
      fg, bg, attrs = translate("bold-red-yellow")
      print(f"FG: {fg}, BG: {bg}, Attrs: {attrs}")

parse_rich_markup()
~~~~~~~~~~~~~~~~~~~

.. py:function:: parse_rich_markup(text)

   Parse Rich console markup format and extract styling information.

   This function parses Rich-style markup tags and handles multiple markup 
   sections in a single string, converting each to proper format for ANSI 
   escape codes.

   :param str text: Text with Rich markup format
   :return: List of tuples (content, foreground, background, style)
   :rtype: list[tuple[str, str|None, str|None, str|None]]

   **Supported Markup:**

   - ``[red]text[/]`` - Single color
   - ``[white on red]text[/]`` - Foreground and background
   - ``[bold red]text[/]`` - Style with color
   - ``[bold white on red]text[/]`` - Style with colors

   **Example:**

   .. code-block:: python

      from make_colors import parse_rich_markup
      
      # Simple markup
      result = parse_rich_markup("[red]Error![/]")
      print(result)
      # Output: [('Error!', 'red', None, None)]
      
      # With background
      result = parse_rich_markup("[white on red]Alert![/]")
      print(result)
      # Output: [('Alert!', 'white', 'red', None)]
      
      # With style
      result = parse_rich_markup("[bold red]Important![/]")
      print(result)
      # Output: [('Important!', 'red', None, 'bold')]
      
      # Multiple sections
      text = "[red]Error:[/] [white]File not found[/]"
      result = parse_rich_markup(text)
      print(result)
      # Output: [('Error:', 'red', None, None), 
      #          ('File not found', 'white', None, None)]

   .. note::
      This function is used internally by :py:func:`make_colors` when
      Rich markup format is detected. The parsed results are then converted
      to ANSI escape codes.

Internal Functions
------------------

_make_ansi_func()
~~~~~~~~~~~~~~~~~

.. py:function:: _make_ansi_func(fg, bg=None, attrs=None)

   Internal function to create ANSI escape code formatter.

   This function generates a callable that applies ANSI escape codes to text.
   It's used internally to create dynamic color functions.

   :param str fg: Foreground color
   :param str bg: Background color (optional)
   :param list attrs: Text attributes (optional)
   :return: A function that applies the ANSI codes to text
   :rtype: callable

   .. warning::
      This is an internal function and should not be called directly.
      Use :py:func:`make_colors` or other public functions instead.

Helper Functions
----------------

Debug Output
~~~~~~~~~~~~

The module provides debug output when the ``MAKE_COLORS_DEBUG`` environment
variable is set. This is controlled internally but can be enabled:

.. code-block:: bash

   export MAKE_COLORS_DEBUG=1

Or in Python:

.. code-block:: python

   import os
   os.environ['MAKE_COLORS_DEBUG'] = '1'

When enabled, functions like :py:func:`getSort` will print detailed
parsing information to help troubleshoot color specifications.

Type Checking
~~~~~~~~~~~~~

The module uses type hints throughout. You can use type checkers like mypy:

.. code-block:: python

   from typing import Optional, List, Tuple
   
   def process_colors(
       fg: str,
       bg: Optional[str] = None,
       attrs: Optional[List[str]] = None
   ) -> Tuple[str, Optional[str], List[str]]:
       from make_colors import getSort
       return getSort(foreground=fg, background=bg, attrs=attrs or [])

Practical Examples
------------------

Creating a Color Validator
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from make_colors import getSort, color_map
   
   def validate_color_spec(color_string):
       """Validate and parse a color specification."""
       try:
           fg, bg, attrs = getSort(color_string)
           print(f"✓ Valid color spec:")
           print(f"  Foreground: {fg}")
           print(f"  Background: {bg or 'None'}")
           print(f"  Attributes: {attrs or 'None'}")
           return True
       except Exception as e:
           print(f"✗ Invalid color spec: {e}")
           return False
   
   # Test various formats
   validate_color_spec("red-yellow")
   validate_color_spec("bold-blue")
   validate_color_spec("r_w")
   validate_color_spec("italic-green-black")

Custom Color Parser
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from make_colors import parse_rich_markup, getSort
   
   def parse_custom_format(text):
       """
       Parse custom color format that supports both
       Rich markup and traditional format.
       """
       # Try Rich markup first
       if '[' in text and ']' in text and '[/' in text:
           return parse_rich_markup(text)
       
       # Fall back to traditional parsing
       parts = text.split('::')
       if len(parts) == 2:
           color_spec, content = parts
           fg, bg, attrs = getSort(color_spec)
           return [(content, fg, bg, attrs[0] if attrs else None)]
       
       return [(text, None, None, None)]
   
   # Usage
   result = parse_custom_format("[bold red]Error![/]")
   result = parse_custom_format("red-yellow::Warning message")

Color Abbreviation Expander
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from make_colors import color_map
   
   def expand_all_abbreviations(text):
       """Expand all color abbreviations in text."""
       import re
       
       # Common abbreviation pattern
       pattern = r'\b(r|g|bl|y|m|c|w|b|lb|lr|lg|ly|lm|lc|lw|lk)\b'
       
       def replace_abbr(match):
           abbr = match.group(1)
           full = color_map(abbr)
           return full
       
       return re.sub(pattern, replace_abbr, text)
   
   # Usage
   text = "Use r for red and lb for lightblue"
   expanded = expand_all_abbreviations(text)
   print(expanded)
   # Output: "Use red for red and lightblue for lightblue"

See Also
--------

- :doc:`main_functions` - Main function documentation
- :doc:`classes` - Classes API reference
- :doc:`constants` - Color codes and constants
- :doc:`../usage` - Complete usage guide
- :doc:`../examples` - Practical examples