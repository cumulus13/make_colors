#!/usr/bin/env python3

# File: make_colors/console.py
# Author: Hadi Cahyadi <cumulus13@gmail.com>
# Date: 2026-08-10
# Description: 
# License: MIT

from make_colors import make_colors

class Console:
    @classmethod
    def print(cls, string, foreground='white', background=None, attrs=[], force=False):
        """Print colored text directly to the console with automatic formatting.

        This convenience function combines color formatting and printing in a single call.
        It applies the make_colors() function and immediately outputs the result to stdout,
        making it ideal for direct console output without intermediate variables.

        Args:
            string (str): The text string to be printed with colors.
                         Examples: "System ready", "Error: File not found", "Process complete"
            foreground (str): Foreground text color. Supports full names, abbreviations,
                             combined formats, and attribute detection. Defaults to 'white'.
                             Examples: "red", "r", "lightblue", "bold-red-yellow"
            background (str, optional): Background color specification.
                                       Supports 'on_' prefix format and abbreviations.
                                       Defaults to None (transparent background).
                                       Examples: "yellow", "on_blue", "lb"
            attrs (list): List of text attributes for styling options.
                         Examples: ['bold', 'underline']. Defaults to empty list.
            force (bool): Force colored output even when terminal doesn't support colors.
                         Useful for logging or file redirection. Defaults to False.

        Returns:
            None: This function outputs directly to console and returns None.

        Example:
            >>> # Direct colored printing
            >>> print("Success!", "green")
            >>> print("Warning: Low disk space", "yellow", "on_black")
            >>> print("Critical Error!", "red", "on_white")
            
            >>> # Using abbreviations
            >>> print("Info message", "lb")  # Light blue text
            >>> print("Debug output", "c", "b")  # Cyan on black
            
            >>> # Combined format with attribute detection (NEW!)
            >>> print("Error", "bold-red")  # Bold red text
            >>> print("Warning", "italic-yellow-black")  # Italic yellow on black

            >>> # Force colors for file redirection
            >>> import sys
            >>> with open("colored_log.txt", "w") as sys.stdout:
            ...     print("Log entry", "blue", force=True)
            
            >>> # Rich markup format
            >>> print("[bold blue]Information[/]")

        Note:
            - This function modifies the built-in print() behavior within this module
            - Automatically handles color support detection
            - Supports all new attribute detection features
            - Respects all environment variable settings
            - Original print function is preserved as _print for internal use
        """

        #logger.success(f"string: {string}")
        print(make_colors(string, foreground, background, attrs, force))
    
    @classmethod
    def status(cls, message, foreground='white', background=None, attrs=[], force=False, **kwargs):
        """Print a status message with color formatting.

        This function is similar to Console.print but is specifically intended
        for printing status messages. It applies color formatting and outputs
        the result to stdout.

        Args:
            message (str): The status message to be printed.
            foreground (str): Foreground text color. Defaults to 'white'.
            background (str, optional): Background color specification. Defaults to None.
            attrs (list): List of text attributes. Defaults to empty list.
            force (bool): Force color output regardless of support. Defaults to False.

        Returns:
            None: This function outputs directly to console and returns None.
        """
        cls.print(message, foreground, background, attrs, force)
