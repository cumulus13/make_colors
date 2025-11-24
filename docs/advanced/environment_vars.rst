Environment Variables
=====================

make_colors can be controlled globally using environment variables. This is useful for
disabling colors in production, forcing colors in CI/CD, or debugging color parsing issues.

Available Environment Variables
--------------------------------

MAKE_COLORS
~~~~~~~~~~~

Control whether colors are enabled or disabled globally.

**Values:**

- ``0`` - Disable all color output
- ``1`` - Enable color output (default behavior)

**When to Use:**

- Production environments where colored logs interfere with log aggregation
- Plain text output requirements
- Testing without color codes
- Disabling colors for specific users/environments

**Bash/Linux/macOS:**

.. code-block:: bash

   # Disable colors
   export MAKE_COLORS=0
   python myapp.py
   
   # Enable colors (explicit)
   export MAKE_COLORS=1
   python myapp.py
   
   # Temporary for one command
   MAKE_COLORS=0 python myapp.py

**Windows (CMD):**

.. code-block:: batch

   rem Disable colors
   set MAKE_COLORS=0
   python myapp.py
   
   rem Enable colors
   set MAKE_COLORS=1
   python myapp.py

**Windows (PowerShell):**

.. code-block:: powershell

   # Disable colors
   $env:MAKE_COLORS = "0"
   python myapp.py
   
   # Enable colors
   $env:MAKE_COLORS = "1"
   python myapp.py

**Python:**

.. code-block:: python

   import os
   from make_colors import make_colors
   
   # Disable colors programmatically
   os.environ['MAKE_COLORS'] = '0'
   
   # Now all color calls return plain text
   text = make_colors("Error!", "red")
   print(text)  # Output: "Error!" (no color codes)
   
   # Re-enable colors
   os.environ['MAKE_COLORS'] = '1'
   text = make_colors("Error!", "red")
   print(text)  # Output: colored text

MAKE_COLORS_FORCE
~~~~~~~~~~~~~~~~~

Force color output even when terminal detection indicates no color support.

**Values:**

- ``1`` or ``True`` - Force colors regardless of terminal support
- ``0`` or any other value - Use automatic detection (default)

**When to Use:**

- Writing colored output to files
- CI/CD environments that support ANSI but fail TTY detection
- Logging systems that preserve ANSI codes
- Generating colored HTML from ANSI codes

**Bash/Linux/macOS:**

.. code-block:: bash

   # Force colors for file output
   export MAKE_COLORS_FORCE=1
   python myapp.py > output.log
   
   # View with color support
   cat output.log

**Python:**

.. code-block:: python

   import os
   from make_colors import make_colors
   
   # Force colors for file output
   os.environ['MAKE_COLORS_FORCE'] = '1'
   
   with open('colored_log.txt', 'w') as f:
       colored_text = make_colors("Log entry", "blue")
       f.write(colored_text)
   
   # Or use force parameter
   with open('colored_log.txt', 'w') as f:
       text = make_colors("Log entry", "blue", force=True)
       f.write(text)

MAKE_COLORS_DEBUG
~~~~~~~~~~~~~~~~~

Enable detailed debug output for troubleshooting color parsing.

**Values:**

- ``1``, ``true``, or ``True`` - Enable debug mode
- ``0`` or any other value - Disable debug mode (default)

**When to Use:**

- Debugging color parsing issues
- Understanding how color specifications are interpreted
- Troubleshooting attribute detection
- Development and testing

**Bash/Linux/macOS:**

.. code-block:: bash

   # Enable debug mode
   export MAKE_COLORS_DEBUG=1
   python myapp.py

**Python:**

.. code-block:: python

   import os
   from make_colors import make_colors
   
   # Enable debug mode
   os.environ['MAKE_COLORS_DEBUG'] = '1'
   
   # Now you'll see detailed parsing info
   text = make_colors("Test", "bold-red-yellow")
   # Outputs debug info:
   # getSort: data = bold-red-yellow
   # getSort: foreground = red
   # getSort: background = yellow
   # getSort: detected_attrs = ['bold']

Practical Use Cases
-------------------

Production Deployment
~~~~~~~~~~~~~~~~~~~~~

Disable colors in production for clean logs:

**Docker/Container:**

