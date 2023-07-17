![](images/calc.png)
____

This code is a simple calculator program that takes user input for two numbers and an operation (+, -, *, /).
It performs the operation and displays the result, handling division by zero and invalid operations.

## Requirements
- Python 3.10 or higher - Ensure `Python3.10`, `Pip3` and `Virtualenv` are installed
- Artifactory Pypi local Repository 

## JFrog Artifactory configuration 
To start a trial with Artifactory cloud you can easily [click here ]([url](https://jfrog.com/start-free/))
Then create a [Pypi repository ]([url](https://jfrog.com/help/r/jfrog-artifactory-documentation/pypi-repositories)) like the following:
![](https://github.com/simple-python-calc/images/Pypi-repo.gif)
After you create the repository run the [set me up ]([url](https://jfrog.com/help/r/what-s-new-in-the-set-me-up-dialog/the-set-me-up-option-explained))
to configure the pypi client like the following:
```
To deploy packages using setuptools you need to add an Artifactory repository to the .pypirc file (usually located in your home directory):
[distutils]
index-servers = local
[local]
repository: https://<ARTIFACTORY-URL>.jfrog.io/artifactory/api/pypi/<repository-name>
username: <USERNAME>
password: <PASSWORD>
To deploy a python egg to Artifactory, after changing the .pypirc file, run the following command:

python3 setup.py sdist upload -r local
To deploy a python wheel to Artifactory, after changing the .pypirc file, run the following command:

python3 setup.py bdist_wheel upload -r local
where local is the index server you defined in .pypirc.
```
  
## Installation
In order to run the package on your local machine, you can clone the repository and utilize the startup.sh script:
```bash
git clone https://github.com/BatelT/simple-python-calc.git
cd simple-python-calc
source startup.sh
```
