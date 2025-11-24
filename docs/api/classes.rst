Classes API Reference
=====================

This section documents all classes available in the make_colors module.

MakeColors
----------

.. py:class:: MakeColors()

   A comprehensive class that provides methods for generating colored text output 
   in Windows 10+, Linux, and macOS terminals with support for both ANSI and rich formatting.

   This class handles cross-platform color support, including Windows console configuration,
   ANSI escape codes, and rich text formatting options.

   **Class Methods:**

   .. py:classmethod:: supports_color()

      Check if the current terminal/console supports colored text output.

      This method performs comprehensive checks including:
      
      - Platform compatibility (excludes Pocket PC)
      - TTY detection for proper terminal output
      - Windows console mode verification
      - ANSICON environment variable detection

      :return: True if the system supports colored output, False otherwise
      :rtype: bool

      **Example:**

      .. code-block:: python

         from make_colors import MakeColors
         
         if MakeColors.supports_color():
             print("Terminal supports colors!")
         else:
             print("Plain text mode only")

   **Instance Methods:**

   .. py:method:: colored(string, foreground, background=None, attrs=[])

      Colorize a string using ANSI escape codes for terminal output.

      :param str string: The text string to colorize
      :param str foreground: Foreground color name or code
      :param str background: Background color name with optional ``on_`` prefix (optional)
      :param list attrs: List of text attributes (optional)
      :return: The input string wrapped with ANSI escape codes
      :rtype: str

      **Example:**

      .. code-block:: python

         mc = MakeColors()
         
         # Basic usage
         red_text = mc.colored("Error!", "red")
         print(red_text)
         
         # With background
         warning = mc.colored("Warning!", "yellow", "on_black")
         print(warning)
         
         # With attributes
         bold_error = mc.colored("Critical!", "red", "on_white", ["bold"])
         print(bold_error)

   .. py:method:: rich_colored(string, color=None, bg_color=None, style=None)

      Generate rich formatted text with enhanced styling options.

      :param str string: The text string to format
      :param str color: Text color name (optional)
      :param str bg_color: Background color name (optional)
      :param str style: Text style modifier (optional)
      :return: Formatted string with rich console styling applied
      :rtype: str

      **Style Options:**
      
      - ``"bold"`` - Bold text
      - ``"italic"`` - Italic text
      - ``"underline"`` - Underlined text
      - ``"dim"`` - Dimmed text

      **Example:**

      .. code-block:: python

         mc = MakeColors()
         
         # Bold red text
         bold_red = mc.rich_colored("ERROR", color="red", style="bold")
         print(bold_red)
         
         # Underlined blue text
         underlined = mc.rich_colored("Link", color="blue", style="underline")
         print(underlined)
         
         # Highlighted text
         highlighted = mc.rich_colored("Important", color="black", bg_color="yellow")
         print(highlighted)

MakeColor
---------

.. py:class:: MakeColor()

   Alias class for :py:class:`MakeColors` to provide alternative naming.

   This class is identical to MakeColors and exists purely for naming preference 
   and backward compatibility.

   **Example:**

   .. code-block:: python

      from make_colors import MakeColor
      
      mc = MakeColor()  # Same as MakeColors()
      text = mc.colored("Hello", "red")
      print(text)

Color
-----

.. py:class:: Color(foreground, background=None)

   A class for creating reusable color formatters.

   This class creates a color formatter instance that can be reused to apply 
   the same color scheme to multiple strings.

   :param str foreground: Foreground color name
   :param str background: Background color name (optional)

   **Attributes:**

   .. py:attribute:: COLOR

      The ANSI escape sequence string for this color combination.

      :type: str

   **Methods:**

   .. py:method:: format(text)

      Format text with the configured colors.

      :param str text: Text to format
      :return: Formatted text with colors applied
      :rtype: str

   .. py:method:: __call__(text)

      Allow the instance to be called as a function.

      :param str text: Text to format
      :return: Formatted text with colors applied
      :rtype: str

   .. py:method:: __str__()

      Return the ANSI escape sequence.

      :return: ANSI color code string
      :rtype: str

   .. py:method:: convert(foreground, background=None)

      Convert color names to ANSI escape sequence.

      :param str foreground: Foreground color name
      :param str background: Background color name (optional)
      :return: ANSI escape sequence
      :rtype: str

   **Example:**

   .. code-block:: python

      from make_colors import Color
      
      # Create a color instance
      error_color = Color("red", "yellow")
      
      # Use format method
      text1 = error_color.format("Error occurred!")
      print(text1)
      
      # Use as callable
      text2 = error_color("Another error!")
      print(text2)
      
      # Get ANSI code
      print(error_color.COLOR)  # Returns: "\033[43;31m"
      
      # Convert to string
      print(str(error_color))   # Returns: "\033[43;31m"
      
      # Reuse for multiple strings
      for msg in ["Error 1", "Error 2", "Error 3"]:
          print(error_color(msg))

Colors
------

.. py:class:: Colors(foreground, background=None)

   Alias class for :py:class:`Color`.

   This class is identical to Color and exists for naming flexibility.

   **Example:**

   .. code-block:: python

      from make_colors import Colors
      
      success = Colors("green")
      print(success("Operation completed!"))

Console
-------

