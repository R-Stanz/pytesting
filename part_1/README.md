# Part 1 - Recap
---

## Summary
* [Setup the enviroment](#setup)
* [How to run/use pytests](#how)

---

## Setup The Enviroment {#setup}
### Summary {#setup-summary}
- [Summary](#setup-summary)

- [Setup Venv](#setup-venv)
    - [Install Venv](#install-venv)
    - [Check Venv install](#check-venv-install)
    - [New Venv enviroment](#new-venv-enviroment)
    - [Activate Venv](#activate-venv)
    - [Deactivate Venve](#deactivate-venv)

- [Pytest](#setup-pytest)
    - [Install Pytest](#install-pytest)
    - [Check Pytest install](#check-pytest-intall)

### Setup Venv 
#### Install Venv
Just run the command bellow.
```bash
$ pip install venv
```

#### Check Venv Install
You can do it with the following command.
```bash
$ pip show venv						
```

#### New Venv Enviroment
When running the command bellow the path chosen will be the on to gain the configuration for new virtual enviroment with venv (the venv directory).
```bash
$ python venv -m <path_to_venv_directory>/
```

#### Activate Venv
To star a venv virtual enviroment go to the venv configuration directory to find the bin directory with the activation script.
```bash
$ source <path_to_venv_directory>/bin/activate
```

#### Deactivate Venv
To get out of the virtual enviroment run the code bellow.
```bash
(<enviroment_name>) $ deactivate
```

### Setup Pytest
#### Install Pytest
Do it by running the code bellow inside the enviroment where it’s going to be used.
```bash
(<enviroment_name>) $ pip install pytest
```

#### Check Pytest Install
Run the code bellow, inside the enviroment where the pytest is going to be used.
```bash
(<enviroment_name>) $ pip show pytest
```
Or
```bash
(<enviroment_name>) $ pytest --version 
```

## How To Run / Use Pytest {#how}