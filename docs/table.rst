================
Table Module
================

.. module:: make_colors.table
   :synopsis: Create beautiful colored tables with Rich-style API

The ``table`` module provides a powerful and flexible way to create beautiful, colored tables in your terminal output. It supports both modern Rich-style API and traditional table API with full integration with make_colors.

.. contents:: Table of Contents
   :local:
   :depth: 2

Quick Start
===========

Basic Example
-------------

.. code-block:: python

    from make_colors.table import Table

    # Create a table with title
    table = Table(title="Server Status", title_style="bold cyan")
    
    # Add columns
    table.add_column("Service", style="bold")
    table.add_column("Status", style="green")
    table.add_column("Uptime", style="yellow")
    
    # Add rows
    table.add_row("Web Server", "✓ Running", "15d 6h")
    table.add_row("Database", "✓ Running", "15d 6h")
    table.add_row("Cache", "⚠ Warning", "2d 3h", style="yellow")
    
    # Display
    print(table.draw())

Output:

.. code-block:: text

               Server Status
    +------------+-----------+---------+
    |  Service   |  Status   | Uptime  |
    +============+===========+=========+
    | Web Server | ✓ Running | 15d 6h  |
    +------------+-----------+---------+
    | Database   | ✓ Running | 15d 6h  |
    +------------+-----------+---------+
    | Cache      | ⚠ Warning | 2d 3h   |
    +------------+-----------+---------+

Features
========

* ✅ **Rich-style API** - Modern ``add_column()`` and ``add_row()`` interface
* ✅ **Traditional API** - Compatible with classic table libraries
* ✅ **Rich markup support** - Use ``[color]text[/]`` in headers and cells
* ✅ **Column styling** - Set colors and styles per column
* ✅ **Row styling** - Set colors and styles per row
* ✅ **Flexible alignment** - Left, center, right alignment (horizontal and vertical)
* ✅ **Data type formatting** - Auto-format numbers, floats, exponential, integers
* ✅ **All make_colors formats** - Abbreviations, full names, attributes, backgrounds
* ✅ **Border customization** - Control borders, lines, and decorations
* ✅ **Width control** - Set fixed widths or auto-calculate

Table Class
===========

.. class:: Table(max_width=80, title=None, title_style=None, header_style=None)

   Create a new table instance.

   :param int max_width: Maximum width of the table. Set to 0 for unlimited width.
   :param str title: Optional table title displayed above the table.
   :param str title_style: Color style for the title (e.g., "bold cyan", "bold-cyan").
   :param str header_style: Color style for the header row (e.g., "bold white").

   **Example:**

   .. code-block:: python

       table = Table(
           max_width=100,
           title="Sales Report",
           title_style="bold magenta",
           header_style="bold white"
       )

Constants
---------

.. attribute:: Table.BORDER

   Flag to enable table border.

.. attribute:: Table.HEADER

   Flag to enable header separator line.

.. attribute:: Table.HLINES

   Flag to enable horizontal lines between rows.

.. attribute:: Table.VLINES

   Flag to enable vertical lines between columns.

Rich-style API
==============

add_column()
------------

.. method:: Table.add_column(header, style=None, align="l", valign="t", dtype="a", width=None)

   Add a column definition (Rich-style API).

   :param str header: Column header text. Supports Rich markup format.
   :param str style: Color style for this column using make_colors format.
   :param str align: Horizontal alignment: ``"l"`` (left), ``"c"`` (center), ``"r"`` (right).
   :param str valign: Vertical alignment: ``"t"`` (top), ``"m"`` (middle), ``"b"`` (bottom).
   :param str dtype: Data type: ``"a"`` (auto), ``"t"`` (text), ``"f"`` (float), ``"e"`` (exponential), ``"i"`` (integer).
   :param int width: Fixed width for this column.

   **Examples:**

   .. code-block:: python

       # Basic column
       table.add_column("Name", style="bold", align="l")
       
       # With data type
       table.add_column("Price", style="green", align="r", dtype="f")
       
       # Rich markup in header
       table.add_column("[white on blue]Status[/]", align="c")
       
       # With fixed width
       table.add_column("Description", width=30)

   **Supported Styles:**

   - Full names: ``"red"``, ``"blue"``, ``"green"``
   - Abbreviations: ``"r"``, ``"bl"``, ``"g"``
   - With attributes: ``"bold-red"``, ``"italic-cyan"``
   - With background: ``"white-red"``, ``"red-yellow"``
   - Rich markup: ``"[bold white on blue]Header[/]"``

