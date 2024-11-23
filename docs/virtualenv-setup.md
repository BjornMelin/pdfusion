
# Virtual Environment Setup Guide

Setting up a virtual environment ensures that the project dependencies are isolated and do not interfere with other projects. Follow these steps to set up and activate a virtual environment.

## Using `venv`

1. Create a new virtual environment in the project directory:

    ```bash
    python -m venv venv
    ```

2. Activate the virtual environment:

    - On Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```bash
        source venv/bin/activate
        ```

## Using `virtualenv`

To ensure that the project dependencies are isolated and do not interfere with other projects, it is recommended to use a virtual environment. Follow these steps to set up and activate a virtual environment:

1. Install the `virtualenv` package if you haven't already:

    ```bash
    pip install virtualenv
    ```

2. Create a new virtual environment in the project directory:

    ```bash
    virtualenv venv
    ```

3. Activate the virtual environment:

    - On Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```bash
        source venv/bin/activate
        ```
