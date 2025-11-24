Custom Formatters
=================

This guide shows how to create custom formatters, themes, and advanced coloring systems
using make_colors.

Creating Custom Formatters
---------------------------

Basic Formatter Class
~~~~~~~~~~~~~~~~~~~~~

Create a reusable formatter:

.. code-block:: python

   from make_colors import make_colors
   
   class CustomFormatter:
       """Custom text formatter with predefined styles."""
       
       def __init__(self):
           self.styles = {
               'header': ('bold-white-blue', ),
               'success': ('bold-green', ),
               'error': ('bold-white-red', ),
               'warning': ('yellow-black', ),
               'info': ('cyan', ),
               'muted': ('lightblack', ),
           }
       
       def format(self, text, style='info'):
           """Format text with predefined style."""
           if style not in self.styles:
               return text
           
           color_spec = self.styles[style][0]
           return make_colors(text, color_spec)
       
       def header(self, text):
           return self.format(text, 'header')
       
       def success(self, text):
           return self.format(text, 'success')
       
       def error(self, text):
           return self.format(text, 'error')
       
       def warning(self, text):
           return self.format(text, 'warning')
       
       def info(self, text):
           return self.format(text, 'info')
       
       def muted(self, text):
           return self.format(text, 'muted')
   
   # Usage
   fmt = CustomFormatter()
   print(fmt.header("=== APPLICATION HEADER ==="))
   print(fmt.success("✓ Operation completed"))
   print(fmt.error("✗ Error occurred"))
   print(fmt.warning("⚠ Warning message"))
   print(fmt.info("ℹ Information"))
   print(fmt.muted("(This is less important)"))

Advanced Formatter with Context
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Context-aware formatter:

.. code-block:: python

   from make_colors import make_colors
   import datetime
   
   class ContextFormatter:
       """Formatter with context support."""
       
       def __init__(self, context=None):
           self.context = context or {}
           self.timestamp_format = "%Y-%m-%d %H:%M:%S"
       
       def format_log(self, level, message, **kwargs):
           """Format log entry with timestamp and context."""
           # Merge kwargs with context
           data = {**self.context, **kwargs}
           
           # Timestamp
           timestamp = datetime.datetime.now().strftime(
               self.timestamp_format
           )
           ts_colored = make_colors(timestamp, "lightblack")
           
           # Level with color
           level_colors = {
               'DEBUG': 'cyan',
               'INFO': 'blue',
               'WARNING': 'yellow',
               'ERROR': 'red',
               'CRITICAL': 'white-red'
           }
           level_colored = make_colors(
               f"[{level:8}]",
               level_colors.get(level, 'white')
           )
           
           # Context
           context_str = ""
           if data:
               pairs = [f"{k}={v}" for k, v in data.items()]
               context_str = " " + make_colors(
                   f"({', '.join(pairs)})",
                   "lightmagenta"
               )
           
           # Combine
           return f"{ts_colored} {level_colored} {message}{context_str}"
       
       def with_context(self, **kwargs):
           """Create new formatter with additional context."""
           new_context = {**self.context, **kwargs}
           return ContextFormatter(new_context)
   
   # Usage
   fmt = ContextFormatter(context={'app': 'myapp', 'version': '1.0'})
   
   print(fmt.format_log('INFO', 'Server started', port=8000))
   print(fmt.format_log('ERROR', 'Connection failed', host='localhost'))
   
   # Create sub-formatter with more context
   request_fmt = fmt.with_context(request_id='abc123')
   print(request_fmt.format_log('DEBUG', 'Processing request'))

Theme System
------------

Creating Themes
~~~~~~~~~~~~~~~

Define color themes:

.. code-block:: python

   from make_colors import make_colors
   
   class Theme:
       """Base theme class."""
       
       # Override these in subclasses
       PRIMARY = 'blue'
       SECONDARY = 'cyan'
       SUCCESS = 'green'
       WARNING = 'yellow'
       ERROR = 'red'
       INFO = 'blue'
       MUTED = 'lightblack'
       
       @classmethod
       def primary(cls, text):
           return make_colors(text, cls.PRIMARY)
       
       @classmethod
       def secondary(cls, text):
           return make_colors(text, cls.SECONDARY)
       
       @classmethod
       def success(cls, text):
           return make_colors(text, cls.SUCCESS)
       
       @classmethod
       def warning(cls, text):
           return make_colors(text, cls.WARNING)
       
       @classmethod
       def error(cls, text):
           return make_colors(text, cls.ERROR)
       
       @classmethod
       def info(cls, text):
           return make_colors(text, cls.INFO)
       
       @classmethod
       def muted(cls, text):
           return make_colors(text, cls.MUTED)
   
   class DarkTheme(Theme):
       """Dark color theme."""
       PRIMARY = 'lightblue'
       SECONDARY = 'lightcyan'
       SUCCESS = 'lightgreen'
       WARNING = 'lightyellow'
       ERROR = 'lightred'
       INFO = 'lightblue'
       MUTED = 'lightblack'
   
   class LightTheme(Theme):
       """Light color theme."""
       PRIMARY = 'blue'
       SECONDARY = 'cyan'
       SUCCESS = 'green'
       WARNING = 'yellow'
       ERROR = 'red'
       INFO = 'blue'
       MUTED = 'black'
   
   class SolarizedTheme(Theme):
       """Solarized-inspired theme."""
       PRIMARY = 'cyan'
       SECONDARY = 'blue'
       SUCCESS = 'green'
       WARNING = 'yellow'
       ERROR = 'red'
       INFO = 'cyan'
       MUTED = 'lightblack'
   
   # Usage
   theme = DarkTheme
   print(theme.success("✓ Task completed"))
   print(theme.error("✗ Error occurred"))
   print(theme.muted("Additional info"))

