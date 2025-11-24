Contributing Guide
==================

We welcome contributions to make_colors!

How to Contribute
-----------------

1. **Fork the Repository**

   .. code-block:: bash

      git clone https://github.com/cumulus13/make_colors.git
      cd make_colors

2. **Create a Branch**

   .. code-block:: bash

      git checkout -b feature/your-feature-name

3. **Make Changes**

   - Write code
   - Add tests
   - Update documentation

4. **Test Your Changes**

   .. code-block:: bash

      python -m pytest tests/

5. **Submit Pull Request**

   Push your changes and create a pull request on GitHub.

Development Setup
-----------------

.. code-block:: bash

   # Install in development mode
   pip install -e ".[dev]"
   
   # Run tests
   pytest
   
   # Build documentation
   cd docs
   make html

Code Style
----------

- Follow PEP 8
- Use type hints
- Write docstrings
- Add tests for new features

Documentation
-------------

When adding features, update:

- Docstrings
- Usage guide
- Examples
- API reference

Contact
-------

- GitHub: https://github.com/cumulus13/make_colors
- Issues: https://github.com/cumulus13/make_colors/issues