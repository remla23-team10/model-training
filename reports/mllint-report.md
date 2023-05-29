# ML Project Report
**Project** | **Details**
--------|--------
Date    | Mon, 29 May 2023 21:31:03 +0200 
Path    | `/home/username/Documents/REMLA/model-training`
Config  | `.mllint.yml`
Default | No
Git: Remote URL | `https://github.com/remla23-team10/model-training.git`
Git: Commit     | `1f980f1a563fb2bec39e0168b21555aa57290abb`
Git: Branch     | `mlconfig`
Git: Dirty Workspace?  | No
Number of Python files | 13
Lines of Python code   | 142

---

## Config

**Note** — The following rules were disabled in `mllint`'s configuration:
- `dependency-management`

## Reports

### Version Control (`version-control`) — **96.9**%

Passed | Score | Weight | Rule | Slug
:-----:|------:|-------:|------|-----
✅ | 100.0% | 1 | Project uses Git | `version-control/code/git`
❌ | 75.0% | 1 | Project should not have any large files in its Git history | `version-control/code/git-no-big-files`
✅ | 100.0% | 1 | DVC: Project uses Data Version Control | `version-control/data/dvc`
✅ | 100.0% | 1 | DVC: Is installed | `version-control/data/dvc-is-installed`
✅ | 100.0% | 1 | DVC: Folder '.dvc' should be committed to Git | `version-control/data/commit-dvc-folder`
✅ | 100.0% | 1 | DVC: Should have at least one remote data storage configured | `version-control/data/dvc-has-remote`
✅ | 100.0% | 1 | DVC: Should be tracking at least one data file | `version-control/data/dvc-has-files`
✅ | 100.0% | 1 | DVC: File 'dvc.lock' should be committed to Git | `version-control/data/commit-dvc-lock`
 | _Total_ | | | 
❌ | **96.9**% | | Version Control | `version-control`

#### Details — Project should not have any large files in its Git history — ❌

Your project's Git history contains the following files that are larger than 10 MB:
- **14 MB** - commit `d09b2e084e402614843d82aba39997f5a6d9f28b` - `duplicateDetectionSet.csv`

These files may not necessarily be in your project right now, but they are still stored inside your project's Git history.
Thus, whenever your project is downloaded (with `git clone`), all these unnecessary files have to be downloaded as well.

