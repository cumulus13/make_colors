Main Functions
==============

This section documents the primary functions for text colorization in make_colors.

make_colors()
-------------

.. py:function:: make_colors(string, foreground='white', background=None, attrs=[], force=False)

   Apply color formatting to text with comprehensive control options and Rich markup support.

   This is the main function for creating colored text output. It provides flexible color 
   specification, environment variable controls, Rich console markup parsing, and cross-platform 
   compatibility.

   :param str string: The text string to be colorized. Can include Rich markup format.
   :param str foreground: Foreground color specification (default: 'white')
   :param str background: Background color specification (default: None)
   :param list attrs: List of text attributes (default: [])
   :param bool force: Force color output even if environment doesn't support it (default: False)
   :return: The colorized string with ANSI escape codes
   :rtype: str

   **Foreground Colors:**
   
   Full names:
      - ``black``, ``red``, ``green``, ``yellow``, ``blue``, ``magenta``, ``cyan``, ``white``
      - ``lightblack``, ``lightred``, ``lightgreen``, ``lightyellow``, ``lightblue``, 
        ``lightmagenta``, ``lightcyan``, ``lightwhite``
   
   Abbreviations:
      - ``b``/``bk`` → black, ``r``/``rd``/``re`` → red
      - ``g``/``gr``/``ge`` → green, ``y``/``ye``/``yl`` → yellow
      - ``bl`` → blue, ``m``/``mg``/``ma`` → magenta
      - ``c``/``cy``/``cn`` → cyan, ``w``/``wh`` → white
      - ``lb``, ``lr``, ``lg``, ``ly``, ``lm``, ``lc``, ``lw``, ``lk`` → light variants

   **Background Colors:**
   
   Same as foreground colors, with optional ``on_`` prefix:
      - ``on_black``, ``on_red``, ``on_yellow``, etc.
      - Or use color name directly: ``black``, ``red``, ``yellow``

   **Text Attributes:**
   
   - ``bold`` - Bold/bright text
   - ``dim`` - Dimmed text
   - ``italic`` - Italic text (terminal dependent)
   - ``underline`` - Underlined text
   - ``blink`` - Blinking text
   - ``reverse`` - Reverse video
   - ``strikethrough``/``strike`` - Strikethrough text

   **Combined Format:**
   
   You can specify colors and attributes in a single string using separators:
      - Hyphen: ``"red-yellow"`` (red on yellow)
      - Underscore: ``"blue_white"`` (blue on white)
      - Comma: ``"green,black"`` (green on black)
      - With attributes: ``"bold-red-yellow"`` (bold red on yellow)

   **Rich Markup Format:**
   
   Supports Rich console markup:
      - ``"[red]text[/]"`` - Single color
      - ``"[white on red]text[/]"`` - Foreground and background
      - ``"[bold red]text[/]"`` - Style with color
      - ``"[bold white on red]text[/]"`` - Style with colors

   **Environment Variables:**
   
   - ``MAKE_COLORS=0`` - Disable all coloring
   - ``MAKE_COLORS=1`` - Enable coloring
   - ``MAKE_COLORS_FORCE=1`` - Force coloring regardless of terminal support
   - ``MAKE_COLORS_DEBUG=1`` - Enable debug output

   **Examples:**

   Basic usage:

   .. code-block:: python

      from make_colors import make_colors
      
      # Simple colored text
      print(make_colors("Error!", "red"))
      print(make_colors("Success!", "green"))
      print(make_colors("Info", "blue"))

   With background:

   .. code-block:: python

      # Using 'on_' prefix
      print(make_colors("Warning!", "yellow", "on_black"))
      print(make_colors("Critical!", "white", "on_red"))
      
      # Without 'on_' prefix
      print(make_colors("Alert!", "black", "yellow"))

   Using abbreviations:

   .. code-block:: python

      print(make_colors("Quick red", "r"))
      print(make_colors("Light blue", "lb"))
      print(make_colors("Red on white", "r", "w"))

   Combined format with attributes:

   .. code-block:: python

      # New attribute detection feature
      print(make_colors("Bold red", "bold-red"))
      print(make_colors("Italic blue", "italic-blue"))
      print(make_colors("Bold white on red", "bold-white-red"))
      print(make_colors("Underline green", "underline_green"))

   Rich markup format:

   .. code-block:: python

      # Basic rich markup
      print(make_colors("[red]Error![/]"))
      print(make_colors("[white on red]Critical![/]"))
      
      # With styles
      print(make_colors("[bold red]Important![/]"))
      print(make_colors("[italic blue]Note[/]"))
      
      # Multiple sections
      log = "[bold red][ERROR][/] [white]Connection failed[/]"
      print(make_colors(log))

   Force mode:

   .. code-block:: python

      # Always apply colors (useful for file output)
      with open("log.txt", "w") as f:
          colored = make_colors("Log entry", "blue", force=True)
          f.write(colored)

   .. note::
      The function automatically detects terminal color support. Use ``force=True`` to 
      bypass detection, useful for file output or non-interactive scenarios.

   .. warning::
      Some attributes like ``italic`` and ``blink`` may not be supported by all terminals.

make_color()
------------