add_row()
---------

.. method:: Table.add_row(*args, style=None)

   Add a data row (Rich-style API).

   :param args: Values for each column.
   :param str style: Color style for this entire row.
   :raises ArraySizeError: If number of values doesn't match column count.

   **Examples:**

   .. code-block:: python

       # Basic row
       table.add_row("Item 1", "100", "Active")
       
       # With row styling
       table.add_row("Item 2", "200", "Error", style="bold red")
       
       # With abbreviations
       table.add_row("Item 3", "150", "Warning", style="y")

Traditional API
===============

header()
--------

.. method:: Table.header(array)

   Set table header (Traditional API).

   :param list array: List of header strings.

   **Example:**

   .. code-block:: python

       table.header(["Name", "Age", "City"])

set_cols_align()
----------------

.. method:: Table.set_cols_align(array)

   Set column alignments.

   :param list array: List of alignment values (``"l"``, ``"c"``, ``"r"``) for each column.

   **Example:**

   .. code-block:: python

       table.set_cols_align(["l", "c", "r"])

set_cols_valign()
-----------------

.. method:: Table.set_cols_valign(array)

   Set column vertical alignments.

   :param list array: List of vertical alignment values (``"t"``, ``"m"``, ``"b"``).

   **Example:**

   .. code-block:: python

       table.set_cols_valign(["t", "m", "b"])

set_cols_dtype()
----------------

.. method:: Table.set_cols_dtype(array)

   Set column data types.

   :param list array: List of data type values (``"a"``, ``"t"``, ``"f"``, ``"e"``, ``"i"``).

   **Example:**

   .. code-block:: python

       table.set_cols_dtype(["t", "f", "i", "a"])

set_cols_width()
----------------

.. method:: Table.set_cols_width(array)

   Set column widths.

   :param list array: List of integer width values for each column.

   **Example:**

   .. code-block:: python

       table.set_cols_width([20, 10, 15])

set_cols_color()
----------------

.. method:: Table.set_cols_color(array)

   Set column colors (Traditional API). 🆕

   Supports both full color names and make_colors abbreviations.

   :param list array: List of color specifications for each column.

   **Supported Formats:**

   - Full names: ``"red"``, ``"blue"``, ``"green"``, ``"yellow"``
   - Abbreviations: ``"r"``, ``"bl"``, ``"g"``, ``"y"``, ``"lb"``, ``"lr"``
   - With background: ``"red-yellow"``, ``"r-y"``, ``"white on blue"``
   - With attributes: ``"bold-red"``, ``"italic-blue"``

   **Examples:**

   .. code-block:: python

       # Using abbreviations
       table.set_cols_color(["y", "r", "c"])  # yellow, red, cyan
       
       # Using full names
       table.set_cols_color(["blue", "magenta", "green"])
       
       # With attributes
       table.set_cols_color(["bold-red", "italic-cyan", "yellow-black"])

set_rows_color()
----------------

.. method:: Table.set_rows_color(array)

   Set row colors (Traditional API). 🆕

   Allows setting different colors for each row.

   :param list array: List of color specifications for each row. Use ``None`` to skip coloring a specific row.

   **Examples:**

   .. code-block:: python

       # Color all rows
       table.set_rows_color(["green", "yellow", "red", None])
       
       # With attributes
       table.set_rows_color(["bold-white", "dim-cyan", "bold-red"])
       
       # Alternating colors (zebra striping)
       table.set_rows_color(["dim", None, "dim", None, "dim"])

set_precision()
---------------

