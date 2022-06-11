# libchecker
A single-file library designed to make the installation process of libraries as easy as possible

# Installation
To install this library, just copy the `libchecker` folder to anywhere in your project, and import it using `import libchecker`.

**Read the comment at the top of `libchecker/__init__.py` to see what you can and cannot do with the library source**

# Usage
## Checking for an import
To check for an import, use `is_import_available("import_name")`

## Installing missing libraries
To install any libraries that might be missing and continue, use `check_if_libraries_exist([("library_import_that_gets_installed", "library-name")])`

Here, it's very important to use the correct format for the library names. First, the import name is specified, which you are using with `import`. If you use `import lib_abc`, then the import name is `lib_abc`. The library name tho is the package name of the pypi package. If you install `abc-lib` via pip (`pip install abc-lib`), then the library name is `abc-lib`.

You can also just make it check for the libraries when the 2nd argument is set to False, it will then return True if all libraries are present, and False if not. If the 2nd argument is True or not set (True by default), then it will try to install all libraries which are missing and return True

## Installing all libraries from a `requirements.txt`
You can also make the library look for a requirements.txt file, and install all libraries found there. To do this, use `install_all_from_requirements_txt()`.

You can also specify the path to the `requirements.txt` file, but by default it is the `"requirements.txt"` standard.

## Notes to _ functions
Functions prefixed with _ are for internal use, and should **not** be called directly, unless you have a good reason to.

# Credits
Please leave the comment in `__init__.py` there, so I am credited for the work I do. Thank you.

# Support
If you like this project, please consider leaving a star. It really helps me out and helps others find this project.