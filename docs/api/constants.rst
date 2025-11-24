Constants and Color Codes
==========================

This section documents all constants, color codes, and predefined values in make_colors.

ANSI Control Codes
------------------

RESET
~~~~~

.. py:data:: RESET
   :type: str
   :value: "\\033[0m"

   ANSI reset sequence that clears all text formatting.

   This constant is used to reset text back to terminal defaults after
   applying colors or attributes.

   **Example:**

   .. code-block:: python

      from make_colors import RESET
      
      text = "\033[31mRed text" + RESET + " Normal text"
      print(text)

REST
~~~~

.. py:data:: REST
   :type: str
   :value: "[0m"

   Alternative reset sequence (without escape character prefix).

   **Example:**

   .. code-block:: python

      from make_colors import REST
      
      # Used in some internal formatting
      formatted = "[31mRed" + REST

Color Code Dictionaries
------------------------

FG_CODES
~~~~~~~~

.. py:data:: FG_CODES
   :type: dict[str, str]

   Dictionary mapping foreground color names to ANSI codes.

   **Standard Colors (30-37):**

   =========== ====== ==================
   Color Name  Code   Description
   =========== ====== ==================
   black       30     Black text
   red         31     Red text
   green       32     Green text
   yellow      33     Yellow text
   blue        34     Blue text
   magenta     35     Magenta text
   cyan        36     Cyan text
   white       37     White text
   =========== ====== ==================

   **Bright Colors (90-97):**

   =============== ====== ==================
   Color Name      Code   Description
   =============== ====== ==================
   lightblack      90     Bright black/gray
   lightgrey       90     Alias for lightblack
   lightred        91     Bright red
   lightgreen      92     Bright green
   lightyellow     93     Bright yellow
   lightblue       94     Bright blue
   lightmagenta    95     Bright magenta
   lightcyan       96     Bright cyan
   lightwhite      97     Bright white
   =============== ====== ==================

   **Example:**

   .. code-block:: python

      from make_colors import FG_CODES
      
      # Get ANSI code for red
      red_code = FG_CODES['red']
      print(f"Red ANSI code: {red_code}")  # Output: 31
      
      # List all foreground colors
      for color, code in FG_CODES.items():
          print(f"{color}: {code}")

BG_CODES
~~~~~~~~

.. py:data:: BG_CODES
   :type: dict[str, str]

   Dictionary mapping background color names to ANSI codes.

   **Standard Backgrounds (40-47):**

   =========== ====== ==================
   Color Name  Code   Description
   =========== ====== ==================
   black       40     Black background
   red         41     Red background
   green       42     Green background
   yellow      43     Yellow background
   blue        44     Blue background
   magenta     45     Magenta background
   cyan        46     Cyan background
   white       47     White background
   =========== ====== ==================

   **Bright Backgrounds (100-107):**

   =============== ====== ======================
   Color Name      Code   Description
   =============== ====== ======================
   lightblack      100    Bright black background
   lightgrey       100    Alias for lightblack
   lightred        101    Bright red background
   lightgreen      102    Bright green background
   lightyellow     103    Bright yellow background
   lightblue       104    Bright blue background
   lightmagenta    105    Bright magenta background
   lightcyan       106    Bright cyan background
   lightwhite      107    Bright white background
   =============== ====== ======================

   **With 'on_' Prefix:**

   All colors are also available with ``on_`` prefix:

   - ``on_black``, ``on_red``, ``on_green``, etc.
   - ``on_lightblack``, ``on_lightred``, etc.

   **Example:**

   .. code-block:: python

      from make_colors import BG_CODES
      
      # Get ANSI code for yellow background
      yellow_bg = BG_CODES['yellow']
      print(f"Yellow background code: {yellow_bg}")  # Output: 43
      
      # Using 'on_' prefix
      yellow_on = BG_CODES['on_yellow']
      print(f"on_yellow code: {yellow_on}")  # Output: 43

