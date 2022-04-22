# Python code and tutorials code.

## How to create a python virtual environment for your code on Ubuntu
From outside any python virtual environment (i.e. from system wide python), 
use the following steps to create a virtual environment based on user installed
python.

1- First install virtualenv:
<br>```pip3 install virtualenv```

2- Then install your required python version following the steps in:

https://websiteforstudents.com/how-to-install-python-on-ubuntu-linux/

3- Finally, create the pyhton environment using the followin command:
```
python3 -m virtualenv -p=</usr/local/bin/pythonX.X> <env_folder_name>
```
For more info, refer to:

https://www.roelpeters.be/virtualenv-venv-choose-python-version/

## Installing a package in a specific version/enviornment of python

#### The system default python:
```$ python -m pip install fish```

#### A virtualenv's python:
```$ .env/bin/python -m pip install fish```

#### A specific version of python:
```$ python3.6 -m pip install fish```