.. method:: Table.set_precision(width)

   Set decimal precision for float formatting.

   :param int width: Number of decimal places (must be >= 0).

   **Example:**

   .. code-block:: python

       table.set_precision(2)  # Show 2 decimal places

set_deco()
----------

.. method:: Table.set_deco(deco)

   Set the table decoration flags.

   :param int deco: Combination of ``BORDER``, ``HEADER``, ``HLINES``, ``VLINES`` flags.

   **Examples:**

   .. code-block:: python

       # Only border and header
       table.set_deco(Table.BORDER | Table.HEADER)
       
       # All decorations (default)
       table.set_deco(Table.BORDER | Table.HEADER | Table.HLINES | Table.VLINES)
       
       # No decorations
       table.set_deco(0)

set_chars()
-----------

.. method:: Table.set_chars(array)

   Set the characters used to draw table lines.

   :param list array: List of 4 characters ``[horizontal, vertical, corner, header]``.

   **Example:**

   .. code-block:: python

       # Default
       table.set_chars(['-', '|', '+', '='])
       
       # Custom style
       table.set_chars(['─', '│', '┼', '═'])

draw()
------

.. method:: Table.draw()

   Generate and return the formatted table as a string.

   :returns: The complete formatted table with all decorations and colors.
   :rtype: str

   **Example:**

   .. code-block:: python

       output = table.draw()
       print(output)
       
       # Or directly
       print(table.draw())

reset()
-------

.. method:: Table.reset()

   Reset the table instance, clearing all data.

   **Example:**

   .. code-block:: python

       table.reset()
       # Table is now empty and ready for new data

Examples
========

Example 1: Package Version Checker
-----------------------------------

.. code-block:: python

    from make_colors.table import Table

    table = Table(title="Package Version Checker", title_style="bold cyan")
    table.add_column("Package", style="bold")
    table.add_column("Installed", style="cyan")
    table.add_column("Required", style="magenta")
    table.add_column("Status", style="yellow")

    table.add_row("numpy", "1.21.0", "1.20.0", "✓ OK")
    table.add_row("pandas", "1.3.0", "1.4.0", "⚠ Update", style="bold yellow")
    table.add_row("requests", "2.26.0", "2.26.0", "✓ OK")
    table.add_row("flask", "1.1.0", "2.0.0", "✗ Old", style="bold red")

    print(table.draw())

Example 2: System Monitor with Column Colors
---------------------------------------------

.. code-block:: python

    from make_colors.table import Table

    table = Table()
    table.set_cols_align(["l", "c", "r", "r"])
    table.set_cols_color(["bold-white", "cyan", "yellow", "magenta"])
    table.header(["Service", "Status", "CPU %", "Memory %"])

    table.add_row("Web Server", "✓ Running", "45.2", "62.8")
    table.add_row("Database", "✓ Running", "78.5", "85.3")
    table.add_row("Cache", "⚠ Warning", "92.1", "95.7")

    print(table.draw())

Example 3: Status-based Row Coloring
-------------------------------------

.. code-block:: python

    from make_colors.table import Table

    table = Table(title="Task Status", title_style="bold-cyan")
    table.header(["Task", "Status", "Progress", "Priority"])

    table.add_row("Deploy to Production", "✓ Complete", "100%", "High")
    table.add_row("Code Review", "⚠ In Progress", "75%", "Medium")
    table.add_row("Write Tests", "● Pending", "0%", "High")
    table.add_row("Fix Bug #123", "✗ Blocked", "30%", "Critical")

    # Color rows based on status
    table.set_rows_color([
        "bold-green",    # Complete
        "bold-yellow",   # In Progress
        "dim",           # Pending
        "bold-red"       # Blocked
    ])

    print(table.draw())

Example 4: Rich Markup Headers
-------------------------------

.. code-block:: python

    from make_colors.table import Table

    table = Table(title="[bold magenta]Sales Dashboard[/]")
    table.add_column("[bold white]Product[/]", align="l")
    table.add_column("[bold green]Revenue[/]", align="r", dtype="f")
    table.add_column("[white on blue]Units Sold[/]", align="r", dtype="i")
    table.add_column("[bold yellow on black]Trend[/]", align="c")

    table.add_row("Widget A", 125000.50, 1234, "📈 Up")
    table.add_row("Widget B", 89000.25, 890, "📉 Down", style="dim")
    table.add_row("Widget C", 250000.00, 2500, "🔥 Hot", style="bold-green")

    print(table.draw())