See [this StackOverflow answer](https://stackoverflow.com/a/46615578/8059181) to learn how to remove these files from your project's Git history.

### Code Quality (`code-quality`) — **46.7**%

Passed | Score | Weight | Rule | Slug
:-----:|------:|-------:|------|-----
❌ | 20.0% | 1 | Project should use code quality linters | `code-quality/use-linters`
❌ | 60.0% | 1 | All code quality linters should be installed in the current environment | `code-quality/linters-installed`
❌ | 0.0% | 1 | Pylint reports no issues with this project | `code-quality/pylint/no-issues`
✅ | 100.0% | 1 | Pylint is configured for this project | `code-quality/pylint/is-configured`
❌ | 0.0% | 1 | Mypy reports no issues with this project | `code-quality/mypy/no-issues`
✅ | 100.0% | 1 | isort reports no issues with this project | `code-quality/isort/no-issues`
❌ | 0.0% | 0 | isort is properly configured | `code-quality/isort/is-configured`
 | _Total_ | | | 
❌ | **46.7**% | | Code Quality | `code-quality`

#### Details — Project should use code quality linters — ❌

Linters detected:

- Pylint


However, these linters were **missing** from your project:

- Mypy
- Black
- isort
- Bandit


We recommend that you start using these linters in your project to help you measure and maintain the quality of your code.

This rule will be satisfied, iff for each of these linters:
- **Either** there is a configuration file for this linter in the project
- **Or** the linter is a dependency of the project

Specifically, we recommend adding each linter to the development dependencies of your dependency manager,
e.g. using `poetry add --dev mypy` or `pipenv install --dev mypy`


#### Details — All code quality linters should be installed in the current environment — ❌

The following linters were not installed, so we could not analyse what they had to say about your project:

- Black
- Bandit


#### Details — Pylint reports no issues with this project — ❌

Pylint reported **24** issues with your project:

- `docs/conf.py:1,0` - _(C0114)_ Missing module docstring
- `docs/conf.py:35,0` - _(C0103)_ Constant name "source_suffix" doesn't conform to UPPER_CASE naming style
- `docs/conf.py:41,0` - _(C0103)_ Constant name "master_doc" doesn't conform to UPPER_CASE naming style
- `docs/conf.py:44,0` - _(C0103)_ Constant name "project" doesn't conform to UPPER_CASE naming style
- `docs/conf.py:44,10` - _(W1406)_ The u prefix for strings is no longer necessary in Python >=3.0
- `docs/conf.py:51,0` - _(C0103)_ Constant name "version" doesn't conform to UPPER_CASE naming style
- `docs/conf.py:53,0` - _(C0103)_ Constant name "release" doesn't conform to UPPER_CASE naming style
- `docs/conf.py:84,0` - _(C0103)_ Constant name "pygments_style" doesn't conform to UPPER_CASE naming style
- `docs/conf.py:94,0` - _(C0103)_ Constant name "html_theme" doesn't conform to UPPER_CASE naming style
- `docs/conf.py:167,0` - _(C0103)_ Constant name "htmlhelp_basename" doesn't conform to UPPER_CASE naming style
- `docs/conf.py:188,5` - _(W1406)_ The u prefix for strings is no longer necessary in Python >=3.0
- `docs/conf.py:189,5` - _(W1406)_ The u prefix for strings is no longer necessary in Python >=3.0
- `docs/conf.py:218,66` - _(W1406)_ The u prefix for strings is no longer necessary in Python >=3.0
- `docs/conf.py:219,6` - _(W1406)_ The u prefix for strings is no longer necessary in Python >=3.0
- `docs/conf.py:232,66` - _(W1406)_ The u prefix for strings is no longer necessary in Python >=3.0
- `docs/conf.py:233,5` - _(W1406)_ The u prefix for strings is no longer necessary in Python >=3.0
- `docs/conf.py:14,0` - _(W0611)_ Unused import os
- `docs/conf.py:15,0` - _(W0611)_ Unused import sys
- `setup.py:1,0` - _(C0114)_ Missing module docstring
- `test_environment.py:1,0` - _(C0114)_ Missing module docstring
- `test_environment.py:6,0` - _(C0116)_ Missing function or method docstring
- `test_environment.py:13,25` - _(C0209)_ Formatting a regular string which could be a f-string
- `test_environment.py:16,4` - _(R1720)_ Unnecessary "else" after "raise"
- `test_environment.py:18,12` - _(C0209)_ Formatting a regular string which could be a f-string


#### Details — Mypy reports no issues with this project — ❌

Mypy reported **29** issues with your project:

- `test_environment.py:6,1` - Error: Function is missing a return type annotation  [no-untyped-def]
- `test_environment.py:6,1` - Note: Use "-> None" if function does not return a value
- `test_environment.py:25,5` - Error: Call to untyped function "main" in typed context  [no-untyped-call]
- `setup.py:1,1` - Error: Skipping analyzing "setuptools": module is installed, but missing library stubs or py.typed marker  [import]
- `docs/conf.py:29,1` - Error: Need type annotation for "extensions" (hint: "extensions: List[<type>] = ...")  [var-annotated]
- `docs/conf.py:172,1` - Error: Need type annotation for "latex_elements" (hint: "latex_elements: Dict[<type>, <type>] = ...")  [var-annotated]
- `src/models/train_model.py:5,1` - Error: Skipping analyzing "joblib": module is installed, but missing library stubs or py.typed marker  [import]
- `src/models/train_model.py:7,1` - Error: Skipping analyzing "sklearn.feature_extraction.text": module is installed, but missing library stubs or py.typed marker  [import]
- `src/models/train_model.py:8,1` - Error: Skipping analyzing "sklearn.metrics": module is installed, but missing library stubs or py.typed marker  [import]
- `src/models/train_model.py:9,1` - Error: Skipping analyzing "sklearn.model_selection": module is installed, but missing library stubs or py.typed marker  [import]
- `src/models/train_model.py:10,1` - Error: Skipping analyzing "sklearn.naive_bayes": module is installed, but missing library stubs or py.typed marker  [import]
- `src/features/preprocessing.py:6,1` - Error: Skipping analyzing "joblib": module is installed, but missing library stubs or py.typed marker  [import]
- `src/features/preprocessing.py:6,1` - Note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
- `src/features/preprocessing.py:7,1` - Error: Skipping analyzing "nltk": module is installed, but missing library stubs or py.typed marker  [import]
- `src/features/preprocessing.py:9,1` - Error: Skipping analyzing "nltk.corpus": module is installed, but missing library stubs or py.typed marker  [import]
- `src/features/preprocessing.py:10,1` - Error: Skipping analyzing "nltk.stem.porter": module is installed, but missing library stubs or py.typed marker  [import]
- `src/features/preprocessing.py:11,1` - Error: Skipping analyzing "sklearn.feature_extraction.text": module is installed, but missing library stubs or py.typed marker  [import]
- `src/features/preprocessing.py:18,5` - Error: Function is missing a return type annotation  [no-untyped-def]
- `src/features/preprocessing.py:18,5` - Note: Use "-> None" if function does not return a value
- `src/features/preprocessing.py:28,5` - Error: Function is missing a type annotation  [no-untyped-def]
- `src/features/preprocessing.py:33,27` - Error: Call to untyped function "preprocess_review" in typed context  [no-untyped-call]
- `src/features/preprocessing.py:36,5` - Error: Function is missing a type annotation  [no-untyped-def]
- `src/features/preprocessing.py:46,5` - Error: Function is missing a type annotation  [no-untyped-def]
- `src/features/preprocessing.py:51,5` - Error: Function is missing a type annotation  [no-untyped-def]
- `src/features/preprocessing.py:58,5` - Error: Function is missing a type annotation  [no-untyped-def]
- `src/features/preprocessing.py:63,5` - Error: Function is missing a type annotation  [no-untyped-def]
- `src/features/preprocessing.py:68,5` - Error: Function is missing a type annotation  [no-untyped-def]
- `src/features/preprocessing.py:76,20` - Error: Call to untyped function "Preprocessing" in typed context  [no-untyped-call]
- `src/features/preprocessing.py:77,12` - Error: Call to untyped function "preprocess_dataset" in typed context  [no-untyped-call]


#### Details — isort reports no issues with this project — ✅

Congratulations, `isort` is happy with your project!

#### Details — isort is properly configured — ❌

isort is not properly configured.
In order to be compatible with [Black](https://github.com/psf/black), which mllint also recommends using,
you should configure `isort` to use the `black` profile.
Furthermore, we recommend centralising your configuration in your `pyproject.toml`

Thus, ensure that your `pyproject.toml` contains at least the following section:

```toml
[tool.isort]
profile = "black"
```


### Testing (`testing`) — **9.6**%

Passed | Score | Weight | Rule | Slug
:-----:|------:|-------:|------|-----
❌ | 38.5% | 1 | Project has automated tests | `testing/has-tests`
❌ | 0.0% | 1 | Project passes all of its automated tests | `testing/pass`
❌ | 0.0% | 1 | Project provides a test coverage report | `testing/coverage`
❌ | 0.0% | 1 | Tests should be placed in the tests folder | `testing/tests-folder`
 | _Total_ | | | 
❌ | **9.6**% | | Testing | `testing`

#### Details — Project has automated tests — ❌

There is **1** test file in your project, which meets the minimum of **1** test file required.

However, this only equates to **7.692308%** of Python files in your project being tests, while `mllint` expects that **20%** of your project's Python files are tests.

#### Details — Project passes all of its automated tests — ❌

No test report was provided.

Please update the `testing.report` setting in your project's `mllint` configuration to specify the path to your project's test report.

When using `pytest` to run your project's tests, use the `--junitxml=<filename>` option to generate such a test report, e.g.:
```sh
pytest --junitxml=tests-report.xml
```


#### Details — Project provides a test coverage report — ❌

No test coverage report was provided.

Please update the `testing.coverage.report` setting in your project's `mllint` configuration to specify the path to your project's test coverage report.

Generating a test coverage report with `pytest` can be done by adding and installing `pytest-cov` as a development dependency of your project. Then use the following command to run your tests and generate both a test report as well as a coverage report:
```sh
pytest --junitxml=tests-report.xml --cov=path_to_package_under_test --cov-report=xml
```


#### Details — Tests should be placed in the tests folder — ❌

The following test files have been detected that are **not** in the `tests` folder at the root of your project:

- /home/username/Documents/REMLA/model-training/test_environment.py


### Continuous Integration (`ci`) — **100.0**%

Passed | Score | Weight | Rule | Slug
:-----:|------:|-------:|------|-----
✅ | 100.0% | 1 | Project uses Continuous Integration (CI) | `ci/use`
 | _Total_ | | | 
✅ | **100.0**% | | Continuous Integration | `ci`

