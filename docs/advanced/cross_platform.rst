Cross-Platform Guide
====================

make_colors is designed to work seamlessly across Windows, Linux, and macOS. This guide
covers platform-specific considerations and best practices.

Platform Support
----------------

Supported Platforms
~~~~~~~~~~~~~~~~~~~

✅ **Windows 10 and later** - Full ANSI support

✅ **Windows 11** - Full ANSI support

✅ **Linux** - All modern distributions

✅ **macOS** - All recent versions

✅ **WSL** (Windows Subsystem for Linux) - Full support

✅ **BSD** - Most variants

Partially Supported
~~~~~~~~~~~~~~~~~~~

⚠️ **Windows 7/8/8.1** - Requires ANSICON or terminal emulator

⚠️ **Older terminals** - May have limited attribute support

Platform-Specific Behavior
---------------------------

Windows
~~~~~~~

**Windows 10+**

make_colors automatically enables ANSI escape sequence processing on Windows 10
and later by modifying the console mode:

.. code-block:: python

   # Automatic Windows setup (happens on import)
   import sys
   if sys.platform == 'win32':
       import ctypes
       kernel32 = ctypes.WinDLL('kernel32')
       hStdOut = kernel32.GetStdHandle(-11)
       mode = ctypes.c_ulong()
       kernel32.GetConsoleMode(hStdOut, ctypes.byref(mode))
       mode.value |= 4  # Enable ANSI processing
       kernel32.SetConsoleMode(hStdOut, mode)

**Supported Terminals:**

- Command Prompt (cmd.exe) - Windows 10+
- PowerShell - All versions on Windows 10+
- Windows Terminal - Recommended
- ConEmu - Full support
- Cmder - Full support

**Code Page Considerations:**

.. code-block:: python

   # Ensure UTF-8 output on Windows
   import sys
   if sys.platform == 'win32':
       sys.stdout.reconfigure(encoding='utf-8')

Linux
~~~~~

**Full Support:**

Linux terminals generally have the best ANSI support. All features work
out of the box.

**Common Terminals:**

- GNOME Terminal - Full support
- Konsole (KDE) - Full support
- xterm - Full support
- rxvt/urxvt - Full support
- Terminator - Full support
- Tilix - Full support

**Special Considerations:**

- Check ``$TERM`` environment variable
- Some attributes (italic, blink) may not work in all terminals

.. code-block:: python

   import os
   
   # Check terminal type
   term = os.getenv('TERM', 'unknown')
   print(f"Terminal: {term}")
   
   # Common values: xterm, xterm-256color, screen, linux

macOS
~~~~~

**Terminal Support:**

- Terminal.app - Full support
- iTerm2 - Full support (recommended)
- Hyper - Full support
- Alacritty - Full support

**Special Notes:**

- macOS Terminal has excellent ANSI support
- True color (24-bit) support varies by terminal
- Some emoji may render differently

Detection and Fallback
-----------------------

Automatic Detection
~~~~~~~~~~~~~~~~~~~

make_colors automatically detects terminal capabilities:

.. code-block:: python

   from make_colors import MakeColors
   
   # Checks:
   # 1. Platform (not Pocket PC)
   # 2. TTY detection (sys.stdout.isatty())
   # 3. Windows console mode
   # 4. ANSICON environment variable
   
   if MakeColors.supports_color():
       print("Colors supported!")
   else:
       print("Plain text mode")

Manual Detection
~~~~~~~~~~~~~~~~

You can check specific capabilities:

.. code-block:: python

   import sys
   import os
   
   def check_terminal_support():
       """Check terminal capabilities."""
       info = {
           'platform': sys.platform,
           'is_tty': sys.stdout.isatty(),
           'term': os.getenv('TERM', 'unknown'),
           'colorterm': os.getenv('COLORTERM', 'none'),
           'ansicon': 'ANSICON' in os.environ
       }
       
       # Windows specific
       if sys.platform == 'win32':
           try:
               import ctypes
               kernel32 = ctypes.WinDLL('kernel32')
               mode = ctypes.c_ulong()
               kernel32.GetConsoleMode(
                   kernel32.GetStdHandle(-11),
                   ctypes.byref(mode)
               )
               info['console_mode'] = mode.value
               info['ansi_enabled'] = bool(mode.value & 4)
           except:
               info['console_mode'] = 'unknown'
       
       return info
   
   # Check support
   support = check_terminal_support()
   for key, value in support.items():
       print(f"{key}: {value}")

Handling Unsupported Terminals
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Graceful degradation for older systems:

.. code-block:: python

   from make_colors import make_colors, MakeColors
   import sys
   
   class SafeColorPrint:
       """Print with colors if supported, plain text otherwise."""
       
       def __init__(self):
           self.supports_color = MakeColors.supports_color()
       
       def print(self, text, color='white', **kwargs):
           if self.supports_color:
               colored = make_colors(text, color)
               print(colored, **kwargs)
           else:
               print(text, **kwargs)
   
   # Usage
   printer = SafeColorPrint()
   printer.print("This works everywhere!", "green")

Platform-Specific Code
-----------------------

Conditional Logic
~~~~~~~~~~~~~~~~~

Execute platform-specific code:

.. code-block:: python

   import sys
   from make_colors import make_colors
   
   def platform_specific_setup():
       """Setup based on platform."""
       
       if sys.platform == 'win32':
           # Windows specific
           print(make_colors("Running on Windows", "blue"))
           # Enable UTF-8
           import codecs
           sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)
       
       elif sys.platform == 'darwin':
           # macOS specific
           print(make_colors("Running on macOS", "green"))
       
       elif sys.platform.startswith('linux'):
           # Linux specific
           print(make_colors("Running on Linux", "cyan"))
       
       else:
           # Other platforms
           print(make_colors("Unknown platform", "yellow"))

Windows-Specific Features
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import sys
   
   if sys.platform == 'win32':
       import ctypes
       from ctypes import wintypes
       
       # Windows console APIs
       kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
       
       def get_console_mode():
           """Get current console mode."""
           h = kernel32.GetStdHandle(-11)  # STD_OUTPUT_HANDLE
           mode = wintypes.DWORD()
           kernel32.GetConsoleMode(h, ctypes.byref(mode))
           return mode.value
       
       def set_console_mode(mode):
           """Set console mode."""
           h = kernel32.GetStdHandle(-11)
           return kernel32.SetConsoleMode(h, mode)
       
       # Check and enable ANSI
       current_mode = get_console_mode()
       if not (current_mode & 4):
           set_console_mode(current_mode | 4)
           print("ANSI support enabled!")

Testing Across Platforms
-------------------------

Unified Testing
~~~~~~~~~~~~~~~

Test on all platforms:

.. code-block:: python

   import sys
   import pytest
   from make_colors import make_colors, MakeColors
   
   class TestCrossPlatform:
       """Cross-platform tests."""
       
       def test_basic_color(self):
           """Test basic coloring works on all platforms."""
           result = make_colors("Test", "red")
           assert result  # Should always return something
       
       def test_color_support_detection(self):
           """Test color support detection."""
           supported = MakeColors.supports_color()
           assert isinstance(supported, bool)
       
       @pytest.mark.skipif(
           sys.platform != 'win32',
           reason="Windows-specific test"
       )
       def test_windows_console(self):
           """Test Windows console mode."""
           import ctypes
           kernel32 = ctypes.WinDLL('kernel32')
           mode = ctypes.c_ulong()
           kernel32.GetConsoleMode(
               kernel32.GetStdHandle(-11),
               ctypes.byref(mode)
           )
           # Check ANSI is enabled
           assert mode.value & 4
       
       @pytest.mark.skipif(
           sys.platform == 'win32',
           reason="Unix-specific test"
       )
       def test_unix_term(self):
           """Test Unix TERM variable."""
           import os
           term = os.getenv('TERM')
           assert term  # Should have TERM set

