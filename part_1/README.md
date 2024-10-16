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
- [Fixture decorator](#fixture-decorator)
    - [Introduction](#fixture-intro)
    - [Parameters](#fixture-parameters)
        - [Scopes](#fixture-scopes)
        - [Autouse](#fixture-autouse)
        - [Name](#fixture-name)
    - [Shared file](#fixtures-shared-file)
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
Python has a built-in tool named assert which is used to check a set of defined conditions.
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
### Fixture Decorator
#### Introduction <a name="fixture-intro"></a>
Fixtures are functions that take the `pytest.fixture()` decorator. Fixtures are reponsible of sending data that can be get after some coding, for example after a querie on a database. Their main utility is improving the readability and reuse of code. The whole signature / how the pytest fixture is defined is:
`@fixture(fixture_function: FixtureFunction, *, scope: `[Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.12)")`['session', 'package', 'module', 'class', 'function'] | `[Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.12)")`[[`[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.12)")`,` [Config](https://docs.pytest.org/en/stable/reference/reference.html#pytest.Config "_pytest.config.Config")`], `[Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.12)")`['session', 'package', 'module', 'class', 'function']] = 'function', params: `[Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "(in Python v3.12)")`[`[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.12)")`] | `[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.12)")` = None, autouse: `[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.12)")` = False, ids: `[Sequence](https://docs.python.org/3/library/typing.html#typing.Sequence "(in Python v3.12)")`[`[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.12)")` | `[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.12)")`] | `[Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.12)")`[[`[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.12)")`], `[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.12)")` | `[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.12)")`] | `[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.12)")` = None, name: `[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.12)")` | `[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.12)")` = None)`

The official [pytest documentation](https://docs.pytest.org/en/stable/reference/reference.html#pytest.fixture) has more informations about it, for further reading there’s also [here](https://docs.pytest.org/en/stable/reference/fixtures.html#fixture) to look at.

### Parameters <a name="fixture-parameters"></a>
#### Scopes <a name="fixture-scopes"></a>
The scopes of fixtures determine for how long a fixture is going to last untill it’s teardown. If a fixture has scope moudule all test in the same model will share the same fixture, the same will happen with the other scopes. The possible scopes are `session`, `package`, `module`, `class`, `function`. By default the `function` scope is used when using fixtures.
The scope order is `package` -> `class` -> `module` -> `session` -> `function`

#### Autouse <a name=”fixture-autouse”></a>
This parameter, when set to `TRUE`, makes all tests request them. For more information on this look at the [pytest documentation](https://docs.pytest.org/en/stable/how-to/fixtures.html#autouse-fixtures-fixtures-you-don-t-have-to-request).

#### Name <a name=”fixture-name”></a>
If a fixture should be called differently from how it was defined, the name parameter can define a call name for the fixture.

### Shared File <a name="fixtures-shared-file">
Pytest is able to locate fixtures on a file automatically applying them to the same directory by having them on a file named `conftest.py`. The fixtures in this file doen’t even need to be imported into the test files, pytest does all the heavy work. 

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
* `-v`: This flag makes the pytest verbose.
* `-vv`: Makes the pytest output even more verbose, in case of errors it will show each occurance that was different from what was expected.
* `-tb=no`: Turns off traceback messages of pytest.
* `-k`: Defines a search pattern for pytest searching of functions.
* `--setup-show`: Shows the setup and teardown of fixtures while exectuing tests. Pytest divides the fixtures show by test functions.
* `--fixtures`: Shows the available fixtures.
* `--fixtures-per-text`: Shows the fixtures used on each test, and where they are defined.
* `-s`: Turns off the output capture. Pytest, by default, only prints the output of failed tests.

---