.. code-block:: dockerfile

   # Dockerfile
   FROM python:3.11
   
   # Disable colors in production
   ENV MAKE_COLORS=0
   
   COPY . /app
   WORKDIR /app
   RUN pip install -r requirements.txt
   
   CMD ["python", "app.py"]

**systemd Service:**

.. code-block:: ini

   # /etc/systemd/system/myapp.service
   [Unit]
   Description=My Application
   
   [Service]
   Environment="MAKE_COLORS=0"
   ExecStart=/usr/bin/python3 /opt/myapp/app.py
   
   [Install]
   WantedBy=multi-user.target

CI/CD Pipelines
~~~~~~~~~~~~~~~

Force colors in CI/CD for colored output in logs:

**GitHub Actions:**

.. code-block:: yaml

   # .github/workflows/test.yml
   name: Tests
   
   on: [push]
   
   jobs:
     test:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v2
         - name: Run tests
           env:
             MAKE_COLORS_FORCE: 1
           run: python -m pytest

**GitLab CI:**

.. code-block:: yaml

   # .gitlab-ci.yml
   test:
     image: python:3.11
     variables:
       MAKE_COLORS_FORCE: "1"
     script:
       - pip install -r requirements.txt
       - python -m pytest

**Jenkins:**

.. code-block:: groovy

   // Jenkinsfile
   pipeline {
       agent any
       environment {
           MAKE_COLORS_FORCE = '1'
       }
       stages {
           stage('Test') {
               steps {
                   sh 'python -m pytest'
               }
           }
       }
   }

Development vs Production
~~~~~~~~~~~~~~~~~~~~~~~~~

Different settings for different environments:

.. code-block:: python

   # config.py
   import os
   
   class Config:
       # Development
       if os.getenv('ENVIRONMENT') == 'development':
           os.environ['MAKE_COLORS'] = '1'
           os.environ['MAKE_COLORS_DEBUG'] = '1'
       
       # Production
       elif os.getenv('ENVIRONMENT') == 'production':
           os.environ['MAKE_COLORS'] = '0'
           os.environ['MAKE_COLORS_DEBUG'] = '0'
       
       # Testing
       elif os.getenv('ENVIRONMENT') == 'testing':
           os.environ['MAKE_COLORS'] = '0'  # No colors in tests

**Usage:**

.. code-block:: bash

   # Development
   ENVIRONMENT=development python app.py
   
   # Production
   ENVIRONMENT=production python app.py
   
   # Testing
   ENVIRONMENT=testing pytest

Logging Configuration
~~~~~~~~~~~~~~~~~~~~~

Configure colored logging based on environment:

.. code-block:: python

   import os
   import logging
   from make_colors import make_colors
   
   class ColoredFormatter(logging.Formatter):
       """Colored log formatter."""
       
       COLORS = {
           'DEBUG': 'cyan',
           'INFO': 'blue',
           'WARNING': 'yellow',
           'ERROR': 'red',
           'CRITICAL': 'white-red'
       }
       
       def format(self, record):
           # Check if colors are enabled
           if os.getenv('MAKE_COLORS') == '0':
               return super().format(record)
           
           # Color the level name
           color = self.COLORS.get(record.levelname, 'white')
           record.levelname = make_colors(
               f"[{record.levelname}]", 
               color
           )
           
           return super().format(record)
   
   # Setup logging
   handler = logging.StreamHandler()
   handler.setFormatter(ColoredFormatter(
       '%(asctime)s %(levelname)s %(message)s'
   ))
   
   logger = logging.getLogger(__name__)
   logger.addHandler(handler)
   logger.setLevel(logging.DEBUG)
   
   # Use it
   logger.debug("Debug message")
   logger.info("Info message")
   logger.warning("Warning message")
   logger.error("Error message")

Testing Without Colors
~~~~~~~~~~~~~~~~~~~~~~~

Ensure tests work without color codes:

.. code-block:: python

   # test_myapp.py
   import os
   import pytest
   from make_colors import make_colors
   
   @pytest.fixture(autouse=True)
   def disable_colors():
       """Disable colors for all tests."""
       old_value = os.environ.get('MAKE_COLORS')
       os.environ['MAKE_COLORS'] = '0'
       
       yield
       
       # Restore
       if old_value is not None:
           os.environ['MAKE_COLORS'] = old_value
       else:
           del os.environ['MAKE_COLORS']
   
   def test_colored_output():
       """Test that color function returns plain text in tests."""
       text = make_colors("Error", "red")
       assert text == "Error"  # No ANSI codes
       assert "\033[" not in text

