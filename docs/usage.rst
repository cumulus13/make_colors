Complete Usage Guide
====================

This comprehensive guide covers all features and usage patterns of make_colors.

Basic Usage
-----------

Importing
~~~~~~~~~

.. code-block:: python

   # Import main function
   from make_colors import make_colors
   
   # Import convenience functions
   from make_colors import make, print
   
   # Import utility functions
   from make_colors import colorize, Color
   
   # Import classes
   from make_colors import MakeColors, Console

Simple Text Coloring
~~~~~~~~~~~~~~~~~~~~~

The most basic usage applies a single color:

.. code-block:: python

   from make_colors import make_colors
   
   # Red text
   red_text = make_colors("Error occurred!", "red")
   print(red_text)
   
   # Green text
   green_text = make_colors("Success!", "green")
   print(green_text)
   
   # Blue text
   blue_text = make_colors("Information", "blue")
   print(blue_text)

Color Specifications
--------------------

Full Color Names
~~~~~~~~~~~~~~~~

Use complete color names for clarity:

.. code-block:: python

   # Standard colors
   print(make_colors("Text", "black"))
   print(make_colors("Text", "red"))
   print(make_colors("Text", "green"))
   print(make_colors("Text", "yellow"))
   print(make_colors("Text", "blue"))
   print(make_colors("Text", "magenta"))
   print(make_colors("Text", "cyan"))
   print(make_colors("Text", "white"))
   
   # Light colors
   print(make_colors("Text", "lightred"))
   print(make_colors("Text", "lightgreen"))
   print(make_colors("Text", "lightblue"))
   print(make_colors("Text", "lightyellow"))
   print(make_colors("Text", "lightmagenta"))
   print(make_colors("Text", "lightcyan"))
   print(make_colors("Text", "lightwhite"))
   print(make_colors("Text", "lightblack"))  # or lightgrey

Color Abbreviations
~~~~~~~~~~~~~~~~~~~

Use short codes for quick development:

.. code-block:: python

   # Basic abbreviations
   print(make_colors("Text", "r"))     # red
   print(make_colors("Text", "g"))     # green
   print(make_colors("Text", "bl"))    # blue
   print(make_colors("Text", "y"))     # yellow
   print(make_colors("Text", "m"))     # magenta
   print(make_colors("Text", "c"))     # cyan
   print(make_colors("Text", "w"))     # white
   print(make_colors("Text", "b"))     # black
   
   # Light color abbreviations
   print(make_colors("Text", "lr"))    # lightred
   print(make_colors("Text", "lg"))    # lightgreen
   print(make_colors("Text", "lb"))    # lightblue
   print(make_colors("Text", "ly"))    # lightyellow
   print(make_colors("Text", "lm"))    # lightmagenta
   print(make_colors("Text", "lc"))    # lightcyan
   print(make_colors("Text", "lw"))    # lightwhite
   print(make_colors("Text", "lk"))    # lightblack

Complete Abbreviation Reference:

========== ============= ===================
Abbrev     Full Name     Alternative
========== ============= ===================
b, bk      black       
r, rd, re  red         
g, gr, ge  green       
y, ye, yl  yellow      
bl         blue        
m, mg, ma  magenta     
c, cy, cn  cyan        
w, wh      white         wi, wt
lb         lightblue   
lr         lightred    
lg         lightgreen  
ly         lightyellow 
lm         lightmagenta
lc         lightcyan   
lw         lightwhite  
lk         lightblack    lightgrey
========== ============= ===================

Background Colors
-----------------

Using ``on_`` Prefix
~~~~~~~~~~~~~~~~~~~~~

The most explicit way to specify backgrounds:

.. code-block:: python

   print(make_colors("Text", "red", "on_yellow"))
   print(make_colors("Text", "white", "on_blue"))
   print(make_colors("Text", "black", "on_white"))
   print(make_colors("Text", "green", "on_black"))

Without ``on_`` Prefix
~~~~~~~~~~~~~~~~~~~~~~~

Background can be specified directly:

.. code-block:: python

   print(make_colors("Text", "red", "yellow"))
   print(make_colors("Text", "white", "blue"))
   print(make_colors("Text", "black", "white"))

