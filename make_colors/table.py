#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
table.py - Rich-style Table Class with make_colors integration

A comprehensive table formatting module that provides rich-style table output
with support for ANSI colors via make_colors integration.

Usage:
    from make_colors.table import Table
    
    table = Table(title="My Table", title_style="bold cyan")
    table.add_column("Name", style="bold")
    table.add_column("Status", style="green")
    table.add_row("Item 1", "OK")
    print(table.draw())
"""

import sys
import re
from functools import reduce

try:
    import textwrap
except ImportError:
    sys.stderr.write("Can't import textwrap module!\n")
    raise

# Import make_colors from parent package
try:
    from .make_colors import make_colors, parse_rich_markup
    HAS_MAKE_COLORS = True
except ImportError:
    try:
        from make_colors import make_colors, parse_rich_markup
        HAS_MAKE_COLORS = True
    except ImportError:
        HAS_MAKE_COLORS = False
        # Fallback ANSI color codes
        ANSI_COLORS = {
            'black': '\033[30m', 'red': '\033[31m', 'green': '\033[32m',
            'yellow': '\033[33m', 'blue': '\033[34m', 'magenta': '\033[35m',
            'cyan': '\033[36m', 'white': '\033[37m', 'lightblack': '\033[90m',
            'lightred': '\033[91m', 'lightgreen': '\033[92m', 'lightyellow': '\033[93m',
            'lightblue': '\033[94m', 'lightmagenta': '\033[95m', 'lightcyan': '\033[96m',
            'lightwhite': '\033[97m', 'bold': '\033[1m', 'dim': '\033[2m',
            'italic': '\033[3m', 'underline': '\033[4m', 'reset': '\033[0m'
        }
        
        def make_colors(text, fg='white', bg=None, attrs=[], force=False):
            """Fallback color function if make_colors is not available"""
            if not force and not sys.stdout.isatty():
                return text
            
            codes = []
            if isinstance(attrs, list):
                for attr in attrs:
                    if attr in ANSI_COLORS:
                        codes.append(ANSI_COLORS[attr])
            
            if fg in ANSI_COLORS:
                codes.append(ANSI_COLORS[fg])
            
            if codes:
                return ''.join(codes) + text + ANSI_COLORS['reset']
            return text
        
        def parse_rich_markup(text):
            """Fallback parse_rich_markup if not available"""
            return [(text, None, None, None)]


class ArraySizeError(Exception):
    """Exception raised when specified rows don't fit the required size"""

    def __init__(self, msg):
        self.msg = msg
        Exception.__init__(self, msg, '')

    def __str__(self):
        return self.msg