Environment Detection
~~~~~~~~~~~~~~~~~~~~~

Auto-detect and configure based on environment:

.. code-block:: python

   import os
   import sys
   from make_colors import MakeColors
   
   def configure_colors():
       """Auto-configure colors based on environment."""
       
       # CI/CD environments
       ci_environments = [
           'CI', 'CONTINUOUS_INTEGRATION',
           'GITHUB_ACTIONS', 'GITLAB_CI',
           'CIRCLECI', 'TRAVIS', 'JENKINS'
       ]
       
       is_ci = any(os.getenv(env) for env in ci_environments)
       
       # Docker/Container
       is_docker = os.path.exists('/.dockerenv')
       
       # Terminal detection
       is_tty = sys.stdout.isatty()
       
       # Configure
       if is_ci:
           # Force colors in CI
           os.environ['MAKE_COLORS_FORCE'] = '1'
       elif is_docker:
           # Disable in Docker by default
           os.environ['MAKE_COLORS'] = '0'
       elif not is_tty:
           # Disable for non-TTY
           os.environ['MAKE_COLORS'] = '0'
       
       # Debug info
       if os.getenv('MAKE_COLORS_DEBUG') == '1':
           print(f"CI: {is_ci}")
           print(f"Docker: {is_docker}")
           print(f"TTY: {is_tty}")
           print(f"Colors: {MakeColors.supports_color()}")
   
   # Call at application start
   configure_colors()

Command-Line Control
--------------------

Allow users to control colors via command line:

.. code-block:: python

   # app.py
   import argparse
   import os
   from make_colors import make_colors
   
   def main():
       parser = argparse.ArgumentParser()
       parser.add_argument(
           '--no-color',
           action='store_true',
           help='Disable colored output'
       )
       parser.add_argument(
           '--force-color',
           action='store_true',
           help='Force colored output'
       )
       parser.add_argument(
           '--debug-colors',
           action='store_true',
           help='Enable color debug mode'
       )
       
       args = parser.parse_args()
       
       # Configure environment
       if args.no_color:
           os.environ['MAKE_COLORS'] = '0'
       
       if args.force_color:
           os.environ['MAKE_COLORS_FORCE'] = '1'
       
       if args.debug_colors:
           os.environ['MAKE_COLORS_DEBUG'] = '1'
       
       # Your application logic
       print(make_colors("Application started", "green"))
   
   if __name__ == '__main__':
       main()

**Usage:**

.. code-block:: bash

   # Normal (auto-detect)
   python app.py
   
   # Disable colors
   python app.py --no-color
   
   # Force colors
   python app.py --force-color
   
   # Debug mode
   python app.py --debug-colors

Best Practices
--------------

1. **Respect User Settings**

   Always check environment variables before overriding:

   .. code-block:: python

      import os
      
      # Don't override if already set
      if 'MAKE_COLORS' not in os.environ:
          os.environ['MAKE_COLORS'] = '1'

2. **Provide Defaults**

   Set sensible defaults for your application:

   .. code-block:: python

      # config.py
      import os
      
      # Set defaults if not already configured
      os.environ.setdefault('MAKE_COLORS', '1')

3. **Document Configuration**

   Document available environment variables in your README:

   .. code-block:: markdown

      ## Environment Variables
      
      - `MAKE_COLORS` - Enable/disable colors (0 or 1)
      - `MAKE_COLORS_FORCE` - Force colors (1 or 0)
      - `MAKE_COLORS_DEBUG` - Debug mode (1 or 0)

4. **Test Both Modes**

   Test your application with colors on and off:

   .. code-block:: python

      # Test with colors
      os.environ['MAKE_COLORS'] = '1'
      test_with_colors()
      
      # Test without colors
      os.environ['MAKE_COLORS'] = '0'
      test_without_colors()

See Also
--------

- :doc:`../usage` - Complete usage guide
- :doc:`cross_platform` - Cross-platform compatibility
- :doc:`../examples` - Practical examples