Attribute Detection
===================

New Feature: Automatic Attribute Detection
-------------------------------------------

make_colors now supports automatic detection of text attributes from color strings.

Quick Examples
--------------

.. code-block:: python

   from make_colors import make_colors
   
   # Bold text
   print(make_colors("Bold red", "bold-red"))
   
   # Italic text
   print(make_colors("Italic blue", "italic-blue"))
   
   # Multiple attributes
   print(make_colors("Styled", "bold-underline-green"))

Supported Separators
--------------------

Use any of these separators:

- **Hyphen**: ``"bold-red-yellow"``
- **Underscore**: ``"italic_blue_white"``
- **Comma**: ``"underline,green,black"``

All Attributes
--------------

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

See :doc:`usage` for complete documentation.