class Table:
    """A Rich-style table class with make_colors integration.
    
    This class provides comprehensive table formatting with support for:
    - Customizable borders and separators
    - Column alignment and width control
    - Color styling via make_colors
    - Rich-style API (add_column, add_row)
    - Traditional API (header, add_row with arrays)
    
    Example:
        >>> from make_colors.table import Table
        >>> 
        >>> # Rich-style usage
        >>> table = Table(title="Package Info", title_style="bold cyan")
        >>> table.add_column("Name", style="bold")
        >>> table.add_column("Version", style="green")
        >>> table.add_column("Status", style="yellow")
        >>> 
        >>> table.add_row("numpy", "1.21.0", "✓ OK")
        >>> table.add_row("pandas", "1.3.0", "⚠ Update", style="bold yellow")
        >>> 
        >>> print(table.draw())
    
    Attributes:
        BORDER: Flag for table border
        HEADER: Flag for header separator line
        HLINES: Flag for horizontal lines between rows
        VLINES: Flag for vertical lines between columns
    """

    BORDER = 1
    HEADER = 1 << 1
    HLINES = 1 << 2
    VLINES = 1 << 3

    def __init__(self, max_width=80, title=None, title_style=None, header_style=None):
        """Initialize a new Table instance.
        
        Args:
            max_width (int): Maximum width of the table (0 for unlimited).
                           Defaults to 80.
            title (str, optional): Table title displayed above the table.
            title_style (str, optional): Color style for title.
                                        Examples: "bold cyan", "bold-cyan"
            header_style (str, optional): Color style for header row.
                                         Examples: "bold white", "bold-white"
        """
        self._max_width = max_width if max_width > 0 else False
        self._precision = 3
        self._title = title
        self._title_style = title_style
        self._header_style = header_style
        
        self._deco = Table.VLINES | Table.HLINES | Table.BORDER | Table.HEADER
        self.set_chars(['-', '|', '+', '='])
        
        self._columns = []
        self._column_count = 0
        
        self.reset()

    def reset(self):
        """Reset the table instance, clearing all data."""
        self._hline_string = None
        self._row_size = None
        self._header = []
        self._rows = []
        self._row_styles = []

    def set_chars(self, array):
        """Set the characters used to draw table lines.
        
        Args:
            array (list): List of 4 characters [horizontal, vertical, corner, header].
                         Example: ['-', '|', '+', '=']
        
        Raises:
            ArraySizeError: If array doesn't contain exactly 4 elements.
        """
        if len(array) != 4:
            raise ArraySizeError("array should contain 4 characters")
        array = [x[:1] for x in [str(s) for s in array]]
        (self._char_horiz, self._char_vert,
            self._char_corner, self._char_header) = array

    def set_deco(self, deco):
        """Set the table decoration flags.
        
        Args:
            deco (int): Combination of BORDER, HEADER, HLINES, VLINES flags.
                       Example: Table.BORDER | Table.HEADER
        """
        self._deco = deco

    def add_column(self, header, style=None, align="l", valign="t", dtype="a", width=None):
        """Add a column definition (Rich-style API).
        
        Args:
            header (str): Column header text. Supports Rich markup format.
                         Examples: "Name", "[white on blue]Status[/]", "[bold red]Error[/]"
            style (str, optional): Color style for this column using make_colors format.
                                  Examples: "bold", "cyan", "bold red", "bold-red"
                                  Note: If header contains Rich markup, style parameter is ignored.
            align (str): Horizontal alignment - "l" (left), "c" (center), "r" (right).
                        Defaults to "l".
            valign (str): Vertical alignment - "t" (top), "m" (middle), "b" (bottom).
                         Defaults to "t".
            dtype (str): Data type - "a" (auto), "t" (text), "f" (float), 
                        "e" (exponential), "i" (integer). Defaults to "a".
            width (int, optional): Fixed width for this column.
        
        Example:
            >>> table.add_column("Name", style="bold", align="l")
            >>> table.add_column("Value", style="cyan", align="r", dtype="f")
            >>> table.add_column("[white on blue]Status[/]")  # Rich markup (uses make_colors parser)
            >>> table.add_column("[bold red]Error Count[/]", align="r")
        """
        self._columns.append({
            'header': header,
            'style': style,
            'align': align,
            'valign': valign,
            'dtype': dtype,
            'width': width
        })
        self._column_count += 1
        
        self._header.append(header)
        
        if not hasattr(self, '_align'):
            self._align = []
            self._valign = []
            self._dtype = []
            self._width = []
            self._col_styles = []
        
        self._align.append(align)
        self._valign.append(valign)
        self._dtype.append(dtype)
        self._col_styles.append(style)
        if width:
            self._width.append(width)
        
        self._row_size = self._column_count

    def add_row(self, *args, style=None):
        """Add a data row (Rich-style API).
        
        Args:
            *args: Values for each column.
            style (str, optional): Color style for this entire row.
                                  Examples: "bold green", "bold-green", "red-yellow"
        
        Raises:
            ArraySizeError: If number of values doesn't match column count.
        
        Example:
            >>> table.add_row("Item 1", "100", "Active")
            >>> table.add_row("Item 2", "200", "Error", style="bold red")
        """
        array = list(args)
        
        if self._column_count > 0 and len(array) != self._column_count:
            raise ArraySizeError(f"Row should contain {self._column_count} elements")
        
        if not hasattr(self, "_dtype"):
            self._dtype = ["a"] * len(array)
        
        cells = []
        for i, x in enumerate(array):
            cells.append(self._str(i, x))
        
        self._rows.append(cells)
        self._row_styles.append(style)

    def set_cols_align(self, array):
        """Set column alignments (Traditional API).
        
        Args:
            array (list): List of alignment values ("l", "c", "r") for each column.
        """
        self._check_row_size(array)
        self._align = array

    def set_cols_valign(self, array):
        """Set column vertical alignments (Traditional API).
        
        Args:
            array (list): List of vertical alignment values ("t", "m", "b").
        """
        self._check_row_size(array)
        self._valign = array

    def set_cols_dtype(self, array):
        """Set column data types (Traditional API).
        
        Args:
            array (list): List of data type values ("a", "t", "f", "e", "i").
        """
        self._check_row_size(array)
        self._dtype = array

    def set_cols_width(self, array):
        """Set column widths (Traditional API).
        
        Args:
            array (list): List of integer width values for each column.
        """
        self._check_row_size(array)
        try:
            array = list(map(int, array))
            if reduce(min, array) <= 0:
                raise ValueError
        except ValueError:
            sys.stderr.write("Wrong argument in column width specification\n")
            raise
        self._width = array

    def set_cols_color(self, array):
        """Set column colors (Traditional API).
        
        Supports both full color names and make_colors abbreviations.
        
        Args:
            array (list): List of color specifications for each column.
                         Supports:
                         - Full names: "red", "blue", "green", "yellow", etc.
                         - Abbreviations: "r", "bl", "g", "y", "lb", "lr", etc.
                         - With background: "red-yellow", "r-y", "white on blue"
                         - With attributes: "bold-red", "italic-blue"
        
        Example:
            >>> table.set_cols_color(["y", "r", "c"])  # yellow, red, cyan
            >>> table.set_cols_color(["blue", "magenta", "green"])
            >>> table.set_cols_color(["bold-red", "italic-cyan", "yellow-black"])
        """
        self._check_row_size(array)
        self._col_styles = array

    def set_rows_color(self, array):
        """Set row colors (Traditional API).
        
        Allows setting different colors for each row.
        
        Args:
            array (list): List of color specifications for each row.
                         Same format as set_cols_color().
                         Use None to skip coloring a specific row.
        
        Example:
            >>> table.set_rows_color(["green", "yellow", "red", None])
            >>> table.set_rows_color(["bold-white", "dim-cyan", "bold-red"])
        """
        # Extend array if needed to match current rows
        while len(self._row_styles) < len(array):
            self._row_styles.append(None)
        
        # Update row styles
        for i, color in enumerate(array):
            if i < len(self._row_styles):
                self._row_styles[i] = color

    def set_precision(self, width):
        """Set decimal precision for float formatting.
        
        Args:
            width (int): Number of decimal places (must be >= 0).
        """
        if not type(width) is int or width < 0:
            raise ValueError('width must be an integer greater than 0')
        self._precision = width

    def header(self, array):
        """Set table header (Traditional API).
        
        Args:
            array (list): List of header strings.
        """
        self._check_row_size(array)
        self._header = list(map(str, array))

    def draw(self):
        """Generate and return the formatted table as a string.
        
        Returns:
            str: The complete formatted table with all decorations and colors.
        
        Example:
            >>> table = Table()
            >>> table.add_column("Name")
            >>> table.add_row("Alice")
            >>> print(table.draw())
        """
        if not self._header and not self._rows:
            return ""
        
        self._compute_cols_width()
        self._check_align()
        
        out = ""
        
        # Draw title if exists
        if self._title:
            out += self._draw_title()
        
        # Draw top border
        if self._has_border():
            out += self._hline()
        
        # Draw header (only once!)
        if self._header:
            out += self._draw_line(self._header, isheader=True, style=self._header_style)
            if self._has_header():
                out += self._hline_header()
        
        # Draw rows
        for idx, row in enumerate(self._rows):
            row_style = self._row_styles[idx] if idx < len(self._row_styles) else None
            out += self._draw_line(row, row_style=row_style)
            if self._has_hlines() and idx < len(self._rows) - 1:
                out += self._hline()
        
        # Draw bottom border
        if self._has_border():
            out += self._hline()
        
        return out[:-1]

    def _draw_title(self):
        """Draw table title with styling."""
        if not self._title:
            return ""
        
        # Calculate total width
        total_width = sum(self._width) + len(self._width) * 3 + 1
        title_text = self._title
        
        # Check if title has Rich markup
        if '[' in title_text and ']' in title_text and '[/' in title_text:
            # Let make_colors handle Rich markup
            title_text = make_colors(title_text)
        elif self._title_style:
            # Apply style parameter
            title_text = self._apply_style(title_text, self._title_style)
        
        # Center the title (use original title for length calculation)
        title_length = self._len_cell(self._title)
        padding = (total_width - title_length) // 2
        line = " " * padding + title_text + "\n"
        
        return line

    def _apply_style(self, text, style):
        """Apply color/style to text using make_colors.
        
        This leverages make_colors' built-in support for Rich markup and various style formats.
        
        Args:
            text (str): Text to style.
            style (str): Style specification or None.
        
        Returns:
            str: Styled text with ANSI codes.
        """
        if not style or not text:
            return text
        
        # Let make_colors handle all the parsing
        # It already supports:
        # - "bold red" (space-separated)
        # - "bold-red" (hyphen-separated)
        # - "bold_red" (underscore-separated)
        # - "red-yellow" (fg-bg)
        # - Rich markup "[color]text[/]"
        return make_colors(text, style)

    def _str(self, i, x):
        """Format cell data based on data type."""
        try:
            f = float(x)
        except:
            return str(x)

        n = self._precision
        dtype = self._dtype[i]

        if dtype == 'i':
            return str(int(round(f)))
        elif dtype == 'f':
            return '%.*f' % (n, f)
        elif dtype == 'e':
            return '%.*e' % (n, f)
        elif dtype == 't':
            return str(x)
        else:
            if f - round(f) == 0:
                if abs(f) > 1e8:
                    return '%.*e' % (n, f)
                else:
                    return str(int(round(f)))
            else:
                if abs(f) > 1e8:
                    return '%.*e' % (n, f)
                else:
                    return '%.*f' % (n, f)

    def _check_row_size(self, array):
        """Check if array size matches expected column count."""
        if not self._row_size:
            self._row_size = len(array)
        elif self._row_size != len(array):
            raise ArraySizeError(f"array should contain {self._row_size} elements")

    def _has_vlines(self):
        """Check if vertical lines should be drawn."""
        return self._deco & Table.VLINES > 0

    def _has_hlines(self):
        """Check if horizontal lines should be drawn."""
        return self._deco & Table.HLINES > 0

    def _has_border(self):
        """Check if border should be drawn."""
        return self._deco & Table.BORDER > 0

    def _has_header(self):
        """Check if header separator should be drawn."""
        return self._deco & Table.HEADER > 0

    def _hline_header(self):
        """Generate header separator line."""
        return self._build_hline(True)

    def _hline(self):
        """Generate horizontal separator line."""
        if not self._hline_string:
            self._hline_string = self._build_hline()
        return self._hline_string

    def _build_hline(self, is_header=False):
        """Build horizontal line string."""
        horiz = self._char_horiz
        if is_header:
            horiz = self._char_header
        s = "%s%s%s" % (horiz, [horiz, self._char_corner][self._has_vlines()], horiz)
        l = s.join([horiz * n for n in self._width])
        if self._has_border():
            l = "%s%s%s%s%s\n" % (self._char_corner, horiz, l, horiz, self._char_corner)
        else:
            l += "\n"
        return l

    def _len_cell(self, cell):
        """Calculate cell width, accounting for ANSI codes and Rich markup.
        
        Uses regex to strip both ANSI codes and Rich markup tags.
        """
        # Remove ANSI codes
        ansi_escape = re.compile(r'\033\[[0-9;]*m')
        # Remove Rich markup tags [xxx]...[/]
        rich_markup = re.compile(r'\[([^\]]+)\]')
        # Remove closing tag [/]
        rich_close = re.compile(r'\[/\]')
        
        clean_cell = str(cell)
        
        # Remove Rich markup tags
        clean_cell = rich_markup.sub('', clean_cell)
        clean_cell = rich_close.sub('', clean_cell)
        
        # Remove ANSI codes
        clean_cell = ansi_escape.sub('', clean_cell)
        
        cell_lines = clean_cell.split('\n')
        maxi = 0
        for line in cell_lines:
            length = 0
            parts = line.split('\t')
            for part, i in zip(parts, list(range(1, len(parts) + 1))):
                length = length + len(part)
                if i < len(parts):
                    length = (length // 8 + 1) * 8
            maxi = max(maxi, length)
        return maxi

    def _compute_cols_width(self):
        """Calculate column widths based on content."""
        if hasattr(self, "_width") and len(self._width) == self._row_size:
            return
        
        maxi = []
        if self._header:
            maxi = [self._len_cell(x) for x in self._header]
        
        for row in self._rows:
            for cell, i in zip(row, list(range(len(row)))):
                try:
                    maxi[i] = max(maxi[i], self._len_cell(cell))
                except (TypeError, IndexError):
                    maxi.append(self._len_cell(cell))
        
        items = len(maxi)
        length = reduce(lambda x, y: x + y, maxi)
        
        if self._max_width and length + items * 3 + 1 > self._max_width:
            maxi = [(self._max_width - items * 3 - 1) // items for n in range(items)]
        
        self._width = maxi

    def _check_align(self):
        """Initialize alignment settings if not set."""
        if not hasattr(self, "_align"):
            self._align = ["l"] * self._row_size
        if not hasattr(self, "_valign"):
            self._valign = ["t"] * self._row_size
        if not hasattr(self, "_col_styles"):
            self._col_styles = [None] * self._row_size

    def _draw_line(self, line, isheader=False, style=None, row_style=None):
        """Draw a single table line/row.
        
        Uses make_colors for all styling, including Rich markup support.
        """
        line = self._splitit(line, isheader)
        space = " "
        out = ""
        
        for i in range(len(line[0])):
            if self._has_border():
                out += "%s " % self._char_vert
            
            for idx, (cell, width, align) in enumerate(zip(line, self._width, self._align)):
                cell_line = cell[i]
                
                # Apply styling
                if not isheader:
                    # For data rows
                    if row_style:
                        # Row-level style takes precedence
                        cell_line = self._apply_style(cell_line, row_style)
                    elif self._col_styles[idx]:
                        # Column-level style
                        cell_line = self._apply_style(cell_line, self._col_styles[idx])
                else:
                    # For header row
                    # Get the original header text
                    original_header = self._header[idx] if idx < len(self._header) else cell_line
                    
                    # Check if the original header has Rich markup
                    if '[' in str(original_header) and ']' in str(original_header) and '[/' in str(original_header):
                        # Apply Rich markup to the current cell line (clean text from splitit)
                        # Extract markup and apply to clean text
                        rich_pattern = re.compile(r'\[([^\]]+)\](.*?)\[/\]')
                        match = rich_pattern.search(str(original_header))
                        if match:
                            markup = match.group(1)
                            # Apply the markup to the clean cell_line
                            cell_line = make_colors(f"[{markup}]{cell_line}[/]")
                    elif style:
                        # Use general header style only if no Rich markup
                        cell_line = self._apply_style(cell_line, style)
                
                fill = width - self._len_cell(cell[i])
                
                if isheader:
                    align = "c"
                
                if align == "r":
                    out += "%s " % (fill * space + cell_line)
                elif align == "c":
                    out += "%s " % (int(fill/2) * space + cell_line + int(fill/2 + fill%2) * space)
                else:
                    out += "%s " % (cell_line + fill * space)
                
                if idx < len(line) - 1:
                    out += "%s " % [space, self._char_vert][self._has_vlines()]
            
            out += "%s\n" % ['', self._char_vert][self._has_border()]
        
        return out

    def _splitit(self, line, isheader):
        """Split cells to fit column width."""
        line_wrapped = []
        for idx, (cell, width) in enumerate(zip(line, self._width)):
            array = []
            # Remove ANSI codes for wrapping calculation
            ansi_escape = re.compile(r'\033\[[0-9;]*m')
            
            cell_str = str(cell)
            
            # Check if this is a header with Rich markup that needs processing
            if isheader and '[' in cell_str and ']' in cell_str and '[/' in cell_str:
                # Process Rich markup: extract clean text for wrapping
                # but keep the markup for later application
                rich_pattern = re.compile(r'\[([^\]]+)\](.*?)\[/\]')
                match = rich_pattern.search(cell_str)
                if match:
                    # Extract just the text content for wrapping
                    clean_text = match.group(2)
                    wrapped = textwrap.wrap(clean_text, width) if clean_text else [clean_text]
                    array.extend(wrapped)
                else:
                    # Fallback if pattern doesn't match
                    array.append(cell_str)
            else:
                # Normal cell processing
                for c in cell_str.split('\n'):
                    # Check if cell has ANSI codes
                    has_ansi = bool(ansi_escape.search(c))
                    if has_ansi:
                        # Extract ANSI codes and text
                        codes_list = ansi_escape.findall(c)
                        clean_text = ansi_escape.sub('', c)
                        wrapped = textwrap.wrap(clean_text, width) if clean_text else ['']
                        # Reapply ANSI codes to wrapped lines
                        reset = '\033[0m'
                        for line_text in wrapped:
                            styled_line = ''.join(codes_list) + line_text + reset
                            array.append(styled_line)
                    else:
                        wrapped = textwrap.wrap(c, width) if c else ['']
                        array.extend(wrapped)
            
            if not array:
                array = ['']
            line_wrapped.append(array)
        
        max_cell_lines = reduce(max, list(map(len, line_wrapped)))
        
        for cell, valign in zip(line_wrapped, self._valign):
            if isheader:
                valign = "t"
            if valign == "m":
                missing = max_cell_lines - len(cell)
                cell[:0] = [""] * int(missing / 2)
                cell.extend([""] * int(missing / 2 + missing % 2))
            elif valign == "b":
                cell[:0] = [""] * (max_cell_lines - len(cell))
            else:
                cell.extend([""] * (max_cell_lines - len(cell)))
        
        return line_wrapped


# Export main class
__all__ = ['Table', 'ArraySizeError']


if __name__ == '__main__':
    """Example usage and tests"""
    
    print("\n" + "="*70)
    print("Table Module - Using make_colors Rich Markup Support")
    print("="*70)
    
    # Example 1: Rich markup in headers (using make_colors parser)
    print("\nExample 1: Rich Markup in Column Headers")
    print("-" * 70)
    table = Table(title="[bold cyan]Package Version Checker[/]")
    table.add_column("[bold white]Package[/]")
    table.add_column("[cyan]Installed[/]")
    table.add_column("[magenta]Required[/]")
    table.add_column("[yellow]Status[/]")
    
    table.add_row("numpy", "1.21.0", "1.20.0", "✓ OK")
    table.add_row("pandas", "1.3.0", "1.4.0", "⚠ Update", style="bold yellow")
    table.add_row("requests", "2.26.0", "2.26.0", "✓ OK")
    table.add_row("flask", "1.1.0", "2.0.0", "✗ Old", style="bold red")
    
    print(table.draw())
    
    # Example 2: Using set_cols_color with abbreviations (NEW!)
    print("\n\nExample 2: Using set_cols_color() with Abbreviations (NEW!)")
    print("-" * 70)
    table2 = Table(max_width=0)
    table2.set_cols_align(["l", "r", "r", "c"])
    table2.set_cols_dtype(["t", "f", "i", "t"])
    table2.set_cols_color(["y", "r", "c", "g"])  # yellow, red, cyan, green
    table2.header(["Product", "Price", "Stock", "Status"])
    table2.add_row("Widget A", 125.50, 234, "✓ Available")
    table2.add_row("Widget B", 89.99, 0, "✗ Out of Stock")
    table2.add_row("Widget C", 250.00, 150, "✓ Available")
    
    print(table2.draw())
    
    # Example 3: Using set_cols_color with full names
    print("\n\nExample 3: Using set_cols_color() with Full Color Names")
    print("-" * 70)
    table3 = Table(max_width=0)
    table3.set_cols_align(["l", "c", "r", "r"])
    table3.set_cols_color(["blue", "magenta", "green", "yellow"])
    table3.header(["Service", "Status", "Uptime", "CPU %"])
    table3.add_row("Web Server", "✓ Running", "15d 6h", "45.2")
    table3.add_row("Database", "✓ Running", "15d 6h", "78.5")
    table3.add_row("Cache", "⚠ Warning", "2d 3h", "92.1")
    
    print(table3.draw())
    
    # Example 4: Using set_cols_color with attributes
    print("\n\nExample 4: set_cols_color() with Attributes")
    print("-" * 70)
    table4 = Table(max_width=0)
    table4.set_cols_align(["l", "r", "r", "c"])
    table4.set_cols_color(["bold-white", "bold-green", "bold-cyan", "bold-yellow"])
    table4.header(["Item", "Revenue", "Units", "Trend"])
    table4.add_row("Product A", "125000.50", "1234", "📈 Up")
    table4.add_row("Product B", "89000.25", "890", "📉 Down")
    table4.add_row("Product C", "250000.00", "2500", "🔥 Hot")
    
    print(table4.draw())
    
    # Example 5: Using set_rows_color (NEW!)
    print("\n\nExample 5: Using set_rows_color() (NEW!)")
    print("-" * 70)
    table5 = Table(max_width=0)
    table5.set_cols_align(["l", "c", "r"])
    table5.header(["Server", "Status", "Load"])
    table5.add_row("Server 1", "✓ OK", "Low")
    table5.add_row("Server 2", "⚠ Warning", "Medium")
    table5.add_row("Server 3", "✗ Critical", "High")
    table5.add_row("Server 4", "✓ OK", "Low")
    table5.set_rows_color(["green", "yellow", "bold-red", "green"])
    
    print(table5.draw())
    
    # Example 6: Combining set_cols_color and set_rows_color
    print("\n\nExample 6: Combining set_cols_color() and set_rows_color()")
    print("-" * 70)
    table6 = Table(max_width=0, title="Sales Dashboard", title_style="bold-cyan")
    table6.set_cols_align(["l", "r", "r", "c"])
    table6.set_cols_color(["bold-white", "green", "cyan", "yellow"])  # Column colors
    table6.header(["Region", "Sales", "Target", "Performance"])
    table6.add_row("North", "150000", "120000", "✓ Exceeded")
    table6.add_row("South", "95000", "100000", "⚠ Close")
    table6.add_row("East", "180000", "150000", "✓ Exceeded")
    table6.add_row("West", "75000", "100000", "✗ Below")
    table6.set_rows_color([None, "dim-yellow", None, "dim-red"])  # Row-specific colors
    
    print(table6.draw())
    
    # Example 7: Mixed approaches (Rich style + Traditional)
    print("\n\nExample 7: Mixed Rich-style and Traditional API")
    print("-" * 70)
    table7 = Table(title="[bold magenta]Mixed API Example[/]")
    table7.add_column("Name", style="bold")  # Rich-style API
    table7.add_column("Age")
    table7.add_column("City")
    table7.add_row("Alice", "28", "New York")
    table7.add_row("Bob", "35", "Los Angeles")
    table7.add_row("Charlie", "42", "Chicago")
    # Then override with traditional colors
    table7.set_cols_color([None, "cyan", "yellow"])  # Keep first col, color others
    
    print(table7.draw())
    
    # Example 8: Complex color combinations
    print("\n\nExample 8: Complex Color Combinations")
    print("-" * 70)
    table8 = Table(max_width=0)
    table8.set_cols_align(["l", "r", "r", "r", "c"])
    table8.set_cols_dtype(["t", "f", "f", "f", "t"])
    # Using various make_colors formats
    table8.set_cols_color([
        "bold-white",           # bold white
        "green-black",          # green on black
        "italic-cyan",          # italic cyan
        "bold-yellow-blue",     # bold yellow on blue
        "lr"                    # lightred abbreviation
    ])
    table8.header(["Stock", "Open", "High", "Low", "Change"])
    table8.add_row("AAPL", 150.25, 152.30, 149.80, "▲ +1.2%")
    table8.add_row("GOOGL", 2800.50, 2825.00, 2790.00, "▲ +0.8%")
    table8.add_row("MSFT", 305.75, 308.20, 304.50, "▼ -0.5%")
    
    print(table8.draw())
    
    # Example 9: Alternating row colors
    print("\n\nExample 9: Alternating Row Colors")
    print("-" * 70)
    table9 = Table(max_width=0, title="User List", title_style="bold-cyan")
    table9.set_cols_align(["r", "l", "l", "r"])
    table9.header(["ID", "Username", "Email", "Status"])
    
    rows_data = [
        ["001", "john_doe", "john@example.com", "Active"],
        ["002", "jane_smith", "jane@example.com", "Active"],
        ["003", "bob_wilson", "bob@example.com", "Inactive"],
        ["004", "alice_brown", "alice@example.com", "Active"],
        ["005", "charlie_davis", "charlie@example.com", "Active"],
    ]
    
    for row in rows_data:
        table9.add_row(*row)
    
    # Alternate between two colors
    alternating_colors = ["dim", None, "dim", None, "dim"]
    table9.set_rows_color(alternating_colors)
    
    print(table9.draw())
    
    # Example 10: Status-based coloring
    print("\n\nExample 10: Status-based Row Coloring")
    print("-" * 70)
    table10 = Table(max_width=0)
    table10.set_cols_align(["l", "c", "r", "r"])
    table10.header(["Task", "Status", "Progress", "Priority"])
    
    tasks = [
        ["Deploy to Production", "✓ Complete", "100%", "High"],
        ["Code Review", "⚠ In Progress", "75%", "Medium"],
        ["Write Tests", "● Pending", "0%", "High"],
        ["Update Docs", "✓ Complete", "100%", "Low"],
        ["Fix Bug #123", "✗ Blocked", "30%", "Critical"],
    ]
    
    for task in tasks:
        table10.add_row(*task)
    
    # Color based on status
    status_colors = [
        "bold-green",      # Complete
        "bold-yellow",     # In Progress
        "dim",             # Pending
        "bold-green",      # Complete
        "bold-red"         # Blocked
    ]
    table10.set_rows_color(status_colors)
    
    print(table10.draw())
    
    print("\n" + "="*70)
    print("New Features:")
    print("="*70)
    print("✓ set_cols_color(array)")
    print("  - Set color for each column")
    print("  - Supports abbreviations: 'y', 'r', 'c', 'bl', 'lb', etc.")
    print("  - Supports full names: 'yellow', 'red', 'cyan', 'blue', etc.")
    print("  - Supports attributes: 'bold-red', 'italic-cyan', etc.")
    print("  - Supports background: 'red-yellow', 'white-blue', etc.")
    print()
    print("✓ set_rows_color(array)")
    print("  - Set color for each row")
    print("  - Use None to skip coloring specific rows")
    print("  - Same format support as set_cols_color()")
    print("  - Great for status-based coloring")
    print()
    print("✓ Rich Markup Support via make_colors:")
    print("  - Using make_colors.parse_rich_markup() for parsing")
    print("  - Using make_colors.make_colors() for styling")
    print("  - All make_colors formats are supported")
    print("="*70)
    
    print("\n" + "="*70)
    print("Integration Status:")
    if HAS_MAKE_COLORS:
        print("✓ make_colors module is active - Full color support enabled")
        print("✓ parse_rich_markup() is available")
    else:
        print("⚠ make_colors not found - Using fallback ANSI colors")
    print("="*70 + "\n")