.. py:function:: make_color(string, foreground='white', background=None, attrs=[], force=False)

   Alias function for :py:func:`make_colors` with identical functionality.

   This function provides an alternative name for ``make_colors()`` to accommodate
   different naming preferences. All parameters and behavior are identical.

   :param str string: The text string to be colorized
   :param str foreground: Foreground color specification (default: 'white')
   :param str background: Background color specification (default: None)
   :param list attrs: List of text attributes (default: [])
   :param bool force: Force color output (default: False)
   :return: The colorized string
   :rtype: str

   **Example:**

   .. code-block:: python

      from make_colors import make_color
      
      # These calls are equivalent:
      text1 = make_color("Hello", "red")
      text2 = make_colors("Hello", "red")

make()
------

.. py:function:: make(string, foreground='white', background=None, attrs=[], force=False)

   Short alias for :py:func:`make_colors` function.

   Provides the shortest possible function name for quick usage while maintaining
   full functionality.

   :param str string: The text string to be colorized
   :param str foreground: Foreground color specification (default: 'white')
   :param str background: Background color specification (default: None)
   :param list attrs: List of text attributes (default: [])
   :param bool force: Force color output (default: False)
   :return: The colorized string
   :rtype: str

   **Example:**

   .. code-block:: python

      from make_colors import make
      
      # Shortest way to colorize text
      text = make("Hello", "bold-red")
      print(text)

print()
-------

.. py:function:: print(string, foreground='white', background=None, attrs=[], force=False)

   Print colored text directly to the console with automatic formatting.

   This convenience function combines color formatting and printing in a single call.
   It applies the :py:func:`make_colors` function and immediately outputs the result 
   to stdout.

   :param str string: The text string to be printed with colors
   :param str foreground: Foreground color specification (default: 'white')
   :param str background: Background color specification (default: None)
   :param list attrs: List of text attributes (default: [])
   :param bool force: Force color output (default: False)
   :return: None

   .. note::
      This function overrides Python's built-in ``print()`` function within the make_colors
      module scope. The original print function is preserved as ``_print`` for internal use.

   **Examples:**

   .. code-block:: python

      from make_colors import print
      
      # Direct colored printing
      print("Success!", "green")
      print("Warning!", "yellow", "on_black")
      print("Error!", "red", "on_white")
      
      # Using abbreviations
      print("Info", "lb")  # Light blue
      print("Debug", "c", "b")  # Cyan on black
      
      # With attribute detection
      print("Bold text", "bold-red")
      print("Italic text", "italic-blue")
      
      # Rich markup
      print("[bold red]Critical Error![/]")

colorize()
----------

.. py:function:: colorize(text, data=None, fg='', bg='', attrs=None)

   Alternative colorization function with flexible parameter parsing.

   This function provides an alternative interface with automatic parsing of color
   specifications from the ``data`` parameter or individual ``fg``/``bg`` parameters.

   :param str text: The text string to colorize
   :param str data: Combined color specification string (optional)
   :param str fg: Foreground color (optional)
   :param str bg: Background color (optional)
   :param list attrs: List of text attributes (default: None)
   :return: The colorized string
   :rtype: str

   **Examples:**

   .. code-block:: python

      from make_colors import colorize
      
      # Using data parameter
      print(colorize("Text", "red-yellow"))
      print(colorize("Text", "bold-blue"))
      
      # Using fg/bg parameters
      print(colorize("Text", fg="red", bg="yellow"))
      print(colorize("Text", fg="blue", attrs=["bold"]))
      
      # Mixed approach
      print(colorize("Text", data="red", attrs=["underline"]))

print_exception()
-----------------

.. py:function:: print_exception(*args, **kwargs)

   Print exception information with color-coded formatting.

   This function automatically formats and colorizes Python exception tracebacks,
   making error output more readable and visually distinct.

   :param kwargs: Keyword arguments for color customization:
                  
                  - ``tb_color`` (str): Traceback color (default: "lc" - light cyan)
                  - ``tp_color`` (str): Exception type color (default: "y" - yellow)
                  - ``tv_color`` (str): Exception value color (default: "white-red-blink")
   
   :return: Tuple of (exception_type, exception_value, traceback)
   :rtype: tuple

   **Example:**

   .. code-block:: python

      from make_colors import print_exception
      
      try:
          result = 10 / 0
      except:
          print_exception()  # Prints colored exception info
      
      # Custom colors
      try:
          undefined_variable
      except:
          print_exception(
              tb_color="lightblue",
              tp_color="lightred",
              tv_color="bold-white-red"
          )

   .. note::
      This function must be called within an exception handler context (inside an
      ``except`` block) to have access to exception information.

Dynamic Color Functions
-----------------------

make_colors also generates dynamic functions for direct color access:

**Foreground Colors:**

.. code-block:: python

   from make_colors import red, green, blue, yellow
   from make_colors import lightred, lightgreen, lightblue
   
   print(red("Error message"))
   print(green("Success"))
   print(lightblue("Information"))

**Combined Colors:**

.. code-block:: python

   from make_colors import red_on_yellow, white_on_blue
   from make_colors import green_on_black
   
   print(red_on_yellow("Warning!"))
   print(white_on_blue("Information"))

**Abbreviated Functions:**

.. code-block:: python

   from make_colors import r, g, bl, lb
   from make_colors import w_bl, r_y, g_b
   
   print(r("Red text"))
   print(lb("Light blue"))
   print(w_bl("White on blue"))

See Also
--------

- :doc:`classes` - MakeColors class documentation
- :doc:`utilities` - Utility functions
- :doc:`../usage` - Comprehensive usage guide
- :doc:`../examples` - Practical examples