Example 5: Alternating Row Colors (Zebra Striping)
---------------------------------------------------

.. code-block:: python

    from make_colors.table import Table

    table = Table(title="User List", title_style="bold-cyan")
    table.header(["ID", "Username", "Email", "Status"])

    users = [
        ["001", "john_doe", "john@example.com", "Active"],
        ["002", "jane_smith", "jane@example.com", "Active"],
        ["003", "bob_wilson", "bob@example.com", "Inactive"],
        ["004", "alice_brown", "alice@example.com", "Active"],
        ["005", "charlie_davis", "charlie@example.com", "Active"],
    ]

    for user in users:
        table.add_row(*user)

    # Alternate between dim and normal
    table.set_rows_color(["dim", None, "dim", None, "dim"])

    print(table.draw())

Example 6: Financial Report
----------------------------

.. code-block:: python

    from make_colors.table import Table

    table = Table(title="Q4 Financial Report", title_style="bold cyan")
    table.add_column("Category", style="bold-white", align="l")
    table.add_column("Revenue", style="green", align="r", dtype="f")
    table.add_column("Expenses", style="red", align="r", dtype="f")
    table.add_column("Profit", style="yellow", align="r", dtype="f")

    table.add_row("Sales", 500000.00, 200000.00, 300000.00)
    table.add_row("Services", 250000.00, 100000.00, 150000.00)
    table.add_row("Products", 350000.00, 180000.00, 170000.00)
    table.add_row("Total", 1100000.00, 480000.00, 620000.00, style="bold-green")

    table.set_precision(2)
    print(table.draw())

Rich Markup Support
===================

Tables support Rich markup in multiple places:

In Titles
---------

.. code-block:: python

    table = Table(title="[bold cyan]My Report[/]")

In Column Headers
-----------------

.. code-block:: python

    table.add_column("[bold white]Name[/]")
    table.add_column("[white on blue]Status[/]")
    table.add_column("[bold green]Revenue[/]")

In Cells
--------

.. code-block:: python

    table.add_row("[bold]Important[/]", "Data", "100")

Supported Rich Markup Formats
------------------------------

- **Color only**: ``[red]text[/]``, ``[blue]text[/]``
- **Attribute + Color**: ``[bold red]text[/]``, ``[italic cyan]text[/]``
- **Color + Background**: ``[white on blue]text[/]``, ``[red on yellow]text[/]``
- **All combined**: ``[bold white on blue]text[/]``

Color Format Support
====================

All make_colors formats are supported in tables:

Full Color Names
----------------

.. code-block:: python

    table.set_cols_color(["red", "green", "blue"])

Abbreviations
-------------

.. code-block:: python

    table.set_cols_color(["r", "g", "bl"])
    table.set_cols_color(["y", "c", "m"])  # yellow, cyan, magenta
    table.set_cols_color(["lb", "lr", "lg"])  # light variants

With Attributes
---------------

.. code-block:: python

    table.set_cols_color(["bold-red", "italic-cyan", "dim-yellow"])
    table.add_row(..., style="bold-green")

With Background
---------------

.. code-block:: python

    table.set_cols_color(["white-red", "black-yellow", "green-black"])
    table.add_column("Status", style="white-blue")

Mixed Formats
-------------

.. code-block:: python

    table.set_cols_color(["bold-white", "r", "italic-cyan", "lb-b"])

Styling Options
===============

Alignment
---------

Horizontal Alignment
~~~~~~~~~~~~~~~~~~~~

- ``"l"`` - Left align (default)
- ``"c"`` - Center align
- ``"r"`` - Right align

.. code-block:: python

    table.set_cols_align(["l", "c", "r"])

Vertical Alignment
~~~~~~~~~~~~~~~~~~

