Practical Examples
==================

This section provides real-world examples of using make_colors in various scenarios.

Logging System
--------------

Create a colorful logging system with different levels:

.. code-block:: python

   from make_colors import make_colors
   import datetime
   
   class ColorLogger:
       """Custom logger with colored output."""
       
       LEVELS = {
           'DEBUG': ('cyan', None),
           'INFO': ('blue', None),
           'SUCCESS': ('green', None),
           'WARNING': ('yellow', 'on_black'),
           'ERROR': ('red', 'on_white'),
           'CRITICAL': ('white', 'on_red')
       }
       
       def __init__(self, name='Logger'):
           self.name = name
       
       def _log(self, level, message):
           timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
           fg, bg = self.LEVELS.get(level, ('white', None))
           
           # Color the level tag
           level_str = make_colors(f"[{level:8}]", fg, bg)
           
           # Color the logger name
           name_str = make_colors(f"[{self.name}]", "lightmagenta")
           
           # Print formatted log
           print(f"{timestamp} {level_str} {name_str} {message}")
       
       def debug(self, msg):
           self._log('DEBUG', msg)
       
       def info(self, msg):
           self._log('INFO', msg)
       
       def success(self, msg):
           self._log('SUCCESS', msg)
       
       def warning(self, msg):
           self._log('WARNING', msg)
       
       def error(self, msg):
           self._log('ERROR', msg)
       
       def critical(self, msg):
           self._log('CRITICAL', msg)
   
   # Usage
   logger = ColorLogger('MyApp')
   logger.debug('Database connection initialized')
   logger.info('User authentication started')
   logger.success('Operation completed successfully')
   logger.warning('Deprecated function called')
   logger.error('Failed to read configuration file')
   logger.critical('System resources exhausted')

Progress Bar
------------

Create an animated progress bar with colors:

.. code-block:: python

   from make_colors import make_colors
   import time
   import sys
   
   def progress_bar(total, prefix='Progress:', length=50, fill='█'):
       """
       Display a colored progress bar.
       
       Args:
           total (int): Total iterations
           prefix (str): Prefix string
           length (int): Character length of bar
           fill (str): Bar fill character
       """
       def print_progress(iteration):
           percent = (iteration / total) * 100
           filled_len = int(length * iteration // total)
           bar = fill * filled_len + '░' * (length - filled_len)
           
           # Choose color based on progress
           if percent < 30:
               color = 'red'
           elif percent < 70:
               color = 'yellow'
           else:
               color = 'green'
           
           colored_bar = make_colors(bar, color)
           percent_str = make_colors(f"{percent:>6.1f}%", 'bold-' + color)
           
           sys.stdout.write(f'\r{prefix} |{colored_bar}| {percent_str}')
           sys.stdout.flush()
       
       # Simulate progress
       for i in range(total + 1):
           time.sleep(0.05)
           print_progress(i)
       
       print()  # New line after completion
   
   # Usage
   progress_bar(100, prefix='Download:')
   progress_bar(50, prefix='Processing:', length=30)

Status Indicators
-----------------

Create status indicators for various states:

.. code-block:: python

   from make_colors import make_colors
   
   class Status:
       """Status indicator with icons and colors."""
       
       STATES = {
           'success': ('✓', 'lightgreen'),
           'error': ('✗', 'lightred'),
           'warning': ('⚠', 'lightyellow'),
           'info': ('ℹ', 'lightblue'),
           'running': ('●', 'lightcyan'),
           'pending': ('◐', 'lightmagenta'),
           'stopped': ('■', 'lightblack'),
       }
       
       @staticmethod
       def show(state, message):
           """Display a status message."""
           if state not in Status.STATES:
               state = 'info'
           
           icon, color = Status.STATES[state]
           icon_colored = make_colors(icon, color)
           print(f"{icon_colored} {message}")
       
       @staticmethod
       def success(msg):
           Status.show('success', msg)
       
       @staticmethod
       def error(msg):
           Status.show('error', msg)
       
       @staticmethod
       def warning(msg):
           Status.show('warning', msg)
       
       @staticmethod
       def info(msg):
           Status.show('info', msg)
   
   # Usage
   Status.success('All tests passed')
   Status.error('Connection timeout')
   Status.warning('Deprecated API used')
   Status.info('Processing started')
   Status.show('running', 'Server is running on port 8000')
   Status.show('pending', 'Waiting for user input')

Syntax Highlighting
-------------------

Simple syntax highlighter for code:

.. code-block:: python

   from make_colors import make_colors
   import re
   
   class SyntaxHighlighter:
       """Simple Python syntax highlighter."""
       
       PATTERNS = {
           'keyword': (r'\b(def|class|import|from|if|else|elif|for|while|'
                      r'return|try|except|with|as|pass|break|continue)\b',
                      'blue'),
           'string': (r'(["\'])(?:(?=(\\?))\2.)*?\1', 'yellow'),
           'comment': (r'#.*$', 'lightblack'),
           'number': (r'\b\d+\.?\d*\b', 'lightcyan'),
           'function': (r'\b([a-zA-Z_][a-zA-Z0-9_]*)\s*\(', 'lightgreen'),
           'decorator': (r'@\w+', 'lightmagenta'),
       }
       
       @staticmethod
       def highlight(code):
           """Highlight Python code."""
           lines = code.split('\n')
           result = []
           
           for line in lines:
               highlighted = line
               
               # Apply patterns in order
               for pattern_name, (pattern, color) in SyntaxHighlighter.PATTERNS.items():
                   matches = list(re.finditer(pattern, line))
                   
                   if matches:
                       offset = 0
                       temp_line = line
                       
                       for match in matches:
                           start = match.start() + offset
                           end = match.end() + offset
                           text = match.group(0)
                           
                           # For function names, only color the name part
                           if pattern_name == 'function':
                               text = match.group(1)
                               end = start + len(text)
                           
                           colored = make_colors(text, color)
                           temp_line = temp_line[:start] + colored + temp_line[end:]
                           offset += len(colored) - len(text)
                       
                       highlighted = temp_line
               
               result.append(highlighted)
           
           return '\n'.join(result)
   
   # Usage
   code = '''
   # Python example
   def hello_world(name="World"):
       """Greet someone."""
       message = f"Hello, {name}!"
       return message
   
   @decorator
   class MyClass:
       pass
   '''
   
   print(SyntaxHighlighter.highlight(code))

Table Formatter
---------------

Create colored tables:

.. code-block:: python

   from make_colors import make_colors
   
   class ColorTable:
       """Create colored formatted tables."""
       
       def __init__(self, headers, rows, header_color='bold-white-blue'):
           self.headers = headers
           self.rows = rows
           self.header_color = header_color
       
       def _get_column_widths(self):
           """Calculate column widths."""
           widths = [len(h) for h in self.headers]
           
           for row in self.rows:
               for i, cell in enumerate(row):
                   widths[i] = max(widths[i], len(str(cell)))
           
           return widths
       
       def _format_row(self, cells, widths, color=None):
           """Format a single row."""
           formatted = []
           for cell, width in zip(cells, widths):
               text = str(cell).ljust(width)
               if color:
                   text = make_colors(text, color)
               formatted.append(text)
           
           return '│ ' + ' │ '.join(formatted) + ' │'
       
       def _separator(self, widths, char='─'):
           """Create separator line."""
           return '├' + char + ('┼' + char).join([char * (w + 2) for w in widths]) + '┤'
       
       def display(self):
           """Display the table."""
           widths = self._get_column_widths()
           
           # Top border
           print('┌' + ('┬').join(['─' * (w + 2) for w in widths]) + '┐')
           
           # Headers
           print(self._format_row(self.headers, widths, self.header_color))
           
           # Separator
           print(self._separator(widths, '═'))
           
           # Rows
           for i, row in enumerate(self.rows):
               # Alternate row colors for better readability
               row_color = 'lightcyan' if i % 2 == 0 else None
               print(self._format_row(row, widths, row_color))
           
           # Bottom border
           print('└' + ('┴').join(['─' * (w + 2) for w in widths]) + '┘')
   
   # Usage
   headers = ['Name', 'Age', 'City', 'Status']
   rows = [
       ['Alice', '30', 'New York', 'Active'],
       ['Bob', '25', 'London', 'Inactive'],
       ['Charlie', '35', 'Tokyo', 'Active'],
       ['Diana', '28', 'Paris', 'Active'],
   ]
   
   table = ColorTable(headers, rows)
   table.display()

Menu System
-----------

Create interactive colored menus:

.. code-block:: python

   from make_colors import make_colors
   
   class ColorMenu:
       """Interactive colored menu system."""
       
       def __init__(self, title, options):
           self.title = title
           self.options = options
       
       def display(self):
           """Display the menu."""
           # Title
           print('\n' + '=' * 50)
           title_colored = make_colors(self.title, 'bold-white-blue')
           print(title_colored.center(50))
           print('=' * 50 + '\n')
           
           # Options
           for i, (key, description) in enumerate(self.options.items(), 1):
               key_colored = make_colors(f"[{key}]", 'bold-yellow')
               print(f"{key_colored} {description}")
           
           print('\n' + '=' * 50)
       
       def get_choice(self):
           """Get user choice."""
           self.display()
           
           while True:
               choice = input(make_colors("\nEnter your choice: ", "bold-green"))
               
               if choice in self.options:
                   return choice
               else:
                   error_msg = make_colors("✗ Invalid choice. Please try again.", "red")
                   print(error_msg)
   
   # Usage
   menu = ColorMenu(
       "Main Menu",
       {
           '1': 'Start Application',
           '2': 'View Settings',
           '3': 'Help Documentation',
           '4': 'About',
           'q': 'Quit'
       }
   )
   
   choice = menu.get_choice()
   print(make_colors(f"\nYou selected: {choice}", "green"))

Diff Viewer
-----------

Show differences between texts with colors:

.. code-block:: python

   from make_colors import make_colors
   import difflib
   
   def colored_diff(text1, text2, context=3):
       """
       Display colored diff between two texts.
       
       Args:
           text1 (str): Original text
           text2 (str): Modified text
           context (int): Lines of context
       """
       lines1 = text1.splitlines()
       lines2 = text2.splitlines()
       
       diff = difflib.unified_diff(
           lines1, lines2,
           lineterm='',
           n=context
       )
       
       for line in diff:
           if line.startswith('---') or line.startswith('+++'):
               print(make_colors(line, 'bold-white'))
           elif line.startswith('@@'):
               print(make_colors(line, 'bold-cyan'))
           elif line.startswith('-'):
               print(make_colors(line, 'red'))
           elif line.startswith('+'):
               print(make_colors(line, 'green'))
           else:
               print(line)
   
   # Usage
   original = """Hello World
   This is a test
   Some content here"""
   
   modified = """Hello World
   This is a modified test
   Some new content here
   Extra line added"""
   
   colored_diff(original, modified)

File Type Icons
---------------

Display file types with colored icons:

.. code-block:: python

   from make_colors import make_colors
   import os
   
   FILE_TYPES = {
       '.py': ('🐍', 'lightblue'),
       '.js': ('📜', 'lightyellow'),
       '.html': ('🌐', 'lightred'),
       '.css': ('🎨', 'lightmagenta'),
       '.json': ('📋', 'lightgreen'),
       '.md': ('📝', 'lightcyan'),
       '.txt': ('📄', 'white'),
       '.pdf': ('📕', 'red'),
       '.zip': ('📦', 'yellow'),
       '.jpg': ('🖼️', 'magenta'),
       '.png': ('🖼️', 'cyan'),
   }
   
   def list_files_colored(directory='.'):
       """List files with colored icons."""
       files = os.listdir(directory)
       
       print(make_colors(f"\n📁 {directory}", "bold-white-blue"))
       print('─' * 60)
       
       for filename in sorted(files):
           ext = os.path.splitext(filename)[1]
           icon, color = FILE_TYPES.get(ext, ('📄', 'white'))
           
           colored_name = make_colors(filename, color)
           print(f"{icon}  {colored_name}")
   
   # Usage
   list_files_colored('.')

See Also
--------

- :doc:`usage` - Detailed usage documentation
- :doc:`api/main_functions` - API reference
- :doc:`rich_markup` - Rich markup format guide