ATTR_CODES
~~~~~~~~~~

.. py:data:: ATTR_CODES
   :type: dict[str, str]

   Dictionary mapping text attribute names to ANSI codes.

   **Text Attributes:**

   =============== ====== ================================
   Attribute       Code   Description
   =============== ====== ================================
   bold            1      Bold or increased intensity
   dim             2      Faint, decreased intensity
   italic          3      Italic (not widely supported)
   underline       4      Underlined text
   blink           5      Slow blink (rarely supported)
   reverse         7      Reverse video (swap fg/bg)
   strikethrough   9      Crossed out text
   strike          9      Alias for strikethrough
   normal          22     Normal intensity (reset bold/dim)
   no_italic       23     Not italic
   no_underline    24     Not underlined
   =============== ====== ================================

   **Example:**

   .. code-block:: python

      from make_colors import ATTR_CODES
      
      # Get ANSI code for bold
      bold_code = ATTR_CODES['bold']
      print(f"Bold code: {bold_code}")  # Output: 1
      
      # List all attributes
      for attr, code in ATTR_CODES.items():
          print(f"{attr}: {code}")

Abbreviation Mappings
---------------------

_MAIN_ABBR
~~~~~~~~~~

.. py:data:: _MAIN_ABBR
   :type: dict[str, str]

   Dictionary mapping full color names to their primary abbreviations.

   **Abbreviation Map:**

   =============== ======
   Full Name       Abbrev
   =============== ======
   black           b
   blue            bl
   red             r
   green           g
   yellow          y
   magenta         m
   cyan            c
   white           w
   lightblue       lb
   lightred        lr
   lightgreen      lg
   lightyellow     ly
   lightmagenta    lm
   lightcyan       lc
   lightwhite      lw
   lightblack      lk
   =============== ======

   **Example:**

   .. code-block:: python

      from make_colors import _MAIN_ABBR
      
      # Get abbreviation for 'red'
      red_abbr = _MAIN_ABBR['red']
      print(f"Red abbreviation: {red_abbr}")  # Output: r
      
      # Reverse lookup
      full_name = next(k for k, v in _MAIN_ABBR.items() if v == 'lb')
      print(f"'lb' is short for: {full_name}")  # Output: lightblue

Environment Variable Controls
-----------------------------

_USE_COLOR
~~~~~~~~~~

.. py:data:: _USE_COLOR
   :type: bool

   Boolean flag indicating whether color output is enabled.

   This is determined by checking if ``sys.stdout`` is a TTY (terminal).
   When False, functions return plain text without ANSI codes.

   **Example:**

   .. code-block:: python

      from make_colors import _USE_COLOR
      
      if _USE_COLOR:
          print("Colors are enabled")
      else:
          print("Colors are disabled (non-TTY output)")

_DEBUG
~~~~~~

.. py:data:: _DEBUG
   :type: bool

   Boolean flag indicating whether debug mode is enabled.

   Set via the ``MAKE_COLORS_DEBUG`` environment variable.
   When True, functions print detailed parsing information.

   **Example:**

   .. code-block:: python

      from make_colors import _DEBUG
      
      if _DEBUG:
          print("Debug mode is active")

Platform Constants
------------------

MODE
~~~~

.. py:data:: MODE
   :type: int | ctypes.c_ulong

   Windows console mode value (Windows only).

   On Windows, this stores the console mode used to enable ANSI escape
   sequence processing. On other platforms, it's set to 0.

   **Windows Only:**

   .. code-block:: python

      import sys
      if sys.platform == 'win32':
          from make_colors import MODE
          print(f"Console mode: {MODE.value}")

Dynamic Function Names
----------------------

__all__
~~~~~~~

