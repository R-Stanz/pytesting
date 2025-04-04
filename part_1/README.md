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
- [Builtin Fixture](#builtin-fixture)
	+ [Temporary directories and files](#temporary-directories-and-files)
		* [tmp_path](#tmp_path)
		* [tmp_path_factory](#tmp_path_factory)
		* [tmpdir and tmpdir_factory](#tmpdir)
	+ [Output capture](#output-capture)
	+ [monkeypatch](#monkeypatch)
- [Testing](#testing)
    - [Testing a single file](#testing-a-single-file)
    - [Testing a single function](#testing-a-single-function)
    - [Testing multiple files](#testing-multiple-files)
    - [Most common Pytest flags](#most-common-pytest-flags)

---
### Conventions
Pytest follows a few conventions for discovering test files (as explained on the [pytest documentation](https://docs.pytest.org/en/7.1.x/explanation/goodpractices.html)). Making it simple, the rules for pytest default discovery / conventions:

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
### Fixture Decorator <a name="fixture-decorator"></a>
#### Introduction <a name="fixture-intro"></a>
Fixtures are functions that take the `pytest.fixture()` decorator. Fixtures are reponsible of sending data that can be get after some coding, for example after a querie on a database. Their main utility is improving the readability and reuse of code. The whole signature / how the pytest fixture is defined is:
`@fixture(fixture_function: FixtureFunction, *, scope: `[Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.12)")`['session', 'package', 'module', 'class', 'function'] | `[Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.12)")`[[`[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.12)")`,` [Config](https://docs.pytest.org/en/stable/reference/reference.html#pytest.Config "_pytest.config.Config")`], `[Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.12)")`['session', 'package', 'module', 'class', 'function']] = 'function', params: `[Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "(in Python v3.12)")`[`[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.12)")`] | `[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.12)")` = None, autouse: `[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.12)")` = False, ids: `[Sequence](https://docs.python.org/3/library/typing.html#typing.Sequence "(in Python v3.12)")`[`[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.12)")` | `[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.12)")`] | `[Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.12)")`[[`[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.12)")`], `[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.12)")` | `[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.12)")`] | `[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.12)")` = None, name: `[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.12)")` | `[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.12)")` = None)`

The official [pytest documentation](https://docs.pytest.org/en/stable/reference/reference.html#pytest.fixture) has more informations about it, for further reading there’s also [here](https://docs.pytest.org/en/stable/reference/fixtures.html#fixture) to look at.

#### Parameters <a name="fixture-parameters"></a>
##### Scopes <a name="fixture-scopes"></a>
The scopes of fixtures determine for how long a fixture is going to last untill it’s teardown. If a fixture has scope moudule all test in the same model will share the same fixture, the same will happen with the other scopes. The possible scopes are `session`, `package`, `module`, `class`, `function`. By default the `function` scope is used when using fixtures.
The scope order is `package` -> `class` -> `module` -> `session` -> `function`.
A scope can also be set dynamically, for example by passing a function that changes the values based on conditions - in the book there is an example where the function changes it scope based on the presence of a flag when calling pytest.

##### Autouse <a name=”fixture-autouse”></a>
This parameter, when set to `TRUE`, makes all tests request them. For more information on this look at the [pytest documentation](https://docs.pytest.org/en/stable/how-to/fixtures.html#autouse-fixtures-fixtures-you-don-t-have-to-request).

##### Name <a name=”fixture-name”></a>
If a fixture should be called differently from how it was defined, the name parameter can define a call name for the fixture.

#### Shared File <a name="fixtures-shared-file"></a>
Pytest is able to locate fixtures on a file automatically applying them to the same directory by having them on a file named `conftest.py`. The fixtures in this file doen’t even need to be imported into the test files, pytest does all the heavy work. 

---
### Builtin Fixtures <a name="builtin-fixture"></a>
#### Temporary directories and files <a name="#temporary-directories-and-files"></a>
Tests can be performed with files that are created during the tests. Pytest already uses a default directory store the temporary directories and files, but that can be changed if the pytest command has the flag `--basetemp=<path_to_temporary_directory>` the temporary directory is wiped before being used (in case there was already a directory with the same name before) or is created (in case there was no other directory with the same path). Pytest, after some time, **automatically deletes the contents of the temporary base directory!** For more info there you can check the [official documentation](https://docs.pytest.org/en/stable/how-to/tmp_path.html).

##### tmp_path <a name="tmp_path"></a>
This works as an object that contains methods to handle a temporary directory - one for each test function (function scope), by default. Sub-directories to the temporary base directory can be created with the `.mkdir()` method and temporary files as in the example bellow:
```python3
# content of test_tmp_path.py
CONTENT = "content"


def test_create_file(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "hello.txt"
    p.write_text(CONTENT, encoding="utf-8")
    assert p.read_text(encoding="utf-8") == CONTENT
    assert len(list(tmp_path.iterdir())) == 1
    assert 0
```


##### tmp_path_factory <a name="tmp_path_factory"></a>
Pretty similar to the [tmp_paht](tmp_path-fixture) but it works following the factory desing pattern. Bellow there is an example to save a image while using a session scope:
```
# contents of conftest.py
import pytest


@pytest.fixture(scope="session")
def image_file(tmp_path_factory):
    img = compute_expensive_image()
    fn = tmp_path_factory.mktemp("data") / "img.png"
    img.save(fn)
    return fn


# contents of test_image.py
def test_histogram(image_file):
    img = load_image(image_file)
    # compute and test histogram
```

##### tmpdir and tmpdir_factory <a name="tmpdir"></a>
These are legacy ways of dealing with temporary directories and files. They work in the same way of the above builtin fixtures with the exception that they use [py.path.local](https://py.readthedocs.io/en/latest/path.html) instead of the [pathlib.Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path).

#### Output capture <a name="output-capture"></a>
All the fixtures in this section allow access to `stdout`/`stderr` output created during test execution. The [official documentation](https://docs.pytest.org/en/stable/how-to/capture-stdout-stderr.html) also has some examples. <br>
The main fixtures are `capsys`, `capfd`, `capsbinary`, `capfdbbinary` and `caplog` - that is the only one that [works a little different from the others](https://docs.pytest.org/en/stable/reference/reference.html#std-fixture-caplog). 

#### monkeypatch <a name="monkeypatch"></a>
A fixture to a fixture that allows to make objects, dictionaries and enviroment variables modifications that can make them more convinent for testing. The documentation can be found [here](https://docs.pytest.org/en/stable/reference/reference.html#std-fixture-monkeypatch).<br>
List of functions of the monketpatch fixture (quoting the book):
- setattr(target, name, value, raising=True) -> Sets an attribute;
- delattr(target, name, raising=True) -> Deletes an attribute;
- setitem(dic, name, value) -> Sets a dictionary entry;
- delitem(dic, name, raising=True) -> Deletes a dictionary entry;
- syspath_prepend(path) -> Prepends path to sys.path, wich is Python's list of import locations;
- chdir(path) -> Changes the current working directory.

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