Dynamic Theme Switching
~~~~~~~~~~~~~~~~~~~~~~~

Switch themes at runtime:

.. code-block:: python

   import os
   
   class ThemeManager:
       """Manage and switch themes."""
       
       THEMES = {
           'dark': DarkTheme,
           'light': LightTheme,
           'solarized': SolarizedTheme,
       }
       
       def __init__(self, default='dark'):
           self._current = self.THEMES.get(default, DarkTheme)
       
       @property
       def current(self):
           return self._current
       
       def set_theme(self, name):
           """Switch to a different theme."""
           if name in self.THEMES:
               self._current = self.THEMES[name]
           else:
               raise ValueError(f"Unknown theme: {name}")
       
       def detect_theme(self):
           """Auto-detect theme from environment."""
           # Check environment variable
           theme_name = os.getenv('COLOR_THEME', 'dark')
           self.set_theme(theme_name)
       
       # Proxy methods
       def primary(self, text):
           return self._current.primary(text)
       
       def success(self, text):
           return self._current.success(text)
       
       def error(self, text):
           return self._current.error(text)
   
   # Usage
   theme = ThemeManager()
   theme.detect_theme()
   
   print(theme.success("Success message"))
   
   # Switch theme
   theme.set_theme('light')
   print(theme.success("Success in light theme"))

Custom Color Schemes
--------------------

Color Palette Generator
~~~~~~~~~~~~~~~~~~~~~~~

Generate complementary color schemes:

.. code-block:: python

   from make_colors import make_colors
   
   class ColorScheme:
       """Generate color schemes."""
       
       @staticmethod
       def monochromatic(base_color, variations=3):
           """Generate monochromatic scheme."""
           # Base + lighter versions
           colors = [base_color]
           if base_color.startswith('light'):
               return colors
           colors.append(f'light{base_color}')
           return colors
       
       @staticmethod
       def complementary(color):
           """Generate complementary colors."""
           complements = {
               'red': 'cyan',
               'green': 'magenta',
               'blue': 'yellow',
               'cyan': 'red',
               'magenta': 'green',
               'yellow': 'blue',
           }
           return complements.get(color, 'white')
       
       @staticmethod
       def triad(color):
           """Generate triadic colors."""
           triads = {
               'red': ['blue', 'yellow'],
               'blue': ['red', 'yellow'],
               'yellow': ['red', 'blue'],
               'green': ['magenta', 'cyan'],
               'magenta': ['green', 'cyan'],
               'cyan': ['green', 'magenta'],
           }
           return triads.get(color, ['white', 'white'])
   
   # Usage
   scheme = ColorScheme()
   
   base = 'blue'
   complement = scheme.complementary(base)
   triads = scheme.triad(base)
   
   print(make_colors("Primary", base))
   print(make_colors("Complement", complement))
   for i, color in enumerate(triads, 1):
       print(make_colors(f"Triad {i}", color))

Syntax Highlighter Formatter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Custom syntax highlighting:

.. code-block:: python

   import re
   from make_colors import make_colors
   
   class SyntaxHighlighter:
       """Syntax highlighter with custom schemes."""
       
       def __init__(self, scheme='default'):
           self.schemes = {
               'default': {
                   'keyword': 'blue',
                   'string': 'green',
                   'comment': 'lightblack',
                   'number': 'cyan',
                   'function': 'yellow',
                   'class': 'lightgreen',
               },
               'solarized': {
                   'keyword': 'green',
                   'string': 'cyan',
                   'comment': 'lightblack',
                   'number': 'magenta',
                   'function': 'blue',
                   'class': 'yellow',
               },
               'monokai': {
                   'keyword': 'magenta',
                   'string': 'yellow',
                   'comment': 'lightblack',
                   'number': 'lightmagenta',
                   'function': 'lightgreen',
                   'class': 'lightgreen',
               }
           }
           self.current_scheme = self.schemes.get(scheme, self.schemes['default'])
       
       def highlight_python(self, code):
           """Highlight Python code."""
           patterns = {
               'keyword': r'\b(def|class|import|from|if|else|for|while|return)\b',
               'string': r'(["\'])(?:(?=(\\?))\2.)*?\1',
               'comment': r'#.*$',
               'number': r'\b\d+\.?\d*\b',
               'function': r'\b(\w+)\s*\(',
               'class': r'\bclass\s+(\w+)',
           }
           
           # Apply highlighting
           result = code
           for token_type, pattern in patterns.items():
               color = self.current_scheme[token_type]
               result = re.sub(
                   pattern,
                   lambda m: make_colors(m.group(0), color),
                   result,
                   flags=re.MULTILINE
               )
           
           return result
   
   # Usage
   highlighter = SyntaxHighlighter('monokai')
   
   code = '''
   def hello(name):
       """Say hello."""
       # This is a comment
       message = f"Hello, {name}!"
       return message
   '''
   
   print(highlighter.highlight_python(code))