- ``"t"`` - Top align (default)
- ``"m"`` - Middle align
- ``"b"`` - Bottom align

.. code-block:: python

    table.set_cols_valign(["t", "m", "b"])

Data Types
----------

- ``"a"`` - Auto (default) - Automatically detect data type
- ``"t"`` - Text - Treat as text
- ``"f"`` - Float - Format as decimal number
- ``"e"`` - Exponential - Format in scientific notation
- ``"i"`` - Integer - Format as integer

.. code-block:: python

    table.set_cols_dtype(["t", "f", "i", "a"])

Border Styles
-------------

Default Style
~~~~~~~~~~~~~

.. code-block:: python

    table.set_chars(['-', '|', '+', '='])

Output:

.. code-block:: text

    +------+------+
    | Col1 | Col2 |
    +======+======+
    | Data | Data |
    +------+------+

Decoration Control
~~~~~~~~~~~~~~~~~~

.. code-block:: python

    # Full decorations (default)
    table.set_deco(Table.BORDER | Table.HEADER | Table.HLINES | Table.VLINES)
    
    # Only border and header
    table.set_deco(Table.BORDER | Table.HEADER)
    
    # No vertical lines
    table.set_deco(Table.BORDER | Table.HEADER | Table.HLINES)
    
    # Minimal (no decorations)
    table.set_deco(0)

Best Practices
==============

1. **Choose appropriate data types**

   .. code-block:: python

       # For numbers, use float or int types
       table.set_cols_dtype(["t", "f", "i"])  # text, float, integer

2. **Use consistent alignment**

   .. code-block:: python

       # Text left, numbers right
       table.set_cols_align(["l", "r", "r"])

3. **Color for meaning**

   .. code-block:: python

       # Use colors to indicate status
       if status == "error":
           table.add_row(..., style="bold-red")
       elif status == "warning":
           table.add_row(..., style="yellow")
       else:
           table.add_row(..., style="green")

4. **Keep it readable**

   .. code-block:: python

       # Don't over-use colors
       # Choose contrasting colors
       # Use dim for less important rows

5. **Use zebra striping for long tables**

   .. code-block:: python

       colors = ["dim" if i % 2 else None for i in range(len(rows))]
       table.set_rows_color(colors)

Exceptions
==========

.. exception:: ArraySizeError

   Raised when specified rows don't fit the required size.

   **Example:**

   .. code-block:: python

       try:
           table.add_row("Value1", "Value2")  # But table has 3 columns
       except ArraySizeError as e:
           print(f"Error: {e}")

Performance Tips
================

1. **Reuse tables when possible**

   .. code-block:: python

       table = Table()
       # ... setup ...
       for data in datasets:
           table.reset()
           # ... add data ...
           print(table.draw())

2. **Set widths explicitly for large datasets**

   .. code-block:: python

       # Prevents recalculation
       table.set_cols_width([20, 15, 10])

3. **Use unlimited width for wide tables**

   .. code-block:: python

       table = Table(max_width=0)  # No width limit

Compatibility
=============

The Table module is designed to be compatible with:

- **Python 2.7+** and **Python 3.x**
- **Windows 10+**, **Linux**, **macOS**
- All terminals that support ANSI escape codes
- Works with make_colors color detection

.. code-block:: python

    from make_colors import MakeColors
    from make_colors.table import Table

    if MakeColors.supports_color():
        # Use colored tables
        table = Table(title_style="bold cyan")
    else:
        # Fallback to plain tables
        table = Table()

See Also
========

* :doc:`index` - Main make_colors documentation
* :doc:`api/main_functions` - Complete API reference
* :doc:`examples` - More examples and use cases

.. note::
   The Table module integrates seamlessly with make_colors. All color formats,
   abbreviations, and Rich markup supported by make_colors work in tables.

.. tip::
   For status monitoring, use ``set_rows_color()`` to dynamically color rows
   based on their status. This makes it easy to spot issues at a glance.

.. warning::
   Very wide tables (many columns or large widths) may not display well on
   narrow terminals. Consider setting ``max_width`` appropriately or using
   vertical layouts for such data.