.. py:data:: __all__
   :type: list[str]

   List of all public names exported by the module.

   This includes:
   
   - All foreground color names (``red``, ``green``, etc.)
   - All color combinations (``red_on_yellow``, etc.)
   - All abbreviation functions (``r``, ``g``, ``lb``, etc.)
   - Main functions (``make_colors``, ``colorize``, etc.)
   - Utility functions (``getSort``, ``color_map``, etc.)

   **Example:**

   .. code-block:: python

      from make_colors import __all__
      
      print(f"Total exported names: {len(__all__)}")
      
      # Show all available functions
      for name in sorted(__all__):
          print(name)

Generated Constants
-------------------

The module dynamically generates several function sets:

_fg_funcs
~~~~~~~~~

Dictionary of foreground-only color functions.

**Example:** ``red()``, ``green()``, ``blue()``, etc.

_combo_funcs
~~~~~~~~~~~~

Dictionary of foreground+background combination functions.

**Example:** ``red_on_yellow()``, ``white_on_blue()``, etc.

_abbr_combo_funcs
~~~~~~~~~~~~~~~~~

Dictionary of abbreviated combination functions.

**Example:** ``r_y()``, ``w_bl()``, ``g_b()``, etc.

_abbr_fg_funcs
~~~~~~~~~~~~~~

Dictionary of abbreviated foreground-only functions.

**Example:** ``r()``, ``g()``, ``bl()``, ``lb()``, etc.

Color Reference Chart
---------------------

Complete ANSI Color Code Chart
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: Foreground Colors
   :header-rows: 1
   :widths: 20 10 15 55

   * - Color Name
     - Code
     - Abbreviation
     - ANSI Sequence
   * - black
     - 30
     - b, bk
     - ``\033[30m``
   * - red
     - 31
     - r, rd, re
     - ``\033[31m``
   * - green
     - 32
     - g, gr, ge
     - ``\033[32m``
   * - yellow
     - 33
     - y, ye, yl
     - ``\033[33m``
   * - blue
     - 34
     - bl
     - ``\033[34m``
   * - magenta
     - 35
     - m, mg, ma
     - ``\033[35m``
   * - cyan
     - 36
     - c, cy, cn
     - ``\033[36m``
   * - white
     - 37
     - w, wh, wi, wt
     - ``\033[37m``
   * - lightblack
     - 90
     - lk
     - ``\033[90m``
   * - lightred
     - 91
     - lr
     - ``\033[91m``
   * - lightgreen
     - 92
     - lg
     - ``\033[92m``
   * - lightyellow
     - 93
     - ly
     - ``\033[93m``
   * - lightblue
     - 94
     - lb
     - ``\033[94m``
   * - lightmagenta
     - 95
     - lm
     - ``\033[95m``
   * - lightcyan
     - 96
     - lc
     - ``\033[96m``
   * - lightwhite
     - 97
     - lw
     - ``\033[97m``

Using Constants Directly
------------------------

You can use the constants directly to build custom ANSI sequences:

.. code-block:: python

   from make_colors import FG_CODES, BG_CODES, ATTR_CODES, RESET
   
   # Build custom ANSI sequence
   bold = ATTR_CODES['bold']
   red = FG_CODES['red']
   yellow_bg = BG_CODES['yellow']
   
   # Combine codes
   ansi_seq = f"\033[{bold};{yellow_bg};{red}m"
   text = f"{ansi_seq}Bold red on yellow{RESET}"
   print(text)

Accessing All Color Codes
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from make_colors import FG_CODES, BG_CODES, ATTR_CODES
   
   def show_all_codes():
       """Display all available color codes."""
       print("Foreground Colors:")
       for name, code in FG_CODES.items():
           print(f"  {name:15} -> {code}")
       
       print("\nBackground Colors:")
       for name, code in BG_CODES.items():
           print(f"  {name:20} -> {code}")
       
       print("\nText Attributes:")
       for name, code in ATTR_CODES.items():
           print(f"  {name:15} -> {code}")
   
   show_all_codes()

See Also
--------

- :doc:`main_functions` - Main function documentation
- :doc:`classes` - Classes API reference
- :doc:`utilities` - Utility functions
- :doc:`../usage` - Complete usage guide