Advanced Formatting
-------------------

Table Formatter
~~~~~~~~~~~~~~~

Create formatted tables:

.. code-block:: python

   from make_colors import make_colors
   
   class TableFormatter:
       """Format tables with colors."""
       
       def __init__(self, header_color='bold-white-blue',
                    row_colors=None,
                    border_color='cyan'):
           self.header_color = header_color
           self.row_colors = row_colors or ['white', 'lightblack']
           self.border_color = border_color
       
       def format(self, headers, rows, column_widths=None):
           """Format table."""
           if not column_widths:
               # Calculate widths
               column_widths = [len(h) for h in headers]
               for row in rows:
                   for i, cell in enumerate(row):
                       column_widths[i] = max(
                           column_widths[i],
                           len(str(cell))
                       )
           
           # Top border
           top = self._border_line('┌', '┬', '┐', column_widths)
           print(make_colors(top, self.border_color))
           
           # Headers
           header_line = self._format_row(headers, column_widths)
           print(make_colors(header_line, self.header_color))
           
           # Separator
           sep = self._border_line('├', '┼', '┤', column_widths)
           print(make_colors(sep, self.border_color))
           
           # Rows
           for i, row in enumerate(rows):
               color = self.row_colors[i % len(self.row_colors)]
               row_line = self._format_row(row, column_widths)
               print(make_colors(row_line, color))
           
           # Bottom border
           bottom = self._border_line('└', '┴', '┘', column_widths)
           print(make_colors(bottom, self.border_color))
       
       def _format_row(self, cells, widths):
           """Format single row."""
           formatted = []
           for cell, width in zip(cells, widths):
               formatted.append(str(cell).ljust(width))
           return '│ ' + ' │ '.join(formatted) + ' │'
       
       def _border_line(self, left, middle, right, widths):
           """Create border line."""
           segments = ['─' * (w + 2) for w in widths]
           return left + middle.join(segments) + right
   
   # Usage
   formatter = TableFormatter()
   
   headers = ['Name', 'Age', 'City']
   rows = [
       ['Alice', '30', 'New York'],
       ['Bob', '25', 'London'],
       ['Charlie', '35', 'Tokyo'],
   ]
   
   formatter.format(headers, rows)

Progress Bar Formatter
~~~~~~~~~~~~~~~~~~~~~~

Customizable progress bars:

.. code-block:: python

   from make_colors import make_colors
   import sys
   
   class ProgressBar:
       """Customizable progress bar."""
       
       def __init__(self, total, width=50, fill='█', empty='░',
                    color_ranges=None):
           self.total = total
           self.width = width
           self.fill = fill
           self.empty = empty
           self.color_ranges = color_ranges or [
               (0, 30, 'red'),
               (30, 70, 'yellow'),
               (70, 100, 'green')
           ]
       
       def get_color(self, percent):
           """Get color based on percentage."""
           for min_pct, max_pct, color in self.color_ranges:
               if min_pct <= percent < max_pct:
                   return color
           return self.color_ranges[-1][2]  # Last color
       
       def show(self, current, message=''):
           """Display progress bar."""
           percent = (current / self.total) * 100
           filled = int(self.width * current / self.total)
           
           bar = self.fill * filled + self.empty * (self.width - filled)
           color = self.get_color(percent)
           
           colored_bar = make_colors(bar, color)
           percent_str = make_colors(f"{percent:5.1f}%", f"bold-{color}")
           
           sys.stdout.write(
               f'\r{message} |{colored_bar}| {percent_str}'
           )
           sys.stdout.flush()
       
       def finish(self):
           """Finish progress bar."""
           print()  # New line
   
   # Usage
   import time
   
   progress = ProgressBar(total=100)
   for i in range(101):
       progress.show(i, "Processing:")
       time.sleep(0.02)
   progress.finish()

See Also
--------

- :doc:`../usage` - Complete usage guide
- :doc:`../examples` - Practical examples
- :doc:`../api/classes` - Classes API reference