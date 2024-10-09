# Part 1 - Recap

## Summary <a name="recap-summary"></a>
* [Summary](#recap-summary)
* [Setup the enviroment](#setup)
* [How to run/use pytests](#how)

---
## Setup The Enviroment <a hreaf="#setup"></a>
### Summary <a href="#setup-summary"></a>
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

---
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

---
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

---
## How To Run / Use Pytest <a name="how"></a>
---
### Summary <a name="how-summary"></a>
- [Summary](#how-summary)
- [Conventions](#conventions)
- [Assertions](#assertions)
    - [Introduction]()
    - [Uses](#assertion-uses)
- [Mark decorators](#mark-decorators)
    - [Introduction](#mark-intro)
    - [Skip](#skip)
    - [Skip if](#skip-if)
    - [xFail](#xfail)
- [Testing](#testing)
    - [Testing a single file](#testing-a-single-file)
    - [Testing a single function](#testing-a-single-function)
    - [Testing multiple files](#testing-multiple-files)
    - [Most common Pytest flags](#most-common-pytest-flags)

---
### Conventions
Pytest follows a few conventions for discovering test files (as explained on the [pytest documentation](https://docs.pytest.org/en/7.1.x/explanation/goodpractices.html)). Making it simple, the rules for pytest default discovery/conventions:

- Test files must have the regex test_*.py or *_test.py in order to be found.
- Functions and methods must start with test_ on their names.
- Classes must start with Test prefix.

---
### Assertions
#### Introduction
Python has a built-in tool named assert wich is used to check a set of defined conditions.
For Example:
```python
def test_2_greater_than_3():
	assert 2 > 3

def test_3_greater_then_2():
	assert 3 > 2
```
In this case once the pytest runs these functions it’ll get a failed test (for the test where if 2 > 3) and a success test (for the test where 3 > 2).

#### Uses <a name="assertion-uses"></a>
Assertions can be made with python operators. Besides that, they are commonly used together with the pytest mark decorator. See more more details at the [pytest documentation](https://docs.pytest.org/en/7.1.x/how-to/assert.html). 

---
### Mark Decorators
#### Introduction <a name="mark-intro"></a>
Mark decorators are really usefull on helping managing how tests should be handled. For more information find out at the [pytest documentation](https://docs.pytest.org/en/stable/reference/reference.html#marks). Furthermore pytest should be imported prior to the use of the mark decorators.
An example of how to place a decorator on a test could be:
```python
import pytest

@pytest.mark.skip(reason="No need to test this obvious thing!")
def test_1_equals_1():
	assert 1 == 1
```
#### Skip
The skip mark `pytest.mark.skip(reason=None)` is usefull to make a test be skipped from the testings, simply because a test has this decorator. The reason parameter is used on pytest verbose `pytest -v` or `pytest -vv` (more info on pytest flags are [here](#most-common-pytest-flags)) to show a message to explain why that test was skipped.

#### Skip If
Skip if works almost the same way as the [skip](#skip). The main difference is that it is skipped based on a condition. `pytest.mark.skipif(condition, *,reason=None)` thats how the decorator is defined, the condition parameter must have a boolean value.

#### xFail
It marks tests that are expected to fail. In case the test has this mark and fails pytest will show it as `XFAIL` in case it fails, otherwise it will be show as `XPASS` (unless the strict parameter is True, in this case the test will be show as a `FAIL`). This mark accepts a lot of parameters, it’s defined as `pytest.mark.xfail(condition=False, *, reason=None, raises=None, run=True, strict=xfail_strict)`.

---
### Testing
#### Testing A Single File
To test a single a file you should just be passing it’s location to the pytest, like on example code bellow.
```bash
(<enviroment_name>) $ pytest <path>/<file_name>
```
Or if the file is on the present working directory (pwd) simply:
```bash
(<enviroment_name>) $ pytest <file_name>
```

#### Testing A Single Function
The code has the same structure of selecting a single file to be tested by pytest, but it should be selected the file where the function is located and at the ending appended the name of function preceeded by :: (as on the example bellow).
```bash
(<enviroment_name>) $ pytest <path>/<file_name>::<function_name>
```

#### Testing Multiple Files
There are a few options for this.
1. One way is by passing individually the files names to pytest, as on the code bellow.
```bash
(<enviroment_name>) $ pytest <path>/<file_name> <path-2>/<file_name-2>
```
2. Another way, using wild cards (just an example bellow):
```bash
(<enviroment_name>) $ pytest <path>/*
```
3. Pytest also accepts directories to look for files. But it won’t be restrained to the directory given to it, the pytest will also look up for tests on the sub-directories there were inside the directory the was given to it.
```bash
(<enviroment_name>) $ pytest <path>/<directory_name>/
```
4. Using pytest with the -k flag, keyword expressions:
```bash
(<enviroment_name>) $ pytest -k "http or quick"
```
On the code above, pytest will look for all tests that might have http or quick some where on their names, taking the current working directory (pwd) where it was used as starting point. For info there is the [pytest documentation](https://docs.pytest.org/en/stable/example/markers.html#using-k-expr-to-select-tests-based-on-their-name).

#### Most Common Pytest Flags
1. **-v**: This flag makes the pytest verbose.
2. **-vv**: Makes the pytest output even more verbose, in case of errors it will show each occurance that was different from what was expected.
3. **-tb=no**: Turns off traceback messages of pytest.
4. **-k**: Defines a search pattern for pytest searching of functions.

---