Combined Format
~~~~~~~~~~~~~~~

Specify both in one string:

.. code-block:: python

   # Using hyphen
   print(make_colors("Text", "red-yellow"))
   print(make_colors("Text", "white-blue"))
   
   # Using underscore
   print(make_colors("Text", "red_yellow"))
   print(make_colors("Text", "white_blue"))
   
   # Using comma
   print(make_colors("Text", "red,yellow"))
   print(make_colors("Text", "white,blue"))
   
   # With abbreviations
   print(make_colors("Text", "r-y"))    # red on yellow
   print(make_colors("Text", "w_bl"))   # white on blue
   print(make_colors("Text", "g,b"))    # green on black

Text Attributes
---------------

Basic Attributes
~~~~~~~~~~~~~~~~

Apply text styling:

.. code-block:: python

   # Bold text
   print(make_colors("Bold", "red", attrs=["bold"]))
   
   # Italic text
   print(make_colors("Italic", "blue", attrs=["italic"]))
   
   # Underlined text
   print(make_colors("Underline", "green", attrs=["underline"]))
   
   # Dimmed text
   print(make_colors("Dim", "white", attrs=["dim"]))
   
   # Strikethrough text
   print(make_colors("Strike", "red", attrs=["strikethrough"]))
   
   # Blinking text (if supported)
   print(make_colors("Blink", "yellow", attrs=["blink"]))
   
   # Reverse video
   print(make_colors("Reverse", "white", attrs=["reverse"]))

Multiple Attributes
~~~~~~~~~~~~~~~~~~~

Combine multiple attributes:

.. code-block:: python

   # Bold and underlined
   print(make_colors("Text", "red", attrs=["bold", "underline"]))
   
   # Italic and dim
   print(make_colors("Text", "blue", attrs=["italic", "dim"]))
   
   # Bold, italic, and underlined
   print(make_colors("Text", "green", attrs=["bold", "italic", "underline"]))

Attribute Detection (NEW!)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Include attributes directly in color strings:

.. code-block:: python

   # Simple attribute detection
   print(make_colors("Bold red", "bold-red"))
   print(make_colors("Italic blue", "italic-blue"))
   print(make_colors("Underline green", "underline-green"))
   
   # With background
   print(make_colors("Bold white on red", "bold-white-red"))
   print(make_colors("Italic blue on yellow", "italic-blue-yellow"))
   
   # Multiple attributes
   print(make_colors("Text", "bold-italic-red"))
   print(make_colors("Text", "underline-dim-green"))
   print(make_colors("Text", "bold-underline-italic-yellow"))
   
   # Any separator works
   print(make_colors("Text", "bold_red"))
   print(make_colors("Text", "italic,blue"))
   
   # Order doesn't matter
   print(make_colors("Text", "red-bold"))      # Same as bold-red
   print(make_colors("Text", "yellow-bold-italic"))  # Same as bold-italic-yellow

Supported Attributes:

============== =============================================
Attribute      Description
============== =============================================
bold           Bold or increased intensity
dim            Dimmed or decreased intensity
italic         Italic text (terminal dependent)
underline      Underlined text
blink          Blinking text (rarely supported)
reverse        Swap foreground and background colors
strikethrough  Strikethrough text
strike         Alias for strikethrough
============== =============================================

Rich Markup Format
------------------

Basic Markup
~~~~~~~~~~~~

Use intuitive markup tags:

.. code-block:: python

   # Single color
   print(make_colors("[red]Error message[/]"))
   print(make_colors("[green]Success message[/]"))
   
   # Color combination
   print(make_colors("[white on red]Alert![/]"))
   print(make_colors("[black on yellow]Warning![/]"))
   
   # With styles
   print(make_colors("[bold red]Important![/]"))
   print(make_colors("[italic blue]Note[/]"))
   print(make_colors("[underline green]Link[/]"))

Multiple Sections
~~~~~~~~~~~~~~~~~

Combine multiple markup sections:

.. code-block:: python

   # Log entry
   log = "[bold blue][INFO][/] [white]User logged in[/]"
   print(make_colors(log))
   
   # Error message
   error = "[bold red][ERROR][/] [lightred]Connection failed:[/] [cyan]timeout[/]"
   print(make_colors(error))
   
   # Complex message
   msg = (
       "[bold white on blue][SYSTEM][/] "
       "[cyan]2024-01-15 10:30:45[/] "
       "[green]Process completed[/]"
   )
   print(make_colors(msg))

See :doc:`rich_markup` for complete Rich markup documentation.

Function Variants
-----------------

make_colors()
~~~~~~~~~~~~~

The main function:

.. code-block:: python

   from make_colors import make_colors
   
   text = make_colors("Hello", "red", "on_yellow")
   print(text)

make_color()
~~~~~~~~~~~~

Alias for make_colors():

.. code-block:: python

   from make_colors import make_color
   
   text = make_color("Hello", "red", "on_yellow")
   print(text)

make()
~~~~~~

Short form:

.. code-block:: python

   from make_colors import make
   
   text = make("Hello", "red", "on_yellow")
   print(text)

print()
~~~~~~~

Direct printing:

.. code-block:: python

   from make_colors import print
   
   print("Hello", "red", "on_yellow")
   # No need to store in variable

colorize()
~~~~~~~~~~

Alternative interface:

.. code-block:: python

   from make_colors import colorize
   
   # Using data parameter
   print(colorize("Hello", "red-yellow"))
   
   # Using fg/bg parameters
   print(colorize("Hello", fg="red", bg="yellow"))
   
   # With attributes
   print(colorize("Hello", fg="red", attrs=["bold"]))

Dynamic Functions
-----------------

Foreground Only
~~~~~~~~~~~~~~~

.. code-block:: python

   from make_colors import red, green, blue, yellow
   from make_colors import lightred, lightgreen, lightblue
   
   print(red("Error message"))
   print(green("Success"))
   print(blue("Information"))
   print(yellow("Warning"))
   print(lightred("Light red text"))

Combinations
~~~~~~~~~~~~

.. code-block:: python

   from make_colors import red_on_yellow, white_on_blue
   from make_colors import green_on_black, black_on_white
   
   print(red_on_yellow("Warning!"))
   print(white_on_blue("Information"))
   print(green_on_black("Success"))

Abbreviated Functions
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from make_colors import r, g, bl, y
   from make_colors import w_bl, r_y, g_b
   
   print(r("Red"))
   print(g("Green"))
   print(bl("Blue"))
   print(w_bl("White on blue"))
   print(r_y("Red on yellow"))

Classes
-------

MakeColors Class
~~~~~~~~~~~~~~~~

.. code-block:: python

   from make_colors import MakeColors
   
   mc = MakeColors()
   
   # Check color support
   if mc.supports_color():
       print("Terminal supports colors")
   
   # Use colored method
   text = mc.colored("Hello", "red", "on_yellow")
   print(text)
   
   # Rich colored method
   text = mc.rich_colored("Hello", "red", "yellow", "bold")
   print(text)

Color Class
~~~~~~~~~~~

.. code-block:: python

   from make_colors import Color
   
   # Create color instance
   red_color = Color("red", "yellow")
   
   # Format text
   text = red_color.format("Hello World")
   print(text)
   
   # Or call directly
   text = red_color("Hello World")
   print(text)
   
   # Get ANSI code
   print(red_color.COLOR)  # Returns ANSI escape sequence

Console Class
~~~~~~~~~~~~~

.. code-block:: python

   from make_colors import Console
   
   # Direct printing
   Console.print("Success!", "green")
   Console.print("Error!", "red", "on_white")
   Console.print("Warning!", "yellow", "on_black", ["bold"])

Environment Variables
---------------------

MAKE_COLORS
~~~~~~~~~~~

Control color output globally:

.. code-block:: bash

   # Disable colors
   export MAKE_COLORS=0
   
   # Enable colors (default)
   export MAKE_COLORS=1

.. code-block:: python

   import os
   
   # Disable colors in Python
   os.environ['MAKE_COLORS'] = '0'
   
   # Now all colors are disabled
   print(make_colors("Text", "red"))  # Returns plain text

MAKE_COLORS_FORCE
~~~~~~~~~~~~~~~~~

Force color output:

.. code-block:: bash

   # Force colors even in non-TTY
   export MAKE_COLORS_FORCE=1

.. code-block:: python

   # Or use force parameter
   text = make_colors("Text", "red", force=True)
   
   # Useful for file output
   with open("log.txt", "w") as f:
       f.write(make_colors("Log entry", "blue", force=True))

MAKE_COLORS_DEBUG
~~~~~~~~~~~~~~~~~

Enable debug output:

.. code-block:: bash

   export MAKE_COLORS_DEBUG=1

.. code-block:: python

   # Debug mode shows parsing details
   import os
   os.environ['MAKE_COLORS_DEBUG'] = '1'
   
   print(make_colors("Text", "bold-red-yellow"))
   # Shows: parsing details, detected attributes, etc.

Advanced Patterns
-----------------

Conditional Coloring
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   def status_color(code):
       if code == 200:
           return make_colors(f"Status: {code}", "green")
       elif code == 404:
           return make_colors(f"Status: {code}", "yellow")
       else:
           return make_colors(f"Status: {code}", "red")
   
   print(status_color(200))
   print(status_color(404))
   print(status_color(500))

Color Mapping
~~~~~~~~~~~~~

.. code-block:: python

   SEVERITY_COLORS = {
       'debug': 'cyan',
       'info': 'blue',
       'warning': 'yellow',
       'error': 'red',
       'critical': 'white-red'
   }
   
   def log(severity, message):
       color = SEVERITY_COLORS.get(severity, 'white')
       print(make_colors(f"[{severity.upper()}] {message}", color))
   
   log('debug', 'Variable x = 42')
   log('info', 'Server started')
   log('error', 'Connection failed')

Template Formatting
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   LOG_TEMPLATE = "[{level_color}][{level}][/] [{time_color}]{time}[/] {message}"
   
   def format_log(level, time, message):
       colors = {
           'DEBUG': ('cyan', 'lightblack'),
           'INFO': ('blue', 'lightblue'),
           'ERROR': ('red', 'lightred'),
       }
       
       level_color, time_color = colors.get(level, ('white', 'white'))
       
       formatted = LOG_TEMPLATE.format(
           level_color=level_color,
           time_color=time_color,
           level=level,
           time=time,
           message=message
       )
       
       return make_colors(formatted)
   
   print(format_log('INFO', '10:30:45', 'User logged in'))

Decorator Pattern
~~~~~~~~~~~~~~~~~

.. code-block:: python

   def colorize_output(color):
       """Decorator to colorize function output."""
       def decorator(func):
           def wrapper(*args, **kwargs):
               result = func(*args, **kwargs)
               return make_colors(str(result), color)
           return wrapper
       return decorator
   
   @colorize_output('green')
   def success_message():
       return "Operation completed successfully"
   
   @colorize_output('red')
   def error_message():
       return "An error occurred"
   
   print(success_message())
   print(error_message())

Context Manager
~~~~~~~~~~~~~~~

.. code-block:: python

   class ColorContext:
       """Context manager for temporary color settings."""
       
       def __init__(self, foreground, background=None):
           self.fg = foreground
           self.bg = background
           self.original_env = os.environ.get('MAKE_COLORS')
       
       def __enter__(self):
           self.color_func = lambda text: make_colors(text, self.fg, self.bg)
           return self.color_func
       
       def __exit__(self, *args):
           if self.original_env:
               os.environ['MAKE_COLORS'] = self.original_env
   
   # Usage
   with ColorContext('red', 'yellow') as color:
       print(color("This is colored"))
       print(color("This too"))

Best Practices
--------------

1. **Consistency**

   Stick to one coloring style throughout your project.

2. **Accessibility**

   Don't rely solely on colors to convey information.

3. **Terminal Detection**

   Let make_colors handle terminal detection automatically.

4. **Performance**

   Cache frequently used colored strings.

5. **Testing**

   Disable colors in tests with ``MAKE_COLORS=0``.

6. **Documentation**

   Document your color scheme for other developers.

See Also
--------

- :doc:`examples` - Practical examples
- :doc:`rich_markup` - Rich markup guide
- :doc:`api/main_functions` - Complete API reference
- :doc:`advanced/environment_vars` - Environment variables guide