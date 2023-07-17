![](images/calc.png)
____

This code is a simple calculator program that takes user input for two numbers and an operation (+, -, *, /).
It performs the operation and displays the result, handling division by zero and invalid operations.

## Menu
-   [Requirements](#Requirements)
-   [Installation](#Installation)
  
## Requirements
- Python 3.10 or higher - Ensure `Python3.10`, `Pip3` and `Virtualenv` are installed
- Install Python dependencies - `$ pip3 install -r requirements.txt` [required for running tests locally]
  
## Installation
In order to run the package on your local machine, you can clone the repository and utilize the startup.sh script:
```bash
git clone https://github.com/BatelT/simple-python-calc.git
cd simple-python-calc
source startup.sh
```

### Installing Pip Binary
To install the calc as a binary, you'll need to build the binary and install it using Pip3:
```bash
python3 -m build
pip3 install dist/fd55-$VERSION.tar.gz
```