CI/CD Testing
~~~~~~~~~~~~~

Test on multiple platforms with GitHub Actions:

.. code-block:: yaml

   # .github/workflows/test.yml
   name: Cross-Platform Tests
   
   on: [push, pull_request]
   
   jobs:
     test:
       runs-on: ${{ matrix.os }}
       strategy:
         matrix:
           os: [ubuntu-latest, windows-latest, macos-latest]
           python-version: ['3.8', '3.9', '3.10', '3.11']
       
       steps:
       - uses: actions/checkout@v2
       - name: Set up Python
         uses: actions/setup-python@v2
         with:
           python-version: ${{ matrix.python-version }}
       - name: Install dependencies
         run: |
           pip install -r requirements.txt
           pip install pytest
       - name: Run tests
         env:
           MAKE_COLORS_FORCE: 1  # Force colors in CI
         run: pytest

Common Issues and Solutions
----------------------------

Windows: Colors Not Working
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Problem:** Colors don't appear on Windows 7/8

**Solution:** Use Windows Terminal or install ANSICON:

.. code-block:: bash

   # Install ANSICON
   choco install ansicon

Or check Windows version:

.. code-block:: python

   import sys
   import platform
   
   if sys.platform == 'win32':
       version = platform.win32_ver()[0]
       print(f"Windows version: {version}")
       
       if version < '10':
           print("Warning: Colors may not work on Windows < 10")
           print("Consider using Windows Terminal or ANSICON")

Linux: Attribute Not Working
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Problem:** Italic or blink doesn't work

**Solution:** Check terminal capabilities:

.. code-block:: bash

   # Check terminal info
   infocmp
   
   # Test italic support
   echo -e "\e[3mItalic text\e[0m"

.. code-block:: python

   import os
   
   def check_terminal_features():
       """Check which features are supported."""
       term = os.getenv('TERM', 'unknown')
       
       # Known limitations
       limited_terms = ['linux', 'screen']
       
       if term in limited_terms:
           print(f"Terminal '{term}' has limited attribute support")
           return False
       
       return True

macOS: Emoji Issues
~~~~~~~~~~~~~~~~~~~

**Problem:** Emoji render incorrectly or cause alignment issues

**Solution:** Use Unicode-aware formatting:

.. code-block:: python

   import unicodedata
   from make_colors import make_colors
   
   def safe_width(text):
       """Calculate display width considering emoji."""
       width = 0
       for char in text:
           if unicodedata.east_asian_width(char) in 'FW':
               width += 2  # Full-width
           else:
               width += 1
       return width
   
   def align_with_emoji(text, width):
       """Align text that may contain emoji."""
       actual_width = safe_width(text)
       padding = width - actual_width
       return text + ' ' * padding

Best Practices
--------------

1. **Always Check Support**

   .. code-block:: python

      from make_colors import MakeColors
      
      if MakeColors.supports_color():
          # Use colors
          pass
      else:
          # Plain text fallback
          pass

2. **Test on Target Platforms**

   Test your application on the actual platforms you support.

3. **Provide Fallbacks**

   Always have a plain-text fallback:

   .. code-block:: python

      def safe_print(text, color='white'):
          try:
              print(make_colors(text, color))
          except Exception:
              print(text)  # Fallback

4. **Document Platform Requirements**

   In your README:

   .. code-block:: markdown

      ## Platform Support
      
      - Windows 10+ (native ANSI support)
      - Windows 7/8 (requires Windows Terminal or ANSICON)
      - Linux (all modern distributions)
      - macOS (all recent versions)

5. **Use Environment Variables**

   Allow users to control behavior:

   .. code-block:: python

      import os
      
      # Respect NO_COLOR standard
      if os.getenv('NO_COLOR'):
          os.environ['MAKE_COLORS'] = '0'

See Also
--------

- :doc:`environment_vars` - Environment configuration
- :doc:`../installation` - Installation guide
- :doc:`../examples` - Practical examples