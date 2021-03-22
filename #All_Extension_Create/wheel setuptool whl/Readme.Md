Requierment:
"""""""""""
python3 -m pip install --user --upgrade setuptools wheel
python3 -m pip install --user --upgrade twine




Creating the package files:
"""""""""""""""""""""""""""
packaging_tutorial
├── LICENSE
├── README.md
├── example_pkg
│   └── __init__.py
├── setup.py
└── tests

A simple project:
""""""""""""""""
        packaging_tutorial
        └── example_pkg
            └── __init__.py

mkd packaging_tutorial
cd packaging_tutorial

example_pkg/__init__.py is required to import the directory as a package, and can simply be an empty file.


Creating a test folder:
""""""""""""""""""""""
tests/ is a placeholder for unit test files. Leave it empty for now.


Creating setup.py:
"""""""""""""""""
setup.py is the build script for setuptools. It tells setuptools about your package (such as the name and version) as well as which code files to include.

setup.py:
        import setuptools

        with open("README.md", "r") as fh:
            long_description = fh.read()

        setuptools.setup(
            name="example-pkg-YOUR-USERNAME-HERE", # Replace with your own username
            version="0.0.1",
            author="Example Author",
            author_email="author@example.com",
            description="A small example package",
            long_description=long_description,
            long_description_content_type="text/markdown",
            url="https://github.com/pypa/sampleproject",
            packages=setuptools.find_packages(),
            classifiers=[
                "Programming Language :: Python :: 3",
                "License :: OSI Approved :: MIT License",
                "Operating System :: OS Independent",
            ],
            python_requires='>=3.6',
        )

Creating README.md:
"""""""""""""""""""
    # Example Package

    This is a simple example package. You can use
    [Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
    to write your content.

Creating a LICENSE:
""""""""""""""""""
        Copyright (c) 2018 The Python Packaging Authority

        Permission is hereby granted, free of charge, to any person obtaining a copy
        of this software and associated documentation files (the "Software"), to deal
        in the Software without restriction, including without limitation the rights
        to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
        copies of the Software, and to permit persons to whom the Software is
        furnished to do so, subject to the following conditions:

        The above copyright notice and this permission notice shall be included in all
        copies or substantial portions of the Software.

        THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
        IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
        FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
        AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
        LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
        OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
        SOFTWARE.


Generating distribution archives
""""""""""""""""""""""""""""""""
1.full fill requierment given above
2.python3 setup.py sdist bdist_wheel

This command should output a lot of text and once completed should generate two files in the dist directory:

dist/
  example_pkg_YOUR_USERNAME_HERE-0.0.1-py3-none-any.whl
  example_pkg_YOUR_USERNAME_HERE-0.0.1.tar.gz

Uploading the distribution archives
"""""""""""""""""""""""""""""""""""
    Finally, it’s time to upload your package to the Python Package Index!

    The first thing you’ll need to do is register an account on Test PyPI. Test PyPI is a separate instance of the package index intended for testing and experimentation. It’s great for things like this tutorial where we don’t necessarily want to upload to the real index. To register an account, go to https://test.pypi.org/account/register/ and complete the steps on that page. You will also need to verify your email address before you’re able to upload any packages. For more details on Test PyPI, see Using TestPyPI.

    Now you’ll create a PyPI API token so you will be able to securely upload your project.

    Go to https://test.pypi.org/manage/account/#api-tokens and create a new API token; don’t limit its scope to a particular project, since you are creating a new project.

    ..................................................................................................
    |Don’t close the page until you have copied and saved the token — you won’t see that token again.|
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    Now that you are registered, you can use twine to upload the distribution packages. You’ll need to install Twine:

    Once installed, run Twine to upload all of the archives under dist:

            python3 -m twine upload --repository testpypi dist/*

    You will be prompted for a username and password. For the username, use __token__. For the password, use the token value, including the pypi- prefix.

    After the command completes, you should see output similar to this:

            Uploading distributions to https://test.pypi.org/legacy/
            Enter your username: [your username]
            Enter your password:
            Uploading example_pkg_YOUR_USERNAME_HERE-0.0.1-py3-none-any.whl
            100%|█████████████████████| 4.65k/4.65k [00:01<00:00, 2.88kB/s]
            Uploading example_pkg_YOUR_USERNAME_HERE-0.0.1.tar.gz
            100%|█████████████████████| 4.25k/4.25k [00:01<00:00, 3.05kB/s]

    Once uploaded your package should be viewable on TestPyPI, for example, https://test.pypi.org/project/example-pkg-YOUR-USERNAME-HERE

Installing your newly uploaded package:
""""""""""""""""""""""""""""""""""""""
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps example-pkg-YOUR-USERNAME-HERE