.. py:class:: Console()

   A utility class for direct console printing with colors.

   This class provides static methods for printing colored text directly 
   to the console without needing to store formatted strings.

   **Class Methods:**

   .. py:classmethod:: print(string, foreground='white', background=None, attrs=[], force=False)

      Print colored text directly to the console.

      :param str string: Text to print
      :param str foreground: Foreground color (default: 'white')
      :param str background: Background color (default: None)
      :param list attrs: Text attributes (default: [])
      :param bool force: Force color output (default: False)
      :return: None

      **Example:**

      .. code-block:: python

         from make_colors import Console
         
         # Direct colored printing
         Console.print("Success!", "green")
         Console.print("Warning!", "yellow", "on_black")
         Console.print("Error!", "red", "on_white", ["bold"])
         
         # With attribute detection
         Console.print("Bold red text", "bold-red")
         Console.print("Italic blue", "italic-blue")
         
         # Rich markup
         Console.print("[bold green]Success![/]")

         # class based
         console = Console()
         console.print("Success!", "green")
         console.print("Warning!", "yellow", "on_black")
         console.print("Error!", "red", "on_white", ["bold"])

         console.print("Bold red text", "bold-red")
         console.print("Italic blue", "italic-blue")

         console.print("[bold green]Success![/]")
         

MakeColorsHelpFormatter
-----------------------

.. py:class:: MakeColorsHelpFormatter(prog, epilog=None, width=None, max_help_position=24, indent_increment=2)

   A custom ArgumentParser HelpFormatter with colored output.

   This formatter extends ``argparse.RawDescriptionHelpFormatter`` to provide
   colored help text for command-line applications.

   :param str prog: Program name
   :param str epilog: Epilog text (optional)
   :param int width: Maximum width (optional)
   :param int max_help_position: Maximum help position (default: 24)
   :param int indent_increment: Indent increment (default: 2)

   **Attributes:**

   .. py:attribute:: styles

      Dictionary mapping style keys to color names.

      :type: ClassVar[dict[str, str]]

      Default styles:
      
      - ``"args"`` - "lightyellow" (for option strings)
      - ``"groups"`` - "lightmagenta" (for section headers)
      - ``"help"`` - "lightcyan" (for help text)
      - ``"metavar"`` - "lightcyan" (for metavar placeholders)
      - ``"syntax"`` - "yellow" (for syntax elements)
      - ``"text"`` - "magenta" (for regular text)
      - ``"prog"`` - "lightcyan" (for program name)
      - ``"default"`` - "green" (for default values)

   **Methods:**

   .. py:method:: format_help()

      Format the help message with colors.

      :return: Colored help text
      :rtype: str

   **Example:**

   .. code-block:: python

      import argparse
      from make_colors import MakeColorsHelpFormatter
      
      # Create parser with colored help
      parser = argparse.ArgumentParser(
          prog='myapp',
          formatter_class=MakeColorsHelpFormatter,
          description='My awesome application'
      )
      
      parser.add_argument('-v', '--verbose', 
                         help='Enable verbose output',
                         action='store_true')
      parser.add_argument('-o', '--output',
                         help='Output file path',
                         metavar='FILE')
      
      # Print colored help
      parser.print_help()

SimpleCustomHelpFormatter
-------------------------

.. py:class:: SimpleCustomHelpFormatter(prog, **kwargs)

   A simpler custom HelpFormatter with basic coloring.

   This formatter provides basic colorization without the extensive styling
   of MakeColorsHelpFormatter. Good for minimalist applications.

   :param str prog: Program name
   :param kwargs: Additional keyword arguments

   **Example:**

   .. code-block:: python

      import argparse
      from make_colors import SimpleCustomHelpFormatter
      
      parser = argparse.ArgumentParser(
          prog='simple',
          formatter_class=SimpleCustomHelpFormatter
      )
      
      parser.add_argument('--config', help='Configuration file')
      parser.print_help()

Exception Classes
-----------------

MakeColorsError
~~~~~~~~~~~~~~~

.. py:exception:: MakeColorsError(color)

   Custom exception class for MakeColors-related errors.

   This exception is raised when invalid color specifications or
   unsupported operations are attempted.

   :param str color: The color name that caused the error

   **Example:**

   .. code-block:: python

      from make_colors import MakeColorsError
      
      try:
          # Some operation that fails
          raise MakeColorsError("invalidcolor")
      except MakeColorsError as e:
          print(f"Color error: {e}")

MakeColorsWarning
~~~~~~~~~~~~~~~~~

.. py:exception:: MakeColorsWarning(color)

   Custom warning class for MakeColors-related warnings.

   This warning is issued for non-critical issues like unrecognized
   color names that fall back to defaults.

   :param str color: The color name that triggered the warning

   **Example:**

   .. code-block:: python

      import warnings
      from make_colors import MakeColorsWarning
      
      warnings.warn(MakeColorsWarning("unknowncolor"))

Usage Examples
--------------

Combining Multiple Classes
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from make_colors import MakeColors, Color, Console
   
   # Check support
   if MakeColors.supports_color():
       print("Colors supported!")
   
   # Create reusable colors
   error = Color("red", "white")
   success = Color("green")
   
   # Use instance methods
   mc = MakeColors()
   warning = mc.colored("Warning!", "yellow", "on_black")
   
   # Direct console output
   Console.print("Information", "blue")
   
   # Apply reusable colors
   print(error("Critical error!"))
   print(success("Operation completed!"))

Creating Custom Color Schemes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from make_colors import Color
   
   # Define color scheme
   class ColorScheme:
       ERROR = Color("red", "white")
       WARNING = Color("yellow", "black")
       SUCCESS = Color("green")
       INFO = Color("blue")
       DEBUG = Color("cyan")
   
   # Use throughout application
   print(ColorScheme.ERROR("Error occurred!"))
   print(ColorScheme.WARNING("Warning: Check configuration"))
   print(ColorScheme.SUCCESS("All tests passed!"))
   print(ColorScheme.INFO("Server started on port 8000"))
   print(ColorScheme.DEBUG("Variable x = 42"))

See Also
--------

- :doc:`main_functions` - Main function documentation
- :doc:`utilities` - Utility functions
- :doc:`constants` - Constants and color codes
- :doc:`../usage` - Complete usage guide