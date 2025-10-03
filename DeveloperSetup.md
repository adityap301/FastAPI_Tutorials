# Developer Setup

## Installation

### 1. Python

1. Download Python (v3.12.10): [Click Here](https://www.python.org/downloads/release/python-31210/)

2. Run the setup file. Follow the on-screen instructions and complete the installation process. 

### 2. Postman (Optional)

1. Download Postman: [Click Here](https://www.postman.com/downloads/)

2. Run the setup file and complete the installation process.

### 3. IDE Setup

Have your faviourite IDE set up and have have all the extensions pertaining to Python installed.

Here are the steps for setting up VS Code:

1. Download VS Code: [Click Here](https://code.visualstudio.com/download)

2. Install the `Python` extension.

3. Intall the `SQLite` by alexcvzz extension.

## Virtual Environment Setup

1. cd into the project folder where the venv is to be set up.

```bash
cd <path-to-project>
```

2. Create the venv

```bash
python -m venv <venv-name> --system-site-packages
```

3. Activate the venv

```bash
.\<path-to-venv>\Scripts\activate.bat
```

4. Check the installed packages

```bash
pip list
```

5. Upgrade pip

```bash
python -m pip install --upgrade pip
```

6. Download the dependencies from requirements.txt

```bash
pip install -r <path-to-project>/src/requirements.txt
```